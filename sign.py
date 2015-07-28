import cookielib
import urllib
import urllib2
import zlib
import time


# Store the cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [
    ('Origin', 'http://www.zimuzu.tv'),
    ('Accept-Encoding', 'gzip, deflate'),
    ('Accept-Language', 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'),
    ('Content-Type', 'application/x-www-form-urlencoded'),
    ('Accept', 'application/json, text/javascript, */*; q=0.01'),
    ('Referer', 'http://www.zimuzu.tv/user/login'),
    ('X-Requested-With', 'XMLHttpRequest'),
    ('Connection', 'keep-alive'),
    ('DNT', '1'),
]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib2.install_opener(opener)

# The action/ target from the form
authentication_url = 'http://www.zimuzu.tv/User/Login/ajaxLogin'

# Use urllib to encode the payload
data = urllib.urlencode({
    'account':'YOUR@EMAIL.COM',
    'password':'YOURPASSWORD',
})

# Build our Request object (supplying 'data' makes it a POST)
req = urllib2.Request(authentication_url, data)

# Make the request and read the response
resp = urllib2.urlopen(req)
# contents = resp.read()
# decompressed_data = zlib.decompress(contents, 16+zlib.MAX_WBITS)

# now we visit sign page
req = urllib2.Request('http://www.zimuzu.tv/user/sign')
resp = urllib2.urlopen(req)
# contents = resp.read()
# decompressed_data = zlib.decompress(contents, 16+zlib.MAX_WBITS)

time.sleep(16)
req = urllib2.Request('http://www.zimuzu.tv/user/sign/dosign') #actually sign
resp = urllib2.urlopen(req)
contents = resp.read()
decompressed_data = zlib.decompress(contents, 16+zlib.MAX_WBITS)

import json

try:
  if json.loads(decompressed_data)['status'] == '1':
    print 'Sign successful!'
  else:
    print 'Sign faild, Data: %s' % decompressed_data
except:
    print 'Sign failed! DATA:%s' % decompressed_data

