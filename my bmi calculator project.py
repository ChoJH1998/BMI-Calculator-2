#bmi calculator
print("YOU ARE WELCOME TO BMI CALCULATOR BUILT BY IDRIS")
print("")
print("PLEASE KINDLY ENTER YOUR VALUE IN KG FOR WEIGHT AND IN METERS FOR HEIGHT, AND ENTER YOUR NAME")
print("")
n=str(input("Please enter your NAME = "))
print("")
w=float(input("please enter the value for weight in KG = "))
print("")
h=float(input("please enter the value for height in METERS = "))
bmi=w/(h*h)
answer=round(bmi,1)
print("")
if (answer<18.5):
    print(n, "You are UNDERWEIGHT BMI =", bmi)
    print("Please try to consume more and getting adequate rest is adviced to live healthier and vitamin supliments in little doses can be adviced be taken")
    print("KEY NOTE SEE THE DOCTOR FOR BETTER AND HEALTHIER SUGGESTIONS")
    print("")
elif ((answer>=18.5) and (answer<=25)):
    print(n, "You have a good body mass BMI =", bmi)
    print("You have a moderate equivalence between your height and weight")
elif ((answer>=25)and(answer<=30)):
    print(n, "You are OVERWEIGHT BMI =", bmi)
    print("Since you cannot change your height I would advice you to cut down on junks and unnecesary food to bring down your weight")
elif (answer>30):
    print(n, "You are Obese BMI =", bmi)
    print("You need to see the doctor fast! Make an appointment today")
    print("")
else:
    print("RE-TRY")
