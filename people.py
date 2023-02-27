from main import People

try:
    name = input("Enter Name \n")
    phone = input("Enter Phone Number\n")
    email = input("Enter Email \n")
    county = input("Enter County \n")
    gender = input("Enter Gender \n")
    religion = input("Enter Religion \n")
    password = input("Enter Password \n")

    People.create(name=name, phone=phone, email=email, county=county, gender=gender, religion=religion,password=password)
    print("Confirmed Registration")

except:
    print("Please try again")
