# brevis-python-client
Python Client for the [Brevis](https://github.com/admiralobvious/brevis) URL shortener API

## How-to use

```
>>> import brevis
>>> client = brevis.BrevisClient('https://brevis-server')
>>> short = client.shorten('https://google.com')
>>> print(short)
{'shortUrl': 'https://brevis-test.klik.co/Hz9YqVphB'}
>>> long = client.unshorten(short['shortUrl'])
>>> print(long)
{'url': 'https://google.com'}
```
