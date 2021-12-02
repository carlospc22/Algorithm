def FindIntersection(strArr):
  set1 = set(strArr[0].split(", "))
  set2 = set(strArr[1].split(", "))
  lista=sorted(list(set1.intersection(set2)), key=lambda str: int(str))
  # code goes here
  return ",".join(lista) if len(lista)>0 else False

# keep this func.tion call here 
print(FindIntersection(input()))