from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs"
html_content = urlopen(url).read().decode("utf-8")
# f = open("song.html","wb")
# f.write(html_content)
# f.close()
soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section", "section chart-grid")
ul = section.div.ul
li = ul.find_all("li")
list_dictionary = []
for i in li:
    a = i.h3.a
    song = a.string
    a = i.h4.a
    sing = a.string
    # print (title + ' - ' + title2)
    dictionary = {
        "tên bài hát":song,
        "ca sĩ":sing
    }
    list_dictionary.append(dictionary)
    # print(list_dictionary)
pyexcel.save_as(records=list_dictionary,dest_file_name="song.xlsx")
