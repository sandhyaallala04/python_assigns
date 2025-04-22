basic_plan_name = "Basic"
basic_plan_cost = 29.99
basic_plan_includes_pool = False
basic_plan_includes_classes = False
basic_plan_guest_passes = 0
 
standard_plan_name = "Standard" 
standard_plan_cost = 49.99
standard_plan_includes_pool = True
standard_plan_includes_classes = False
standard_plan_guest_passes = 1
 
premium_plan_name = "Premium"
premium_plan_cost = 79.99
premium_plan_includes_pool = True
premium_plan_includes_classes = True
premium_plan_guest_passes = 3
 
# User information
customer_name = input("Enter your name: ")
customer_age = int(input("Enter your age: "))
customer_weight_kg = int(input("Enter your weight in kg: "))
customer_height_cm = float(input("Enter your height in cm: "))
 
# Expected usage
expected_visits = int(input("How many times do you plan to visit the gym per month? "))
wants_pool = input("Do you want to use the pool? (yes/no): ").lower() == "yes"
wants_classes = input("Do you want to attend fitness classes? (yes/no): ").lower() == "yes"
needs_guest_passes = int(input("How many guest passes will you need per month? "))
 
#cost per visit
basic_cost_per_visit= basic_plan_cost/expected_visits
standard_cost_per_visit= standard_plan_cost/expected_visits
premium_cost_per_visit= premium_plan_cost/expected_visits

body_mass_index= customer_weight_kg/customer_height_cm*customer_height_cm
basal_metabolic_rate= 10*customer_weight_kg+6.25*customer_height_cm-5*customer_age+5
 
print("basic_cost_per_visit:",basic_cost_per_visit)
print("standard_cost_per_visit:",standard_cost_per_visit)
print("premium_cost_per_visit:",premium_cost_per_visit)
print("body_mass_index:",body_mass_index)
print("basal_metabolic_rate:",basal_metabolic_rate)