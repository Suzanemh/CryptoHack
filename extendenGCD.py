def extended_gcd(a, b):
    old_r, r = a, b  # Rest
    old_u, u = 1, 0  # Coeffisient for a
    old_v, v = 0, 1  # Coeffisient for b

    while r != 0:
        quotient = old_r // r
        # formula: new_v=old_v−quotient⋅v
        # formula: new_u=old_u−quotient⋅u

        old_r, r = r, old_r - quotient * r
        old_u, u = u, old_u - quotient * u
        old_v, v = v, old_v - quotient * v

    return old_r, old_u, old_v  # gcd, u, v

# Some values
p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)
print(f"gcd({p}, {q}) = {gcd}")
print(f"u = {u}, v = {v}")
print(f"Verifisering: {p} * {u} + {q} * {v} = {gcd}")
