ch="y"
while ch=="y":
    a=int(input("Enter your marks"))
    if (a>=90):
        print("Grade = A+")
    elif (a>=80):
        print("Grade = A")
    elif (a>=70):
        print("Grade = B")
    elif (a>=60):
        print("Grade = C")
    elif (a>=50):
        print("Grade = D")
    elif (a<50 and a>0):
        print("FAIL")
    else:
        print("Invalid Marks")
    ch=input("enter y for continue and n for exit")
    if (ch=="n"):
        print("Thankyou")

