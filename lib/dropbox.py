#!/usr/bin/env python

import time
import requests
import dropbox

app_key = 'yflj5de801oqhbg'
app_secret = '30bmjjbhvvlfn7g'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

print 'Go here and "allow": %s' % flow.start()
code = raw_input('Paste in your authorization code: ').strip()

access_token, _ = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)

cursor = None
while True:
    result = client.delta(cursor)
    cursor = result['cursor']
    if result['reset']:
        print 'RESET'

    for path, metadata in result['entries']:
        if metadata is not None:
            print '%s was created/updated' % path
        else:
            print '%s was deleted' % path

    # if has_more is true, call delta again immediately
    if not result['has_more']:

        changes = False
        # poll until there are changes
        while not changes:
            response = requests.get('https://api-notify.dropbox.com/1/longpoll_delta',
                params={
                    'cursor': cursor,  # latest cursor from delta call
                    'timeout': 120     # default is 30 seconds
                })
            data = response.json()

            changes = data['changes']
            if not changes:
                print 'Timeout, polling again...'

            backoff = data.get('backoff', None)
            if backoff is not None:
                print 'Backoff requested. Sleeping for %d seconds...' % backoff
                time.sleep(backoff)
                print 'Resuming polling...'
