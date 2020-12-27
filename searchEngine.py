import os
import warnings
warnings.filterwarnings("ignore")

packageList=["nltk","pandas","spacy","gensim"]
for package in packageList:
    try:
        command_string = "pip install " + package
        os.system(command_string)
    except:
        count=1

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import gensim
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import spacy
spacyInstall="python -m spacy download en_core_web_sm"
os.system(spacyInstall)
EN = spacy.load('en_core_web_sm')

data = pd.read_csv('Data/data.csv')

w2v_model = gensim.models.word2vec.Word2Vec.load('Models/Pandas_word2vec_embeddings.bin')

def question_to_vec(question, embeddings, dim=300):
    question_embedding = np.zeros(dim)
    valid_words = 0
    for word in question.split(' '):
        if word in embeddings:
            valid_words += 1
            question_embedding += embeddings[word]
    if valid_words > 0:
        return question_embedding/valid_words
    else:
        return question_embedding


all_title_embeddings = []
for title in data.processed_title:
    all_title_embeddings.append(question_to_vec(title, w2v_model))
all_title_embeddings = np.array(all_title_embeddings)


def tokenize_text(text):
    tokens = EN.tokenizer(text)
    return [token.text.lower() for token in tokens if not token.is_space]

def to_lowercase(words):
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def remove_stopwords(words):
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def normalize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    return words

def tokenize_code(text):
    return RegexpTokenizer(r'\w+').tokenize(text)

def preprocess_text(text):
    return ' '.join(normalize(tokenize_text(text)))

MAX_SEQUENCE_LENGTH = 300

def showResults(userQuery):
    search_string = userQuery
    search_string = ' '.join(normalize(tokenize_text(search_string)))
    results_returned = "5"
    search_vect = np.array([question_to_vec(search_string, w2v_model)])  # Vectorize the user query
    cosine_similarities = pd.Series(cosine_similarity(search_vect, all_title_embeddings)[0])
    cosine_similarities = cosine_similarities *(1 + 0.2 * data.overall_scores_normalized)

    resultsDict={"Questions":[],"Votes":[],"Web URL":[],"S.I.":[]}

    for i, j in cosine_similarities.nlargest(int(results_returned)).iteritems():

        resultsDict["Questions"].append(data.original_title[i])
        resultsDict["Votes"].append(data.overall_scores[i])

        URL="<a href="+data.question_url[i]+">"+data.question_url[i]+"</a>"
        resultsDict["Web URL"].append(URL)
        resultsDict["S.I."].append(j)

    return resultsDict