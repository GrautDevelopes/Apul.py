# Apul.py
Apul (Automatic PopUp Logger) automatically gets tech support scammer popups and their numbers from blobar redirectors and logs them to a console or file.
# Usage
`python Apul.py http://pete.com/ pete.com.log`
# Not getting anything?
If your not in my timezone they're might be an issue. Copy this in the url bar and add a 'j' to the front, press enter.
`avascript:var z = (new Date()).getTimezoneOffset();alert(z);`
Remember the number that showed up. Find and replace `&z=240` on line 37 with `&z=` and the number that showed up. If your number is also 240 it means the time isn't the issue. Change the useragent on both lines 29 and 45 to another browser, preferrably Chrome or IE/Edge.
