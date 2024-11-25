from googletrans import Translator

def translate_text(texts, src_lang='lv', dest_lang='en'):
    translator = Translator()
    translated_texts = [translator.translate(text, src=src_lang, dest=dest_lang).text for text in texts]
    return translated_texts

latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translated_texts = translate_text(latvian_texts)

for text in translated_texts:
    print(text)
