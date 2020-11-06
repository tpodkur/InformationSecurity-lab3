def littleendian(b0, b1, b2, b3):  # b3 - старший
    res = (b3 << 8) | b2
    res = (res << 8) | b1
    res = (res << 8) | b0

    return res


def littleendian_back(b):
    b0 = b & 255  # 11111111
    b1 = (b & 65280) >> 8  # 11111111 00000000
    b2 = (b & 16711680) >> 16  # 11111111 00000000 00000000
    b3 = (b & 4278190080) >> 24  # 11111111 00000000 00000000 00000000

    return [b0, b1, b2, b3]


def quarterround(y0, y1, y2, y3):
    z1 = y1 ^ ((y0 | y3) << 7)
    z2 = y1 ^ ((y1 | y0) << 9)
    z3 = y1 ^ ((y2 | y1) << 13)
    z0 = y1 ^ ((y3 | y2) << 18)

    return [z0, z1, z2, z3]


def rowround(y):  # y - массив из 16 элементов (матрица 4х4)
    row0123 = quarterround(y[0], y[1], y[2], y[3])
    row3012 = quarterround(y[5], y[6], y[7], y[4])
    row2301 = quarterround(y[10], y[11], y[8], y[9])
    row1230 = quarterround(y[15], y[12], y[13], y[14])

    return [
        row0123[0], row0123[1], row0123[2], row0123[3],
        row3012[3], row3012[0], row3012[1], row3012[2],
        row2301[2], row2301[3], row2301[0], row2301[1],
        row1230[1], row1230[2], row1230[3], row1230[0]
    ]


def columnround(y):  # y - массив из 16 элементов (матрица 4х4)
    column1 = quarterround(y[0], y[4], y[8], y[12])
    column2 = quarterround(y[5], y[9], y[13], y[1])
    column3 = quarterround(y[10], y[14], y[2], y[6])
    column4 = quarterround(y[15], y[3], y[7], y[11])

    return [
        column1[0], column2[3], column3[2], column4[1],
        column1[1], column2[0], column3[3], column4[2],
        column1[2], column2[1], column3[0], column4[3],
        column1[3], column2[2], column3[1], column4[0]
    ]


def doubleround(y):  # y - массив из 16 элементов (матрица 4х4)
    return rowround(columnround(y))


def salsa20(x):
    i = 1
    z = doubleround(x)
    while i < 10:
        z = doubleround(z)
        i = i + 1

    sum_array = []
    i = 0
    while i < 16:
        sum_array.append(x[i] | z[i])
        i = i + 1

    resulting_sequence = []
    for i in sum_array:
        cod = littleendian_back(i)
        resulting_sequence = resulting_sequence + cod

    return resulting_sequence


def encode_salsa20(x):
    a = bytearray(x.encode('UTF-8'))

    if 0 != len(a) % 64:
        for i in range(64 - len(a) % 64):
            a.append(0)

    x = []
    while len(a):
        word = littleendian(a[0], a[1], a[2], a[3])
        del a[0:4]
        x.append(word)

    return salsa20(x)


if __name__ == '__main__':
    y = input()
    coded_sequence = encode_salsa20(y)

    for i in range(0, len(coded_sequence), 4):
        print(coded_sequence[i], coded_sequence[i+1], coded_sequence[i+2], coded_sequence[i+3], )

