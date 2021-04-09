from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
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

df=pd.read_csv("test2.txt", engine='python',encoding='cp1252', sep= "|")

print(df)
data= pd.DataFrame(columns= ['Name', 'Raw count', 'Avg. weight','Viability Ceiling', 'Abilities', 'Items','Spreads', 'Moves','Teammates', 'Checks and Counters'])
file2= open("finaltest.txt", "w")
pattern="\\|(.+?)\\|"
noline="+----------------------------------------+"
with open("test2.txt") as fo:
    """for rec in fo:
        delResult=re.search(pattern,rec)
        dd=""
        if delResult:
            dd = delResult.group()
        file2.write(str(dd))
        file2.write("\n")
    file2.close()
fo.close()"""
    for rec in fo:
        if noline in rec:
            next(fo)
            delResult = re.search(pattern, rec)
            dd = ""
            if delResult:
                ddname = delResult.group(1)
        else:
            delResult = re.search(pattern, rec)
            dd = ""
            if delResult:
                dd = delResult.group(1)
                part_string=dd.partition(':')
                if "Raw count" in part_string[0]:
                    ddRaw=part_string[1]
                elif "Avg. weight" in part_string[0]:
                    ddAvg = part_string[1]
                elif "Viability Ceiling" in part_string[0]:
                    ddViab = part_string[1]
        delResult = re.search(pattern, rec)
        dd = ""
        if delResult:
            dd = delResult.group(1)
            if "Abilities" in dd:
                next(fo)
                delResult = re.search(pattern, rec)
                dd = ""
                if delResult:
                    dd = delResult.group(1)
                    ddAbi=dd


fo.close()
print("2nd file done")