from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd


def scrapping(annee, tier):
    # here we have to pass url and path
    # (where you want to save ur text file)
    url = f'https://www.smogon.com/stats/{annee}/moveset/{tier}.txt'
    print('Grabbing the page...')
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # first we do the CombinedScrapper
    file = open("scrapped.txt", "w")
    for data in soup:
        file.write(str(data))
    file.close()
    print("CombinedScrapper done")

    # second we add the CombinedScrapper page into a dataframe
    data = pd.DataFrame(
        columns=['Name', 'Raw count', 'Avg. weight', 'Viability Ceiling', 'Abilities', 'Items', 'Spreads', 'Moves',
                 'Teammates', 'Checks and Counters'])

    pattern = "\\|(.+?)\\|"
    noline = "+----------------------------------------+"
    with open("scrapped.txt", "r+") as fo:

        for rec in fo:
            ddRaw = ""
            ddAvg = ""
            ddViab = ""
            ddName = ""
            ddAbi = []
            ddIt = []
            ddSprd = []
            ddMov = []
            ddTeam = []
            ddCC = []
            dd = ""
            tmp = ""

            if rec.strip() == noline:
                continue
            delResult = re.search(pattern, rec)
            if delResult:
                ddName = delResult.group(1)
                ddName = ddName.split()[0]
                pass
            next(fo)
            tmp = next(fo)
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Raw count", dd):
                    ddRaw = dd.split(':')[1]
                    pass
            tmp = next(fo)
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Avg. weight", dd):
                    ddAvg = dd.split(':')[1]
                    pass
            tmp = next(fo)
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Viability Ceiling", dd):
                    ddViab = dd.split(':')[1]
                    pass
            tmp = next(fo)
            if tmp == noline:
                pass
            tmp = next(fo)
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Abilities", dd):
                    pass
                    while dd != noline:
                        dd = re.search(pattern, next(fo))
                        try:
                            dd = dd.group(1).strip()
                            ddAbi.append(dd)
                        except AttributeError:
                            tmp = next(fo)
                            break
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Items", dd):
                    pass
                    while dd != noline:
                        dd = re.search(pattern, next(fo))
                        try:
                            dd = dd.group(1).strip()
                            ddIt.append(dd)
                        except AttributeError:
                            tmp = next(fo)
                            break
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Spread", dd):
                    pass
                    while dd != noline:
                        dd = re.search(pattern, next(fo))
                        try:
                            dd = dd.group(1).strip()
                            ddSprd.append(dd)
                        except AttributeError:
                            tmp = next(fo)
                            break
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Moves", dd):
                    pass
                    while dd != noline:
                        dd = re.search(pattern, next(fo))
                        try:
                            dd = dd.group(1).strip()
                            ddMov.append(dd)
                        except AttributeError:
                            tmp = next(fo)
                            break
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Teammates", dd):
                    pass
                    while dd != noline:
                        dd = re.search(pattern, next(fo))
                        try:
                            dd = dd.group(1).strip()
                            ddTeam.append(dd)
                        except AttributeError:
                            tmp = next(fo)
                            break
            delResult = re.search(pattern, tmp)
            if delResult:
                dd = delResult.group(1)
                if re.search("Checks and Counters", dd):
                    pass
                    while dd != noline:
                        dd = re.search(pattern, next(fo))
                        try:
                            dd = dd.group(1).strip()
                            ddCC.append(dd)
                        except AttributeError:
                            break
            data = data.append(
                {'Name': ddName, 'Raw count': ddRaw, 'Avg. weight': ddAvg, 'Viability Ceiling': ddViab,
                 'Abilities': ddAbi,
                 'Items': ddIt, 'Spreads': ddSprd, 'Moves': ddMov, 'Teammates': ddTeam, 'Checks and Counters': ddCC},
                ignore_index=True)
    fo.close()
    data.to_csv(r'./export_poke.csv', index=False, header=True)
    #print(data)
    return data


def teammates(file, pokemon):
    dataTemp = pd.read_csv(file)
    finalList = []
    if pokemon.islower():
        return "Error : the first letter should be upper case"
    for i in dataTemp.loc[dataTemp['Name'] == pokemon, 'Teammates'].tolist():
        line = i.translate({ord(i): None for i in '[]'})
        list_tmp = list(line.split(","))
        for j in list_tmp:
            nameP = j.split()[0].replace("'", "")
            finalList.append(nameP)
    return finalList

