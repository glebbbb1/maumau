from textblob import TextBlob


def noskanjuma_analize(teikums):
    blob = TextBlob(teikums)
    polaritāte = blob.sentiment.polarity 

    
    if polaritāte > 0:
        return "Pozitīvs"
    elif polaritāte < 0:
        return "Negatīvs"
    else:
        return "Neitrāls"


teikumi = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]


for teikums in teikumi:
    noskanjums = noskanjuma_analize(teikums)
    print(f"Teikums: '{teikums}' \nNoskaņojums: {noskanjums}\n")
