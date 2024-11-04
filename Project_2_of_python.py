Bangla = float(input("Enter Your Marks Of Bangla, In Floating Number: "))
if Bangla>=1.0 and Bangla<=100.0: Bangla_ = Bangla
else:
    print("Your Given Marks Of Bangla Was Invalid, It Must Be Between 1 To 100")
    Bangla_ = float(input("Enter Your Marks Of Bangla Again In Floating Number: "))
    print(" ")

English = float(input("Enter Your Marks Of English, In Floating Number: "))
if English>=1.0 and English<=100.0: English_ = English
else:
    print("Your Given Marks Of English Was Invalid, It Must Be Between 1 To 100")
    English_ = float(input("Enter Your Marks Of English Again In Floating Number: "))
    print(" ")

Math = float(input("Enter Your Marks Of Math, In Floating Number: "))
if Math>=1.0 and Math<=100.0: Math_ = Math
else:
    print("Your Given Marks Of Math Was Invalid, It Must Be Between 1 To 100")
    Math_ = float(input("Enter Your Marks Of Math Again In Floating Number: "))
    print(" ")

Science = float(input("Enter Your Marks Of Science, In Floating Number: "))
if Science>=1.0 and Science<=100.0: Science_ = Science
else:
    print("Your Given Marks Of Science Was Invalid, It Must Be Between 1 To 100")
    Science_ = float(input("Enter Your Marks Of Science Again In Floating Number: "))
    print(" ")

The_Average = (Bangla_+English_+Math_+Science_)/4.0

print("The Average Of Your Results is: ",The_Average)

The_Average_int = int(The_Average)

if The_Average_int>90 and The_Average_int<=100:
    print("You've Got A+")
elif The_Average_int>80 and The_Average_int<=90:
    print("You've Got A")
elif The_Average_int>70 and The_Average_int<=80:
    print("You've Got B")
elif The_Average_int>60 and The_Average_int<=70:
    print("You've Got C")
elif The_Average_int>40 and The_Average_int<=60:
    print("You've Got D")
elif The_Average_int>=0 and The_Average_int<=40:
    print("You've Got F,,LoL!")
