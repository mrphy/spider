
import urllib.request
import ssl


class HtmlDownoader(object):
    ssl._create_default_https_context = ssl._create_unverified_context
    def download(self, url):
        if url is None:
            return None
        # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows  NT)'
        # headers = {'User-Agent': user_agent}

        headers={
            # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    #'Accept-Encoding':'gzip, deflate, sdch, br',
                    # 'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
                    'Connection':'keep-alive',
                    #'Cookie':'BAIDUID=ACA7A4AD2ACB29B6C1BBD49107A32A33:FG=1; BIDUPSID=B49DB871FA6CA8EC12F8EEA1FA4D920B; PSTM=1461832892; __cfduid=dffac1b1d0addf813e8c53cec6436f7aa1473648149; MCITY=-131%3A; BDUSS=VoNzczTElaVkxoTWpmclQ3My1jUWZHazFvdU5aZ0pLTlZUam9XWFU5VWtUS1ZZSVFBQUFBJCQAAAAAAAAAAAEAAACDrgYKdGhvbWFzMTM5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACS~fVgkv31YVU; ispeed_lsm=2; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; shifen[55616578655_13683]=1488114620; BCLID=1530356930622988985; BDSFRCVID=bG-sJeC62u-ncHRi4rmk-tZITg5MDc7TH6aIaPlJErCCoJs8EKGmEG0Pqf8g0Ku-Nb29ogKK0mOTHvbP; H_BDCLCKID_SF=tR4t_K0-fC03fP36q45H24k0-qrtetJyaR3aK56bWJ5TMCoGqtTjyhDtjh5LaKrJye5n0K5z3n8bShPC-frH0-ApQq5m3-RZ-bb4ah3E3l02V-jIe-t2ynQDXxKHq4RMW20jWl7mWPQDVKcnK4-Xj5j3jHjP; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=1422_21086_20697_22036_22175_22072; BD_UPN=12314753; H_PS_645EC=2bf9NNSjYxAjFdRgcVXWXpQLwQkCQENApgLpMF7WIQnBIE52NblQG0wjyDU',
                    'Host':'www.baidu.com',
                    # 'Upgrade-Insecure-Requests':'1',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        }

        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        if response.getcode()!=200:
            print(response.getcode())
            return None
        #print(response.read())
        #print("*******************************")
        return response.read()
