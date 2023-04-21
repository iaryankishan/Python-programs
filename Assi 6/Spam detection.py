Text=input("Enter the text\n")
if("make a lot of money" in Text):
    spam=True
elif("buy Now" in Text):
    spam=True
elif("click this" in Text):
    spam=True
elif("suscribe this" in Text):
    spam=True
else:
    spam=False

if(spam):
 print("This text is spam")
else:
 print("This text is not spam")
