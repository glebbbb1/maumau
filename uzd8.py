import spacy

nlp = spacy.load("xx_ent_wiki_sm")

teksts = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

doc = nlp(teksts)

personvardi = []
organizacijas = []

for ent in doc.ents:
    if ent.label_ == "PER":
        personvardi.append(ent.text)
    elif ent.label_ == "ORG":
        organizacijas.append(ent.text)

print("Personvārdi:", personvardi)
print("Organizācijas:", organizacijas)
