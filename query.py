from main import Person, session

result = session.query(Person).filter(Person.firstname == "Abbas")
for r in result:
    print(r)