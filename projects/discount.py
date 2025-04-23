amount= float(input("enter your bill :"))
is_member=input("enter you are a member?(yes/no) :")
coupon=input("enter your code :")
discount=0
if is_member=="yes":
    if amount>100:
        discount=discount+20
    if coupon=="special":
        discount=discount+5
    else:
        discount=discount+10
if is_member=="no":
    if amount>200:
        discount=discount+10
    elif coupon=="special":
        discount=discount+5
    else:
        discount=discount+5
final_price=amount-amount*discount/100
print(f"you final price is :",final_price)
 