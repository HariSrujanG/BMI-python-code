def bmi(ht,wt):
    bmi = wt/pow(ht,2)
    return bmi

def main():
    a=float(input("Enter Hieght in meters: "))
    b=float(input("Enter Weight in Kgs: "))
    n = bmi(a,b)
    print(n)
    if(18.5 < n and n >= 24.9 ):
       print("You are in a healthy range")
    if(n > 24.9):
        print("You are overweighed")
    if(n < 18.5):
        print("You are underweighted")
        
main()

