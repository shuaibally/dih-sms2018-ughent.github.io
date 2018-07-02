# This script generates a frequency list out of a text file.

import re

##################################
# Operation 0: clean Arabic ######
##################################

# deNoise(text) deletes short vowels from Arabic text
def deNoise(text):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return(text)

def normalizeArabicLight(text):
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("[يى]ء", "ئ", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("(ؤ)", "ء", text)
    text = re.sub("(ئ)", "ء", text)
    #text = re.sub("(ء)", "", text)
    #text = re.sub("(ة)", "ه", text)
    return(text)


# deNormalize(text) - deNormalizing Function (adds all possible variations of letters with RegEx)
def deNormalize(text):
    text = re.sub('[إأٱآا]', '[إأٱآا]', text)
    text = re.sub('(ي|ى)\\b', '[يى]', text) # HEAVY '[إأٱآايى]'
    #text = re.sub('ة', '[هة]', text)
    text = re.sub('(ؤ|ئ|ء)', '[ؤئءوي]', text)
    return(text)

##########################################
# Operation 1: Generating freq List ######
##########################################

def kwic(fileName, searchWord):

    lor = []

    with open(fileName, "r", encoding = "utf8") as f1:
        text = f1.read()

        text = deNoise(text)
        text = normalizeArabicLight(text)

        text = text.replace("\n", " ")
        text = re.sub(" +", " ", text)

        results = re.findall(r"(.{30})(%s)(.{30})" % deNormalize(searchWord), text)

        for r in results:
            val = (r[0]+"[["+r[1]+"]]"+r[2])
            lor.append(val)


    with open("%s.KWIC_Results" % fileName, "w", encoding="utf8") as f9:
        f9.write("\n".join(lor))

    print("="*80)
    print("Top 100 words are:")
    print("="*80)
    print("\n".join(lor[:100]))


kwic("../sample_texts/0726Yunini.DhaylMiratZaman.JK010379-ara1", "القاهرة")


    

        


