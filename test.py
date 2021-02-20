from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getKRIndstrClsfStndIndtpInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'Ijgvh4BB2r0xFk8W%2BMguZoKtmkhYx8sEHdg7Zt8sJ3pjXmliwopc1jcx4Mmmh9G1%2FC4qTtmn8splNsbyuEAWtQ%3D%3D', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('indtpClsfNo') : 'K64110' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)