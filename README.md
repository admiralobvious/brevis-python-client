# brevis-python-client
Python Client for the Brevis URL shortener API

## How-to use

```
>>> import brevis
>>> client = brevis.BrevisClient('https://brevis-server')
>>> short = client.shorten('https://google.com')
>>> print(short)
{u'url': u'https://google.com', u'shortUrl': u'https://brevis-test.klik.co/Hz9YqVphB'}
>>> long = client.unshorten(short['shortUrl'])
>>> print(long)
{u'url': u'https://google.com', u'shortUrl': u'https://brevis-test.klik.co/Hz9YqVphB'}
```
