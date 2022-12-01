thisList = ['apple', 'banana','cherry']
for x in thisList:
  print(x)
  # to loop through list items use "for"

thisList = ['apple', 'banana','cherry']
for i in range(len(thisList)):
  print(thisList[i])

thisList = ['apple', 'banana','cherry']
i = 0
while i < len(thisList):
  print(thisList[i])
  i = i + 1

thisList = ['apple', 'banana','cherry']
[print(x) for x in thisList]
