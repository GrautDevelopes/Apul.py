#Main page for Apul.py http://github.com/GrautDevlopes/Apul.py/
#Very alpha. Expect bugs!
#Only use redirectors that go to blobar and don't go to clickvalidator.net. Examples:
#http://youtuber.com/ << Redirects to clickvalidator
#http://pete.com/ << The only one that seems to work
#http://youtibe.com/ << Redirects to clickvalidator
import urllib2
import sys
import re
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
if "http://blobar.org/d/p" in RedirectorResponseHTML:
     print("[Apul] Verifed " + sys.argv[1] + " !")
     while True:
          trim1 = RedirectorResponseHTML[244:]
          req2 = urllib2.Request(clean_text('"><META name="r.*', trim1))
          Redirector2Response = urllib2.urlopen(req2)
          Redirecter3url = Redirector2Response.geturl() + "&z=240"
          Redirector2Response.close()
          #print("[Apul] Resolving " + Redirecter3url + " ...") #The blobar url
          req3 = urllib2.Request(Redirecter3url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' })
          Redirector3Response = urllib2.urlopen(req3)
          PopUpHTML = Redirector3Response.read() #TODO: Extract phone number from popup
          PopUpURL = Redirector3Response.geturl()
          print(PopUpURL);
          Redirector3Response.close()
     else:
	      print("[Apul] The redirector " + sys.argv[1] + " does not use blobar.")
