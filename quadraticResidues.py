p = 29
x = 6

found = False
for a in range(1,p):
    if(a**2) % p == x:
        print(f"{a}^2 ≡ {x} mod {p}")
        found = True
        break
if not found:
     print(f"There is no such a where {a}^2 ≡ {x} mod {p}")