import spacy


nlp = spacy.load("xx_ent_wiki_sm")

def varda_sakritibas_aprekins(teksts1, teksts2):
    doc1 = nlp(teksts1)
    doc2 = nlp(teksts2)

    vardi_teksts1 = set([token.text.lower() for token in doc1 if token.is_alpha])
    vardi_teksts2 = set([token.text.lower() for token in doc2 if token.is_alpha])

    kopīgi_vārdi = vardi_teksts1.intersection(vardi_teksts2)

    kopīgo_vārdu_skaits = len(kopīgi_vārdi)
    visi_vārdi = len(vardi_teksts1.union(vardi_teksts2))
    
    sakritibas_limenis = (kopīgo_vārdu_skaits / visi_vārdi) * 100
    return kopīgi_vārdi, sakritibas_limenis

teksts1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
teksts2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

kopigi_vardi, sakritibas_limenis = varda_sakritibas_aprekins(teksts1, teksts2)


print("Kopīgie vārdi:", kopigi_vārdi)
print(f"Sakritības līmenis: {sakritibas_limenis:.2f}%")
