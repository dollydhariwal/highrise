highrise
========


System requirement:

Linux OS (any flavour, 12.04 LTS preferred)

python > 2.6

python-requests (sudo apt-get install python-requests)
python-urllib (sudo apt-get install python-urllib)


Tool Access:

You can access the tool using github

https://github.com/dollydhariwal/highrise

> git clone https://github.com/dollydhariwal/highrise
> cd highrise
highrise> 


How to run the Tool:

highrise> python highrise.py

Welcome to the HighRise User Management tool
What would you like to do today?



1. List Contacts
2. Create Contact
3. List Task/s
4. Create Task
5. Search User
6. Exit


Please Select Operation[1-6]:



Currently on the (option 1) is working.  User can select to list the contacts for the following account:

https://organization223.highrisehq.com


(I have created a dummy account here with username/password as such:   ddhariwal/0p3nb00t)



How to customize it to use for yourself:

For now you can change the parameters in highrise.py file to enter your url and login details. Later plan to change the highrise.py as a module and write a separate script for configs, but for now this is what I have.


In main function change the following highlighted in RED:

def main(argv=sys.argv):
  os.system('clear')
  print "Welcome to the HighRise User Management tool"
  print "What would you like to do today?\n\n\n"

  while(1):
    choice = printMainMenu()
    while (choice < 1 or choice > 6):
      os.system('clear')
      print "-----Invalid Selection-----"
      print "Please Choose one of the following:"
      choice = printMainMenu()
    if choice == 6:
      print "Goodbye"
      sys.exit(1)
    else:
     hl = Highrise("https://organization223.highrisehq.com","77427d6a0fae05a6bd5a34df27221ab1")
     hl.connection()





1. The url is basically the url provided to you by highrise.
2. The token you can find from here:  http://welovehighriseblog.wordpress.com/2012/02/14/faq-where-can-i-find-my-highrise-api-token/
