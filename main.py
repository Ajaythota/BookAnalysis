import os
import re
import nltk
from nltk.corpus import stopwords
path=os.getcwd()+"\\data\miracle_in_the_andes.txt"

# #Added encoding="utf8" to fix UnicodeDecodeError: 'charmap' codec can't decode byte X in position Y:
with open(path,"r",encoding="utf8") as files:
    book=files.read()
#
# #list put the chapters in the book
pattern=re.compile("Chapter [0-9]+")
cht=re.findall(pattern,book)
#print(cht)

#list put the chapter Titles in the book
pattern=re.compile("([a-zA-Z]+)\n\n")
title=re.findall(pattern,book)
#print(title)

#find the sentence which contains word "love"
pattern1=re.compile("[^.]* love [^.]*")
st=re.findall(pattern1,book)
#print(st)

#extract the paragraph which contains word "love"
pattern=re.compile("[^\n]+ love [^\n]+")
pg=re.findall(pattern1,book)
#print(pg)

#most words used in the book
pattern_2=re.compile("[a-zA-z]+")
findings=re.findall(pattern_2,book.lower())
d={}
for word in findings:
    if word in d.keys():
        d[word]=d[word]+1
    else:
        d[word]=1

#convert dict into list for sorting
list=[(value,key) for (key,value) in d.items()]


S_list=sorted(list, reverse=True)
#print(S_list[0][1])

#extract number of times the word is in  the book

#InputWord=input("Please enter the work to search: ")
#print(d[InputWord])

# "Remove english stop wars like 'the, is ,and etc."
# ran the following commands from python console
# import nltk
# nltk.download('stopwords')

eng_sw=stopwords.words("english")
#print(eng_sw)
nsw=[]
for value, word in S_list:
    if word not in eng_sw:
        nsw.append((value,word))
#print(nsw)

#Sentiment intensity analysis
# ran the following commands from python console
# import nltk
# nltk.download('vader_lexicon')

#Book sentiment
from  nltk.sentiment import SentimentIntensityAnalyzer
analyzer=SentimentIntensityAnalyzer()
#score=analyzer.polarity_scores("This is a great day for picnic and bad bad bad day for sleeping in")
score=analyzer.polarity_scores(book)
print(f"Book Sentiment{score}")

#chapter sentiment
pattern=re.compile("Chapter [0-9]+")
chapters=re.split(pattern,book)
chapters=chapters[1:]
#print(chapters[1:])
for chapter in chapters:
     scores=analyzer.polarity_scores(chapter)
     print(f"chapter sentiment for  {scores}")