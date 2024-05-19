from s_box import gf_multi

def hex_conv(s):

    bytes = []
    for i in range(0,len(s),2):
        bytes.append(int(s[i:i+2],16))
    return bytes

def multiply_matrix(matrix, block):

    output = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(block) //2):
            a = 0
            for k in range(len(matrix[i])): #len(matrix[i]) gibt mir die Länge der i-ten Zeile zurück. Das bedeutet in unserem Fall 2
                a ^= gf_multi(matrix[i][k],block[ j * 2 + k],0b111000011)
            row.append(hex(a))
        output.extend(row)
    return output

M = [
        [0x59, 0x4c],
        [0x4f, 0x4f]
    ]

print(f"0xa3caab05 nach MixColums{multiply_matrix(M,hex_conv("a3caab05"))}")