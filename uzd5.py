from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

raksts = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. 
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

rezumēts_teksts = summarizer(raksts, max_length=50, min_length=30, do_sample=False)

print("Rezumēts raksts:")
print(rezumēts_teksts[0]['summary_text'])
