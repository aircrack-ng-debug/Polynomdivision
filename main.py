
def gf_mult(a, b, mod_poly):
    result = 0
    while b > 0:
        if b & 1: #prüft ob b ungerade, mit niederwertigstes bit.
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= mod_poly
        b >>= 1
    return result

def gf_inv(a, mod_poly):
    t0, t1 = 0, 1
    r0, r1 = mod_poly, a
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 ^ gf_mult(q, r1, mod_poly)
        t0, t1 = t1, t0 ^ gf_mult(q, t1, mod_poly)
    return t0

element_123 = 0x7B

element_ab = 0xAB

mod_poly = 0xC3

product = gf_mult(element_123, element_ab, mod_poly)

inverse_element = gf_inv(product, mod_poly)

print(f"Das Inverse von {hex(element_123)} multipliziert mit {hex(element_ab)} ist: {hex(inverse_element)}")
