import re
padrao = re.compile(r"\W+")

def LongestWord(sen):
  palavra=padrao.split(sen)
  # code goes here
  return max(palavra, key=len)

# keep this function call here 
print(LongestWord(input()))