height =float(input("Enter height in meters :"))
weight =float(input("Enter weight in kilograms :"))

BMI=weight/(height**2)

if BMI<18.5:
    print("underweighted")

elif (BMI>18.5 and BMI <25):
    print("Healthy")

else :
    print("overweighted")