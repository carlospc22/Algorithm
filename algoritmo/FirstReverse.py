def FirstReverse(strParam):
  lista=list(strParam)
  lista.reverse()
  strParam=''.join(lista)
  
 
  # code goes here
  return strParam

# keep this function call here 
print(FirstReverse(input()))