import spacy

#lv nlp model
nlp = spacy.blank("lv")

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# NLP analīze
doc = nlp(text)

#stopvārdus, alfabētiski kartošana
words = sorted([token.text.lower() for token in doc if not token.is_stop and token.is_alpha])

print("Sakārtots vārdu saraksts:", words)