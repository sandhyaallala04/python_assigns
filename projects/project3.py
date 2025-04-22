total_trip_budget = 0
 
cost_per_litre = 100
mileage_per_litre = 35
total_distance = int(input("Total Distance: "))
 
total_trip_litres =  total_distance / mileage_per_litre
total_fuel_cost = total_trip_litres * cost_per_litre
 
hotel_cost_per_day = 1000
hotel_stay_days = int(input("Total Stay days: "))
total_hotel_bill = hotel_stay_days * hotel_cost_per_day
 
food_budget_per_day = int(input("Food budget per day : "))
total_eating_days = int(input("Number of eating days: "))
total_food_budget = total_eating_days * food_budget_per_day
 
total_activity_budget = int(input("Activities budget: "))
 
total_trip_budget = total_fuel_cost + total_hotel_bill + total_food_budget + total_activity_budget
 
print(f"Your total trip budget would be around: Rs. {total_trip_budget} /-")
