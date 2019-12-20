import requests
from lxml.html import fromstring
from itertools import cycle


def _get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def _get_valid_proxy():
    proxies = _get_proxies()
    proxy_pool = cycle(proxies)
    url = 'https://httpbin.org/ip'
    validproxy = False
    returnproxy = None
    while not validproxy:
        proxy = next(proxy_pool)
        print("Getting new proxy, standby...")
        try:
            print("Trying proxy "+proxy)
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
            validproxy = True
            returnproxy = proxy
            print("Got proxy "+returnproxy)
        except Exception as e:
            print(e)
            validproxy = False
    return returnproxy
