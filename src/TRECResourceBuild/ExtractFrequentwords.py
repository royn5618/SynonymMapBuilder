'''
Created on 15 Mar 2018

@author: Owner
'''
import numpy as np
import pandas as pd
import os
from pandas import ExcelWriter
from pandas import DataFrame
from nltk.probability import FreqDist
import nltk
from bs4 import BeautifulSoup
from rope.base.resources import Folder
root_path = "$/TRECResourceBuild/input_docs"
from nltk.tokenize import RegexpTokenizer

my_list = []
tokenizer = RegexpTokenizer(r'\w+')

TRECfiles = os.listdir(root_path)
for folders in TRECfiles:
    print(folders)
    
    if "fb" in folders:
        
        TRECfdocs = os.listdir(root_path + '/' + folders)
        for doc in TRECfdocs:
            print(doc)
            if "fb" in doc:
                file = open(root_path + '/' + folders + '/' + doc , "r")
                raw = file.readlines()
                raw = " ".join(raw)
                soup = BeautifulSoup(raw, "lxml")
                all_text = soup.text
                tokens = tokenizer.tokenize(all_text)
                freq = FreqDist(tokens)
                for each in freq.most_common(100):
                    my_list.append(each[0])
        print(my_list)
    if "ft" in folders:
        TRECfdocs = os.listdir(root_path + '/' + folders)
        
        for doc in TRECfdocs:
            print(doc)
            TRECfsubdocs = os.listdir(root_path + '/' + folders + '/' + doc)
            
            for subdoc in TRECfsubdocs:
                print(subdoc)
                if "ft" in file:
                    file = open(root_path + '/' + folders + '/' + doc + '/' + subdoc , "r")
                    raw = file.readlines()
                    raw = " ".join(raw)
                    soup = BeautifulSoup(raw, "lxml")
                    all_text = soup.text
                    tokens = tokenizer.tokenize(all_text)
                    freq = FreqDist(tokens)
                    for each in freq.most_common(100):
                        my_list.append(each[0])
    print(my_list)  
    if "la" in folders:
        TRECfdocs = os.listdir(root_path + '/' + folders)
        
        for doc in TRECfdocs:
            print(doc)
            if "la" in doc:
                file = open(root_path + '/' + folders + '/' + doc , "r")
                raw = file.readlines()
                raw = " ".join(raw)
                soup = BeautifulSoup(raw, "lxml")
                all_text = soup.text
                print(all_text)
                tokens = tokenizer.tokenize(all_text)
                freq = FreqDist(tokens)
                for each in freq.most_common(100):
                    my_list.append(each[0])
    print(my_list)
unique_set = set(my_list)          
print("Printing.......")
with open('topwords.txt', 'w') as f:
    print(unique_set, file=f)
