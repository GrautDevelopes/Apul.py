#Main page for Apul.py http://github.com/GrautDevelopes/Apul.py/
#Very alpha. Expect bugs!
#Only use redirectors that go to blobar and don't go to clickvalidator.net. Examples:
#Usage `python Apul.py http://youtuber.com/ youtuber.com.log` 
#http://youtuber.com/
#http://pete.com/
#http://youtibe.com/
# @Thunder when you get script sorted out.
import urllib2
import sys
import re
import os
print("[Apul] Starting...")
print("[Apul] Checking " + sys.argv[1] + " ...")
req = urllib2.Request(sys.argv[1], headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' })
RedirectorResponse = urllib2.urlopen(req)
RedirectorResponseHTML = RedirectorResponse.read()
RedirectorResponse.close()
def clean_text(rgx, text):
    new_text = text
    new_text = re.sub(rgx, '', new_text)
    return new_text
def save():
     logstream = open(sys.argv[2], 'a+') #Was 'w'
     for item in Popups:
         logstream.write("%s\n" % item)
     logstream.close()
def getnewblobarurl():
     req = urllib2.Request(sys.argv[1], headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' })
     RedirectorResponse = urllib2.urlopen(req)
     RedirectorResponseHTML = RedirectorResponse.read()
     RedirectorResponse.close()
     trim0 = clean_text('.*var u = \'', RedirectorResponseHTML)
     trim1 = clean_text('\'\+\(\(r.*', trim0)
     req2 = urllib2.Request(clean_text('\'\+\(\(.*', trim1))
     Redirector2Response = urllib2.urlopen(req2)
     Redirecter3url = Redirector2Response.geturl() + "&z=240"
     Redirector2Response.close()
     return Redirecter3url
     #print("[Apul] Resolving " + Redirecter3url + " ...") #The blobar url
if "http://blobar.org/d/p" in RedirectorResponseHTML:
    print("[Apul] Verifed " + sys.argv[1] + " !")
    Popups = []
    while True:
         req3 = urllib2.Request(getnewblobarurl(), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' })
         Redirector3Response = urllib2.urlopen(req3)
         PopUpHTML = Redirector3Response.read() #TODO: Extract phone number from popup
         PopUpURL = Redirector3Response.geturl()
         if PopUpURL == 'http://ww90.blobar.org/':
		     getnewblobarurl()
         num = re.search(r"(((((\(\d{3})|(\s\d{3}))((\)|-)|(\s|\) )|(\)-)?))?)|(\d{3}(-|\s)))?\d{3}(-|\s)\d{4}", PopUpHTML)#.group(0) #Much thanks to Eclipse. Created by Eclipse for Graut and the scambaiting community. https://0-eclipse-0.github.io/phone_regex.txt
         Redirector3Response.close()
         if num:
             ##print(PopUpURL + " | " + num)
             #Popups.append(PopUpURL + " | " + num)
			 Popups.append(PopUpURL + " | {}".format(num.group(0)))
             #print(PopUpURL + " | {}".format(num.group(0)))
         else:
             Popups.append(PopUpURL)
             #print(PopUpURL)
         Popups = list(set(Popups))
         Popups.sort()
         if os.name == 'nt':
              _=os.system("cls")
         if os.name != 'nt':
              _=os.system("clear")
         print "\n".join(Popups)
         save()
else:
    print("[Apul] The redirector " + sys.argv[1] + " does not use blobar.")
