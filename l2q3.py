#Create a program that reads a sentence from the user and stores each word as an
#element of a list. Then count the frequency of each word using only lists.
sent=input("Enter a sentence: ")
words=sent.split()
unwords=[]
wordcount=[]
print("Words in the sentence:", words)
count=0
for word in words:
    if word in unwords:
        ind=unwords.index(word)
        wordcount[ind]+=1
    else:
        unwords.append(word)
        wordcount.append(1)

print(unwords,wordcount)