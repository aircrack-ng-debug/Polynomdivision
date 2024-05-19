def gf_mult(a, b, poly):
    """Multiplies two numbers in GF(2^8) with a given modulus polynomial."""
    p = 0
    while b:
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= poly
        b >>= 1
    return p


def gf_inverse(a, poly):
    """Finds the multiplicative inverse of a in GF(2^8) with a given modulus polynomial."""
    if a == 0:
        return 0

    lm, hm = 1, 0
    low, high = a, poly

    while low > 1:
        ratio = high // low
        nm, new = hm ^ gf_mult(lm, ratio, poly), high ^ gf_mult(low, ratio, poly)
        lm, low, hm, high = nm, new, lm, low

    return lm


def generate_s_box(multiplier, poly):
    """Generates the S-Box using the given multiplier and modulus polynomial."""
    s_box = []
    for i in range(256):
        s_box.append(gf_mult(i, multiplier, poly))
    return s_box


def generate_inverse_s_box(s_box):
    """Generates the inverse S-Box."""
    inverse_s_box = [0] * 256
    for i in range(256):
        inverse_s_box[s_box[i]] = i
    return inverse_s_box


# Given parameters
multiplier = 0xab
modulus_poly = 0x11b  # This represents x^8 + x^7 + x^6 + x + 1

# Step 1: Generate the S-Box
s_box = generate_s_box(multiplier, modulus_poly)

# Step 2: Generate the inverse S-Box
inverse_s_box = generate_inverse_s_box(s_box)

# Step 3: Find the 123rd element of the inverse S-Box
element_123 = inverse_s_box[123]
print(int(element_123))
print(f"The inverse S-Box element at position 123 is: {element_123:02x}")
