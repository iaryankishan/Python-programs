Dict = {
    "Khana" : "Food",
    "Paani" : "Water",
    "Ghar" : "House",
    "Paisa" : "Money"
}
print("Choose from ", Dict.keys())
a= input("Enter the Hindi word\n")
print("Meaning of the word is: ",Dict.get(a))
