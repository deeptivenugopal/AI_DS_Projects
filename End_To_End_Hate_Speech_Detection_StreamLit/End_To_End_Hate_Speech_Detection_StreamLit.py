from nltk.util import pr
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import re
import nltk

stemmer = nltk.SnowballStemmer("english")
#print(stemmer)

from nltk.corpus import stopwords
import string

stopword = set(stopwords.words('english'))
#print(stopword)


#Reading Data
data = pd.read_csv('twitter_all_data.csv')   # dummy_twitter_data.csv
#print(data.head())
#print(data.shape)

#Adding new column 'labels' with new values
data['labels'] = data['class'].map({0:"Hate Speech",1:"Offensive Language",2:"No Hate and Offensive"})

#print(data.head())

#Only Selecting 2 cols: twwets and labels for model building
data = data[["tweet","labels"]]
#print(data.head())

#Data Cleaning using  regexp

def clean(text):
    text = str(text).lower()
    #print(text)

    text = re.sub('\[.*?\]','',text)
    #print(text)

    text = re.sub('https?://\S+|www\.\S+','',text)
    #print(text)

    text = re.sub('<.*?>+','',text)
    #print(text)

    text = re.sub('[%s]' % re.escape(string.punctuation),'',text)
    #print(text)

    text = re.sub('\n','',text)
    #print(text)

    text = re.sub('\w*\d\w*','',text)
    #print(text)

    #checking if word in stopword
    text = [word for word in text.split(' ') if word not in stopword]
    #print(text)

    #After removing stopwords,join it to make a text
    text = ' '.join(text)
    #print(text)
                  
    return text

#print(clean(" got ya bitch tip toeing on my hardwood floors "" &#128514; http://t.co/cOU2WQ5L4q"))

#print("Regular Exp:",data.loc[:1,"tweet"].apply(clean))

data['tweet'] = data['tweet'].apply(clean)


# Split dataset and train model
x = np.array(data['tweet'])  # 1 dimension array
y = np.array(data['labels']) # 1 dimension array


cv = CountVectorizer()
X = cv.fit_transform(x)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)


#clf = DecisionTreeClassifier()
clf = RandomForestClassifier()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)

import streamlit as st
st.title("Hate Speech Detection")

#Testing the model on the UI
def hate_speech_detection():
    

    user_input = st.text_area("Enter any Tweet:")

    if len(user_input) <1:
        st.write(" ")
    else:
        sample = user_input
        data = cv.transform([sample]).toarray()
        res = clf.predict(data)
        st.title(res)


hate_speech_detection()





























    
