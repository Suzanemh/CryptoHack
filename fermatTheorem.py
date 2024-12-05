def modularExp(base, exp, mod):
    return pow(base, exp,mod)

base = int(input("Base: "))
exp = int(input("Exp: "))
mod = int(input("Mod: "))

result = modularExp(base,exp,mod)
print(f"Fermat little theorem gives the result: {result}")