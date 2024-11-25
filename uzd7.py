import spacy
nlp = spacy.load("xx_ent_wiki_sm")

words = ["māja", "dzīvoklis", "jūra"]

def iegut_vektoru(vards):
    return nlp(vards).vector

vektori = {vards: iegut_vektoru(vards) for vards in words}

def salidzinat_lidzibu(vards1, vards2):
    return nlp(vards1).similarity(nlp(vards2))

similarities = {
    (vards1, vards2): salidzinat_lidzibu(vards1, vards2)
    for i, vards1 in enumerate(words)
    for vards2 in words[i+1:]
}

print("Vārdu vektori:")
for vards, vektors in vektori.items():
    print(f"{vards}: {vektors[:10]}...")  

print("\nVārdu līdzība:")
for pair, similarity in similarities.items():
    print(f"Līdzība starp '{pair[0]}' un '{pair[1]}': {similarity:.4f}")
