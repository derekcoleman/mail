import email, getpass, imaplib, os, quopri, re
from HTMLParser import HTMLParser

f = open('workfile', 'w')

word = '…'
detach_dir = '.' # directory where to save attachments (default: current)
#user = raw_input("Enter your GMail username:")
#pwd = getpass.getpass("Enter your password: ")
user = "…"
pwd ="…"

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("[Gmail]/INBOX",readonly=True) # here you a can choose a mail box like INBOX instead
# use m.list() to get all the mailboxes
print m.list()
#resp, items = m.search(None, 'FROM', "eileenbernardi@gmail.com") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
resp, items = m.search(None, '(SINCE "01-Jan-2008")')
items = items[0].split() # getting the mails id

for emailid in items:
    resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
    email_body = data[0][1] # getting the mail content
    mail = email.message_from_string(email_body) # parsing the mail content to get a mail object

    if word in email_body:

        body=quopri.decodestring(email_body)
        t = re.findall ( 'Date:([^X]*)', body, re.DOTALL)
        #print body
        print("\n")
        print(re.sub("<.*?>", " ", str(t)))
        print("-------------------\n\n\n\n")