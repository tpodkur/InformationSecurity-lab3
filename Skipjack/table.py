row0 = [163, 215, 9, 131, 248, 72, 246, 244, 179, 33, 21, 120, 153, 177, 175, 249]
row1 = [231, 45, 77, 138, 206, 76, 202, 46, 82, 149, 217, 30, 78, 56, 68, 40]
row2 = [10, 223, 2, 160, 23, 241, 96, 104, 18, 183, 122, 195, 233, 250, 61, 83]
row3 = [150, 132, 107, 186, 242, 99, 154, 25, 124, 174, 229, 245, 247, 22, 106, 162]
row4 = [57, 182, 123, 15, 193, 147, 129, 27, 238, 180, 26, 234, 208, 145, 47, 184]
row5 = [85, 185, 218, 133, 63, 65, 191, 224, 90, 88, 128, 95, 102, 11, 216, 144]
row6 = [53, 213, 192, 167, 51, 6, 101, 105, 69, 0, 148, 86, 109, 152, 155, 118]
row7 = [151, 252, 178, 194, 176, 254, 219, 32, 225, 235, 214, 228, 221, 71, 74, 29]
row8 = [66, 237, 158, 110, 73, 60, 205, 67, 39, 210, 7, 212, 222, 199, 103, 24]
row9 = [137, 203, 48, 31, 141, 198, 143, 170, 200, 116, 220, 201, 93, 92, 49, 164]
rowA = [112, 136, 97, 44, 159, 13, 43, 135, 80, 130, 84, 100, 38, 125, 3, 64]
rowB = [52, 75, 28, 115, 209, 196, 253, 59, 204, 251, 127, 171, 230, 62, 91, 165]
rowC = [173, 4, 35, 156, 20, 81, 34, 240, 41, 121, 113, 126, 255, 140, 14, 226]
rowD = [12, 239, 188, 114, 117, 111, 55, 161, 236, 211, 142, 98, 139, 134, 16, 232]
rowE = [8, 119, 17, 190, 146, 79, 36, 197, 50, 54, 157, 207, 243, 166, 187, 172]
rowF = [94, 108, 169, 19, 87, 37, 181, 227, 189, 168, 58, 1, 5, 89, 42, 70]

tableF = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, rowA, rowB, rowC, rowD, rowE, rowF]

key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key_bytes = bytearray(key)

def replaceF(byte):

    older = (byte & 240) >> 4  # 1111 0000
    younger = byte & 15  # 0000 1111

    return tableF[older][younger]