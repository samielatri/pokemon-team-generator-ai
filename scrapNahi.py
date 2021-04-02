from bs4 import BeautifulSoup
import urllib.request
import re
# here we have to pass url and path
# (where you want to save ur text file)
url = 'https://www.smogon.com/stats/2021-02/moveset/gen8uu-0.txt'
print('Grabbing the page...')
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')


file = open("test2.txt", "w")
print("start for")
for data in soup:
    file.write(str(data))
file.close()
print("1st file done")
print("end for")

file2= open("finaltest.txt", "w")
pattern="\\|(.+?)\\|"
noline="+----------------------------------------+"
with open("test2.txt") as fo:
    for rec in fo:
        delResult=re.search(pattern,rec)
        dd=""
        if delResult:
            dd = delResult.group(1)
        file2.write(str(dd))
        file2.write("\n")
    file2.close()
fo.close()
"""for rec in fo:
        if noline not in rec:
            delResult = re.search(pattern, rec)
            dd = ""
            if delResult:
                dd = delResult.group(1)
                file2.write(str(dd))
                file2.write("\n")
    file2.close()
fo.close()"""
print("2nd file done")