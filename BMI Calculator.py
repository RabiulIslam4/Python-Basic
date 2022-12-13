print("Wellcome To BMI Calculator !")
height = float(input("Enter your Height in M :"))
weight  = float(input("Enter Your Weight in KG :"))

BMI = round(weight / height ** 2)
print(BMI)
if BMI < 18.5 :
  print("underweight")
elif BMI <= 25 :
  print("Normal Weight")
elif BMI <= 30 :
  print("Overweight")
elif BMI <= 35 :
  print("obese")
else :
  print("Clinically obese")  
