import url_manager,html_downloader,html_parser,html_output
import xlwt
import xlrd
import urllib
for realdata in range(201601,201613):
    index = int((realdata - 200100) / 100) * 12 + ((realdata - 200100) % 100)
    index = 16 * 12 - index + 1

    index2 = int((realdata - 200100) / 100) * 4 + int(int(((realdata - 200100) % 100) - 1) / 3)
    index2 = 16 * 4 - index2
    print(realdata)
    print(index,index2)