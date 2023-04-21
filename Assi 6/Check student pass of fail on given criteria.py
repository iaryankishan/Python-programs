subject1=int(input("Enter marks of first subject\n"))
subject2=int(input("Enter marks of second subject\n"))
subject3=int(input("Enter marks of third subject\n"))

if(subject1<33 or subject2<33 or subject3<33):
    print("You are fail because you have less than 33% in one subject")
elif(subject1+subject2+subject3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congrats You pass this Exam")
