import re

test = "here is a new here string string string!"

def wordCount(test):
  dic = {}
  test = re.sub(r'[^\w\s]','',test)
  test = test.lower().split()

  for word in test:
    if word in dic:
      dic[word] += 1
    else:
      dic[word] = 1

  for k, v in dic.items():
    print(k, v)

wordCount(test)
