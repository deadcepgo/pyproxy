import requests
from lxml import html

class Proxy():
    headers = {
        'Accept':'*/*',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }
    def __init__(self,limit=10,mycode=None):
        self.mycode = mycode
        self.limit = limit
    def get_paid_proxies(self):
        url     = 'https://hidemy.name/ru/loginx'
        url1    = 'https://hidemy.name/api/proxylist.txt?out=plain&lang=ru'
        data    = {'c' : self.mycode}
        if self.mycode is not None:
            try:
                s       = requests.session()
                s.get(url1, headers = self.headers)
                s.post(url, data = data, headers= self.headers)
                res     = s.get(url1, headers = self.headers)
            except Exception as e:
                print e
                return []
            result  = res.text.split('\r\n')
            random.shuffle(result)
            return result
        else:
            print 'Please input your code on hidemy.name Proxy(mycode="12345")'
            return []
    def get_free_proxies(self)
        result  = []
        url     = 'https://www.us-proxy.org'
        try:
            res     = requests.get(url, headers = self.headers).content
        except Exception as e:
            print e
            return []
        page    = html.fromstring(res)
        ips     = page.xpath('//table[@id="proxylisttable"]/tbody/tr/td[1]/text()')
        ports   = page.xpath('//table[@id="proxylisttable"]/tbody/tr/td[2]/text()')
        for i, ip in enumerate(ips):
            result.append(':'.join([ip,ports[i]]))
        random.shuffle(result)
        return result
    def validate_proxies(self,proxies,url):
        proxys  = []
        for proxy in proxies:
            bad_proxy = is_bad_proxy(proxy,url)
            if not bad_proxy:
                print proxy, "APPROVED!"
                proxys.append({'http':proxy})
                if len(proxys) == self.limit:
                    break
	    elif str(bad_proxy)[0] == '5' and len(proxys) == 0:
	        print 'This service is now unavailable (site from scraping is unavailable)'
        if len(proxys) == 0:
            return 0
        return proxys