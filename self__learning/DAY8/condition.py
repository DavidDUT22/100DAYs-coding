#if condition and else condition

age = int(input("please input your age: "))

if age >= 18:
    print("you are sign up now")
elif age<0 :
    print("your age is invalid")
else: 
    print("your age is unable to sign up now")


#reponse yes or no

response = input("would you like some food(Y/N): ")
if response == "Y" or "y": 
  print("have some food!")

elif response =="N" or "n": 
    print("GO back home please") 