#assignment 1

person={
    "name": "john",
    "age": 30,
    "is_married": True,
}
print(person)

person_age=person["age"]
print(person_age)

b=person.get("age")
print(b)

all_keys=person.keys()
print(all_keys)

all_values=person.values()
print(all_values)