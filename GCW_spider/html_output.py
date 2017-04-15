import xlwt


class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self, sheet,resultlist,name,num):
        count=1
        sheet.write(num,0,name)
        for result in resultlist:
            sheet.write(num,count,result)
            count = count + 1
        #self.datas.append(data)


    def output_html(self):
        try:
            fout=open('output.html','w')
            fout.write("<html>")
            fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
            fout.write("<body>")
            fout.write("<table>")

            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % data['title'])
                fout.write("<td>%s</td>" % data['summary'])
                fout.write("</tr>")

            fout.write("</table>")
            fout.write("</body>")


            fout.write("<html>")

        except Exception as e:
            print(e)
            print("file open failure")

        finally:
            fout.close()