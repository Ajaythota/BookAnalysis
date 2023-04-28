import glob
import os
import streamlit as st
import plotly.express as px
from  pathlib import Path

from  nltk.sentiment import SentimentIntensityAnalyzer
analyzer=SentimentIntensityAnalyzer()

#path=os.getcwd()+"\\dairy/*.txt"
#print(path)
myfiles=glob.glob("diary/*.txt")
#myfiles=glob.glob(path)
myfiles=sorted(myfiles)
print(myfiles)
positivity=[]
negativity=[]
fileName=[]

for file in myfiles:
    with open(file,'r') as file:
         book=file.read()
         scores=analyzer.polarity_scores(book)
         positivity.append(scores['pos'])
         negativity.append(scores['neg'])

fileName=[name.strip(".txt").strip("dairy\\") for name in myfiles]

print(f"positive sentiment {positivity}  & negative sentiment {negativity}")
print(fileName)

st.title("Dairy Tone")
st.subheader("Positivity")
pos_figure=px.line(x=fileName,y=positivity,labels={"x":"Date","y":"Postivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure=px.line(x=fileName,y=negativity,labels={"x":"Date","y":"Negativity"})
st.plotly_chart(neg_figure)