from lxml import html
import requests
import time
import string

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
}

param = {
    'category': 'Sk_ermar.TFT__23__-__24'
}

login = {
    'action': 'LOGIN',
    'email': 'email',
    'password': 'pass,
    'login': 'Logga+In'
}

payload = {
    'itemID': '102732',
    'action': 'WATCH',
    'centeredItem': '102732',
    'amount': 1,
    'laggbud': 'L%E4gg+bud'
}

s = requests.Session()
url = 'https://www.it-auktion.se/index.jsp'
result = s.post(url, headers=header, data=login, verify='./cert.crt')
print (result.ok)
print (result.status_code)
print (s.cookies)
print (result.url)
result = s.post(url, headers=header, data=payload, verify='cert.crt')
tree = html.fromstring(result.content)
items = tree.xpath('//*[@id="user"]/text()')
bids = tree.xpath('//*[@id="pris"]/text()')
print (result.ok)
print (result.status_code)
print (s.cookies)
print (result.url)
print (str(items).strip())
print (str(bids).strip())

while False:

    result = requests.get('https://www.it-auktion.se/index.jsp?category=Sk_ermar.TFT__23__-__24', data=login, verify='cert.crt')
    tree = html.fromstring(result.content)
    result = requests.post('https://www.it-auktion.se/index.jsp?category=Sk_ermar.TFT__23__-__24', data=payload, verify='cert.crt')

    # items = tree.xpath('//span[@class="titleauk"]//span//h2/text()')
    items = tree.xpath('//*[@id="produktnamn"]//h2/text()')

    bidding = tree.xpath('//*[@id="budgivare"]/h5/text()')


    items = str(items.pop(0).strip())

    print ('Items:', items)
    if 'HP - LA2405x' in items:
        bids = tree.xpath('//*[@id="form102667"]//div[@id="pris"]//p/text()')
        bidders = tree.xpath('//*[@id="form102667"]//div[@id="budgivare"]//p/text()')
        bidsList = []
        biddersList = []
        for i in range (len(bids)):
            bidsList.insert(0, str(bids[i]).strip())
            biddersList.insert(0, str(bidders[i]).strip())

        for i in range (len(bids)):
            print (bidsList[i] + ': ' + biddersList[i])

        # if biddersList[0] is not 'xMez':
        #     #


        print ('YES')
    time.sleep(5)
