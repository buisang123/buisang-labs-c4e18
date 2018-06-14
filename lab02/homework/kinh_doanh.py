from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
import re

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read().decode("utf-8")
# f = open("kinh_te.html","wb")
# f.write(html_content)
# f.close
soup = BeautifulSoup(html_content,"html.parser")
div = soup.find("div",style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
table = div.table
tr = table.find_all("tr", {"class": ["r_item", "r_item_a"]})
list_so_lieu =[]
for i in tr:
    # print (i)
    # print ("===================")
    td = i.find_all("td", class_="b_r_c")
    data = {
        "danh mục":td[0].string
        "quý4":td[1].string,
        "quý 1-2017":td[2].string,
        "quý 2-2017":td[3].string,
        "quý 3-2017":td[4].string
    }
    print (data)
    list_so_lieu.append(data)
pyexcel.save_as(records=list_so_lieu,dest_file_name="kinh doanh.xlsx")
#     list_so_liệu.append(data)
# pyexcel.save_as(records=list_so_liệu,dest_file_name="kinh doanh.xlsx")

    


        

