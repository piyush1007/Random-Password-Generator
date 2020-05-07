import random
wordlst=[]
special_char=['@','#','&','^']
data=open("wiki.txt","r")
for line in data:
    word=line.split()
    

    for items in word:
        if len(items)>5:
            wordlst.append(items.capitalize())
wording=random.choice(wordlst)
schar=random.choice(special_char)
num=str(random.randint(10,99))
passw=wording+schar+num
print("The generated password is : ",passw)            