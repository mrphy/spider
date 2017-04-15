
import url_manager,html_downloader,html_parser,html_output
import xlwt
import xlrd
import urllib
import time


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownoader()
        self.parser=html_parser.HtmlParser()
        self.output=html_output.HtmlOutputer()
    def craw(self,sheet1,sheet2,root_url,num,name):
        count=1
        listZeros=[0]
        resultlistM=listZeros*((2016-2000)*12)
        resultlistS = listZeros * ((2016 - 2000) * 4)


        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print('crawling URL => %d ... : %s' % (count, new_url))
                html_cont=self.downloader.download(new_url)

                #print(html_cont)

                new_urls, resultlistM,resultlistS=self.parser.parse(new_url,html_cont,resultlistM,resultlistS)
                self.urls.add_new_urls(new_urls)
                #if count==100:
                #    break
                time.sleep(0.5)
                count=count+1

            except Exception as e:
                print(e)
                print('crawing failure')

        #self.output.output_html()
        self.output.collect_data(sheet1, resultlistM,name,num)
        self.output.collect_data(sheet2, resultlistS, name, num)




if __name__=="__main__":

    wb = xlwt.Workbook()
    wsmonth = wb.add_sheet('month')
    wsseason = wb.add_sheet('season')

    A2016=list(range(201612,201600,-1))#2016年12月到2001年1月(月份)
    A=A2016
    for year in range(1,16):
        A=A+[a-100*year for a in A2016]
    for gap in range(len(A)):
        wsmonth.write(0,gap+1,A[gap])


    for Ygap in range(16):    #季度
        for Sgap in range(4):
            if 16 - Ygap < 10:
                B = "0" + str(16 - Ygap)
            else:
                B = str(16 - Ygap)
            wsseason.write(0,Ygap*4+Sgap+1,"20" + B + "年第" + str(4 - Sgap) + "季度")



    keywords=xlrd.open_workbook('add_add_keywords.xlsx')#295words  40keywords
    sh = keywords.sheet_by_index(0)

    for num in range(114):
        name=sh.cell(num,0).value
        #root_url = "http://news.baidu.com/ns?cl=2&rn=20&tn=news&word=" + urllib.parse.quote(name)

        root_url = "https://www.baidu.com/s?wd=" + urllib.parse.quote(name)

        obj_spider = SpiderMain()
        number=num+1
        obj_spider.craw(wsmonth,wsseason, root_url,number,name)
        time.sleep(3)
        wb.save('add_add_new_result.xls')

