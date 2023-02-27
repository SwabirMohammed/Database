from main import People

mypeople = People.select()
for people in mypeople:
    print(people.name, people.phone, people.email, people.county, people.gender,
          people.religion, people.password)