wt = float(input("Enter your weight(in Kg): "))
ht = float(input("Enter your hieght(in  m): "))
ht2 = ht*ht
bmi = wt/ht2
print("Your BMI is: ",bmi)
if(18.5 < bmi and bmi >= 24.9 ):
   print("You are in a healthy range")
if(bmi > 24.9):
   print("You are overweighed")
if(bmi < 18.5):
   print("You are below a healthy range")

