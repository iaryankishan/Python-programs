letter='''Dear <|NAME|>
YOU ARE SELECTED!!

<|DATE|>'''
Name=input("Enter Your Name: ")
Date=input("Enter Date: ")
letter=letter.replace("<|NAME|>",Name)
letter=letter.replace("<|DATE|>",Date)
print(letter)
