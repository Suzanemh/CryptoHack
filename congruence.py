def is_congruent(a,b,m):
    if a % m == b % m: 
        return True
    else: 
        return False
    
# some inputs from the user
a1 = 11
m1 = 6
x = a1 % m1 #gives the reminder

# some inputs from the user
a2 = 8146798528947 
m2 =17
y = a2 % m2 #gives the reminder

print(f"11 ≡ {x} (mod6)")
print(f"8146798528947≡ {y} (mod17)")

minValue = min(x,y)
print(f"the smallest value of the two integers x and y is {minValue}")


