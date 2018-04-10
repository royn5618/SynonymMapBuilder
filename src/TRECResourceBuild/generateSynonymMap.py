'''
Created on 7 Apr 2018

@author: Nabanita
'''
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tag import StanfordNERTagger
from nltk.corpus import words
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

st = StanfordNERTagger('$/TopicModelling/stanford-ner-2018-02-27/classifiers/english.muc.7class.distsim.crf.ser.gz',
                       '$/stanford-ner-2018-02-27/stanford-ner.jar',
                       encoding='utf-8')

file_path = "$/TRECResourceBuild/src/TRECResourceBuild/topwords.txt"


token_list = []
final_list = []

#tokenise without punctuations
tokenizer = RegexpTokenizer(r'\w+')

file = open(file_path, "r")
lines = file.readlines()
tokens = tokenizer.tokenize(lines[0])

#for some document numbers appeared - To remove document numbers
for token in tokens:
    if "LA" not in token and "FR" not in token:
        token_list.append(token)
classified_text = st.tag(token_list)

#No synonym for people names - to filter persons using NER tagger
for text in classified_text:
    if 'PERSON' not in text[1]:
        final_list.append(text[0])
tagged_text = nltk.pos_tag(final_list)

#To filter numbers
legitimate_words = []
for text in tagged_text:
    if 'CD' not in text[1]:
        legitimate_words.append(text[0])

#remove alphabets from the collection
for eachword in legitimate_words.copy():
    if len(eachword) == 1:
        legitimate_words.remove(eachword)
#print(legitimate_words)
#Finally build the map using wordnet
string_builder = []
for word in legitimate_words:
    synsets = wn.synsets(word)
    synonyms = []
    for syn in synsets:
        for each in syn.lemma_names():
            synonyms.append(each)
    set_syns = set(synonyms)
    syn_string = ','.join(set_syns)
    string_builder.append(word + '=>' + syn_string + '\n')
#print(string_builder)

#Save to file
with open('synonyms_corrected.txt', 'w') as f:
    print(string_builder, file=f)
print("Done...")
