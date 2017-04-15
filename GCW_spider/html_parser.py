from bs4 import BeautifulSoup
import re
import urllib

class HtmlParser(object):

    def parse(self, page_url, html_cont,resultlistM,resultlistS):
        if page_url is None or html_cont is None:
           return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        # print(soup)
        new_urls=self._get_new_urls(page_url,soup)
        new_resultlistM,new_resultlistS=self._get_new_data(resultlistM,resultlistS,soup)
        return new_urls,new_resultlistM,new_resultlistS

    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        #< a href = "/ns?word=%E5%8D%9A%E6%97%B6%E6%9D%A8%E9%94%90&amp;pn=60&amp;cl=2&amp;ct=1&amp;tn=news&amp;rn=20&amp;ie=utf-8&amp;bt=0&amp;et=0" >
        # < span class ="fk fkd" > < i class ="c-icon c-icon-bear-pn" > < / i > < / span > < span class ="pc" > 4 < / span > < / a >
        # print(soup)
        links=soup.find_all('a', href=re.compile(r"/s\?wd=.*pn=[^0].*"))
        if links is None:
            print("what's the fuck!")
        for link in links:
            new_url=link['href']
            # print(new_url+"********************************************************")
            if new_url.endswith('-1') or new_url.endswith('1'):
                continue
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            url = new_full_url.split('&')[0:3]
            url = url[0] + '&' + url[1] + '&' + url[2]
            new_urls.add(url)
        return new_urls

    def data_process(self,data):
        data=re.sub("\D","",data)
        if len(data)==7 or len(data)==6:
            real_data=int(data[0:4])*100+int(data[5])
        elif len(data)==8:
            real_data=int(data[0:6])
        else:
            #print("data erros!")
            #print(data)
            real_data=0

        return real_data

    def _get_new_data(self, resultlistM,resultlistS, soup):
        res_data=[]
        #res_data['url']=page_url


        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        #title_node=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        #nodes=soup.find_all('div',class_="result")
        #< span class =" newTimeFactor_before_abs m" > 2012年8月5日 & nbsp;- & nbsp; < / span >
        nodes=soup.find_all('span',class_=" newTimeFactor_before_abs m")
        for node in nodes:
            realdata=self.data_process(node.get_text())
            if realdata==0:
                #print(node.get_text())
                continue

            index = int((realdata - 200100) / 100) * 12 + ((realdata - 200100) % 100)
            index = 16 * 12 - index

            index2 = int((realdata - 200100) / 100) * 4 + int(int(((realdata - 200100) % 100) - 1) / 3)
            index2 = 16 * 4 - index2-1

            resultlistM[index] = resultlistM[index] + 1
            resultlistS[index2] = resultlistS[index2] + 1


        return resultlistM, resultlistS


        #< p class ="c-author" > 凤凰网 & nbsp; & nbsp;2014年07月29日 15:00 </ p >

        # for node in nodes:
        #     time=node.find('p',class_="c-author")
        #     realdata=self.data_process(time.get_text())
        #     if realdata>201612 or realdata<200101:
        #         print("time out of range")
        #         continue
        #
        #     index=int((realdata-200100)/100)*12+((realdata-200100)%100)
        #     index=16*12-index+1
        #
        #
        #     index2=int((realdata-200100)/100)*4+int(((realdata-200100)%100)/4)
        #     index2=16*4-index2+1
        #
        #
        #     num=node.find('a',class_="c-more_link")
        #     if num is None:
        #         resultlistM[index] = resultlistM[index] + 1
        #         resultlistS[index2] = resultlistM[index] + 1
        #
        #     else:
        #         realnum=self.data_process(num.get_text())
        #         resultlistM[index]=resultlistM[index]+realnum
        #         resultlistS[index2] = resultlistM[index] + realnum

        #summary_node=soup.find('div',class_="lemma-summary")
        #res_data['summary']=summary_node.get_text()









