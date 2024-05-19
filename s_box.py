
def poly_div(term,modulo):

    while term.bit_length() >= modulo.bit_length():
        term ^= (modulo << term.bit_length() - modulo.bit_length()) #das funktioniert, weil bit_length führende Nullen nichtmehr mitzählt.
        #musste das aufschreiben, hat mich ewig gebraucht xD
    return term

def gf_multi(x,y,mod):

    result = 0
    while y != 0:
        if y & 1: #betrachte letztes Bit von y. Wenn dieses 1 ist, xor x auf result drauf
            result ^= x
        x = x << 1
        y >>= 1
        if x.bit_length() > 8:
            x = poly_div(x,mod)
    return result
def generate_i_sBox():

    inv_S_Box = {}
    for i in range (256):

        inv_S_Box[gf_multi(i, 0b10101011, 0b111000011)] = i
    return inv_S_Box

print(f"Das Element S^(-1)123 ist: {generate_i_sBox()[123]}")
