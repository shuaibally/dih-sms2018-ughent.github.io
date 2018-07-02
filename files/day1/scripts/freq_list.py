# This script generates a frequency list out of a text file.

import re

def freqList(fileName):

    fDictionary = {}

    with open(fileName, "r", encoding = "utf8") as f1:
        text = f1.read()

        for r in re.findall(r"\b\w+\b", text):
            if r in fDictionary:
                fDictionary[r] += 1
            else:
                fDictionary[r]  = 1

    fList = []

    for k,v in fDictionary.items():
        fList.append("%09d\t%s" % (v,k))

    fList = sorted(fList, reverse=True)

    with open("%s.freqList" % fileName, "w", encoding="utf8") as f9:
        f9.write("\n".join(fList))

    print("="*80)
    print("Top 10 words are:")
    print("="*80)
    print("\n".join(fList[:10]))


freqList("0726Yunini.DhaylMiratZaman.JK010379-ara1")


    

        


