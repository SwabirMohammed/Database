from main import People

try:
    name = input("Enter Name")
    phone = input("Enter Phone Number")
    email = input("Enter Email")
    county = input("Enter County")
    gender = input("Enter Gender")
    religion = input("Enter Religion")
    password = input("Enter Password")

People.create(name=name, phone=phone, email=email, county=county, gender=gender, religion=religion,password=password)
print("Confirmed Registration")

except:
    print("Please try again")
