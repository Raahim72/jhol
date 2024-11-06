with open('document.rtf', "w") as file:
  file.write('hi im penguin and im 1 year old')
file.close

with open('document.rtf', "w") as file:
    data = file.readline
    print("words in this file are......")
    for line in data:
     word=line.split()
    print(word)
    file.close()