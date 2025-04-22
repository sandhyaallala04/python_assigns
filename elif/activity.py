temp = int(input("Enter the temperature:"))
rain = input("Is it raining?(Yes/No)")
if temp>30:
    if rain=="yes":
         print("Stay indoors and watch a movie")
    else:        
         print("Go swimming")    
elif 20<=temp<=30:
    if rain=="yes":
        print("Visit a museum")
    else:
        print("Perfect for a picinic")
elif 10<=temp<=20:
    if rain=="yes":
        print("Indoor sports recommended")
    else:
        print("Go for a walk")
elif temp<=10:
    if rain=="yes":
        print("Stay home with hot chocolate")
    else:
        print("Ice skating would be fun!")