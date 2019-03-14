from collections import Counter
import re

#test string
sen = "This this this this is is too funny too too ThIs"

def wordCount(sen):
  #remove non words from text
  #need to factor in numbers being inside text
  sen = re.sub(r'[^\w\s]','',sen)

  #make it lower and split into a list
  sen = sen.lower().split()

  #Coutner() is a dictionary
  foo = Counter(sen)

  #print frequency of words
  for k, v in foo.items():
    print(k, v)

wordCount(sen)
