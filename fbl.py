import urllib2
import cookielib
import urllib
import re

if __name__ == '__main__':
    urlLogin = 'http://www.facebook.com/login.php'

    id    = 'tiffanymorethanyou@gmail.com'
    passw = 'chunky1'

    fieldId   = 'email'
    fieldPass = 'pass'

    cj = cookielib.CookieJar()
    data = urllib.urlencode({fieldId:id, fieldPass:passw})

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    urllib2.install_opener(opener)

    usock = opener.open(urlLogin)
    usock = opener.open(urlLogin, data)
    pageSource = usock.read()
    usock.close()
    print(pageSource)

    usock = opener.open('http://www.facebook.com/ads/adboard/')
    pageSource = usock.read()
    usock.close()
    print(pageSource)

    #find images
    adimgs = re.compile('[a-zA-Z0-9_]*.jpg')
    fimgs = adimgs.findall(pageSource)
    print "list of images",fimgs
