#/usr/bin/env python

import os,sys
import time
import requests
# Include the Dropbox SDK libraries
from dropbox import client, rest, session
sys.path.insert(1, '%s/lib' % os.getcwd())
from highrise import *

# Get your app key and secret from the Dropbox developer website

APP_KEY = 'yflj5de801oqhbg'
APP_SECRET = '30bmjjbhvvlfn7g'
ACCESS_TYPE = 'dropbox'


sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE )

request_token = sess.obtain_request_token()
#request_token = "sq0rqeB985agW3hD"
# Make the user sign in and authorize this token
url = sess.build_authorize_url(request_token)
print "url:", url
print "Please authorize in the browser. After you're done, press enter."
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)

client = client.DropboxClient(sess)
#stored_creds = open(CONF_DIR + self.TOKEN_FILE).read()
print "linked account:", client.account_info()
print "display name:", client.account_info()['display_name']


cursor = None
while True:
    result = client.delta(cursor)
    cursor = result['cursor']
    if result['reset']:
        print 'RESET'

    for path, metadata in result['entries']:
        if metadata is not None:
            print '%s was created/updated' % path
	    hl = Highrise("https://organization223.highrisehq.com","77427d6a0fae05a6bd5a34df27221ab1")
	    hl.createAutoNote( client.account_info()['display_name'])

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
                    'timeout': 360     # default is 30 seconds
                })
	    print response.content
            data = response.content

            changes = data[changes]
            if not changes:
                print 'Timeout, polling again...'

            backoff = 60
            if backoff is not None:
                print 'Backoff requested. Sleeping for %d seconds...' % backoff
                time.sleep(backoff)
                print 'Resuming polling...'

