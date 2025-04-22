total_bill = 0

coffee_price = 20

tea_price = 15

muffin_price = 25

sandwich_price = 45

coffee_quantity = input("Number of coffees: ")

tea_quantity = input("Number of teas': ")

muffin_quantity = input("Number of muffins: ")

sandwich_quantity = input("Number of sandwiches: ")

coffee_bill = int(coffee_quantity) * coffee_price

tea_bill = int(tea_quantity) * tea_price

muffin_bill = int(muffin_quantity) * muffin_price

sandwich_bill = int(sandwich_quantity) * sandwich_price

total_bill = coffee_bill + tea_bill + muffin_bill + sandwich_bill

print("----/your reciept/----")
print(f"cofee: Rs.{coffee_bill}/-")
print(f"tea: Rs.{tea_bill}/-")
print(f"muffins: Rs.{muffin_bill}/-")
<<<<<<< HEAD
print(f"sandwich: Rs.{sandwich_bill}")
print(f"Your Total Bill is: Rs. {total_bill}/-")
=======
print(f"sandwich: Rs.sandwich_bill}/-")
print(f"Your Total Bill is: Rs. {total_bill}/-")
>>>>>>> 3ad54a043bfab09b9dc08958b54d53e53de84e06
