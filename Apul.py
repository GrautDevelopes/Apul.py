#!/usr/bin/python
# -*- coding: utf-8 -*-
# Main page for Apul.py http://github.com/GrautDevelopes/Apul.py/
# I guess we are in beta now.
# Only use redirectors that go to blobar and not to clickvalidator.net. Examples:
# Example: python Apul.py http://youtuber.com/ youtuber.com.log
# http://youtuber.com/
# http://pete.com/
# http://httfacebook.com/

import urllib2
import httplib
import base64
import sys
import re
import os
import time
import pytz
from datetime import datetime
if len(sys.argv) < 3:
    sys.exit('Usage: python Apul.py http://example.com/ example.log')
print '[Apul] Starting Release 030418.2 ...'  # Release numbers are based on date released in US format with possible number after showing version of that day.
print '[Apul] Checking ' + sys.argv[1] + ' ...'
print '[Apul] Getting timezone...'
print '[Apul] If you are outside US/Eastern timezone, change code below to correct timezone.'
timezonename = 'US/Eastern' #Change code here


def is_dst ():
    """Determine whether or not Daylight Savings Time (DST)
    is currently in effect (https://gist.github.com/dpapathanasiou/09bd2885813038d7d3eb)"""

    x = datetime(datetime.now().year, 1, 1, 0, 0, 0, tzinfo=pytz.timezone(timezonename)) # Jan 1 of this year
    y = datetime.now(pytz.timezone(timezonename))

    # if DST is in effect, their offsets will be different
    return not (y.utcoffset() == x.utcoffset())    
    
if is_dst():
    utcoffsetinmin = str(time.timezone / 60 - 60)
else:
    utcoffsetinmin = str(timezone / 60)
print '[Apul] ' + utcoffsetinmin + ' is current offset. ' + timezonename + ' is current timezone.'

### Config ######################
# Feel free to change these if you know what you're doing.
### Useragent ###################
ua = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'  # Chrome
# ua = 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko'  #Internet Explorer
# ua = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0' #Edge
# ua = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fi-fi) AppleWebKit/420+ (KHTML, like Gecko) Safari/419.3' #Mac Safari
# ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.38 (KHTML, like Gecko) Version/10.0 Mobile/14A5297c Safari/602.1' #iPhone Safari
# ua = 'Insert own useragent here' #Custom
#################################

req = urllib2.Request(sys.argv[1], headers={'User-Agent': ua})
try:
    redirectorresponse = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print '[ERROR] HTTPError: ' + str(e.code) + ', could not reach ' \
        + sys.argv[1]
    pass
except urllib2.URLError, e:
    print '[ERROR] URLError: ' + str(e.reason) + ', could not reach ' \
        + sys.argv[1]
    pass
except httplib.HTTPException, e:
    print '[ERROR] HTTPException, could not reach ' + sys.argv[1]
    pass
except Exception:
    import traceback
    print '[ERROR] Generic exception: ' + traceback.format_exc() \
        + ', could not reach ' + sys.argv[1]
    pass
redirectorresponseHTML = redirectorresponse.read()
redirectorresponse.close()


def clean_text(rgx, text):
    new_text = text
    new_text = re.sub(rgx, '', new_text)
    return new_text


def save():
    logstream = open(sys.argv[2], 'a+')  # Was 'w'
    for item in Popups:
        logstream.write('%s\n' % item)
    logstream.close()
    lines = open(sys.argv[2], 'r').readlines()
    lines_set = set(lines)
    logstream.close()
    out = open(sys.argv[2], 'w')
    for line in lines_set:
        out.write(line)


def getnewblobarurl():
    req = urllib2.Request(sys.argv[1], headers={'User-Agent': ua})
    try:
        redirectorresponse = urllib2.urlopen(req)
        redirectorresponseHTML = redirectorresponse.read()
        redirectorresponse.close()
    except urllib2.HTTPError, e:
        print '[ERROR] HTTPError: ' + str(e.code) \
            + ', could not reach ' + sys.argv[1]
        pass
    except urllib2.URLError, e:
        print '[ERROR] URLError: ' + str(e.reason) \
            + ', could not reach ' + sys.argv[1]
        pass
    except httplib.HTTPException, e:
        print '[ERROR] HTTPException, could not reach ' + sys.argv[1]
        pass
    except Exception:
        import traceback
        print '[ERROR] Generic exception: ' + traceback.format_exc() \
            + ', could not reach ' + sys.argv[1]
        pass
    trim0 = clean_text('.*var u = \'', redirectorresponseHTML)
    trim1 = clean_text('\'\+\(\(r.*', trim0)
    trim2 = clean_text('\'\+\(\(.*', trim1)
    Redirecter3url = trim2 + '2.1.' + base64ofdomain + '&r=&z=' \
        + utcoffsetinmin

    # print("[Apul] Resolving " + Redirecter3url + " at " + sys.argv[1] + " ...") #The blobar url, disabled because we don't clear our screen anymore

    return Redirecter3url


if 'related content to what you are looking for' \
    in redirectorresponseHTML:
    print '[Apul] Verifed ' + sys.argv[1] + ' !'
    base64ofdomain = base64.urlsafe_b64encode(clean_text('/',
            clean_text('.*://', sys.argv[1])))
    Popups = []
    while True:
        currentblobarurl = getnewblobarurl()
        req3 = urllib2.Request(currentblobarurl,
                               headers={'User-Agent': ua})
        Redirector3Response = urllib2.urlopen(req3)
        try:
            Redirector3Response = urllib2.urlopen(req3)
            PopUpHTML = Redirector3Response.read()
            PopUpURL = re.sub('htt', 'hxx',
                              Redirector3Response.geturl())
        except urllib2.HTTPError, e:
            print '[ERROR] HTTPError: ' + str(e.code) \
                + ', could not reach ' + currentblobarurl \
                + 'to redirect to ' + PopUpURL
            pass
        except urllib2.URLError, e:
            print '[ERROR] URLError: ' + str(e.reason) \
                + ', could not reach ' + currentblobarurl \
                + 'to redirect to ' + PopUpURL
            pass
        except httplib.HTTPException, e:
            print '[ERROR] HTTPException, could not reach ' \
                + currentblobarurl + 'to redirect to ' + PopUpURL
            pass
        except Exception:
            import traceback
            print '[ERROR] Generic exception: ' \
                + traceback.format_exc() + ', could not reach ' \
                + currentblobarurl + 'to redirect to ' + PopUpURL
            pass
        if 'ww90.' in PopUpURL:
            getnewblobarurl()
        num = \
            re.search(r"(((((\(\d{3})|(\s\d{3}))((\)|-)|(\s|\) )|(\)-)?))?)|(\d{3}(-|\s)))?\d{3}(-|\s)\d{4}"
                      , PopUpURL + PopUpHTML)

               # .group(0) #Much thanks to Eclipse. Created by Eclipse for Graut and the scambaiting community. https://0-eclipse-0.github.io/phone_regex.txt

        Redirector3Response.close()
        if base64ofdomain not in PopUpURL:  # Detection could be improved, small patch for now.
            if num:
                outline = PopUpURL + ' | {}'.format(num.group(0))
            else:
                outline = PopUpURL
                Popups = list(set(Popups))
                Popups.sort()
                if outline not in Popups:
                    print outline
                    Popups.append(outline)
                    save()
    else:
        print '[Apul] The redirector ' + sys.argv[1] \
            + ' does not use blobar.'
