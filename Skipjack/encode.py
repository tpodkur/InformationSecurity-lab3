from table import *


def skipjack(w1, w2, w3, w4):
    block = [w1, w2, w3, w4]
    alg_round_number = 0
    for i in range(2):

        for j in range(8):
            alg_round_number = alg_round_number + 1
            block = ruleA(block[0], block[1], block[2], block[3], alg_round_number)

        for j in range(8):
            alg_round_number = alg_round_number + 1
            block = ruleB(block[0], block[1], block[2], block[3], alg_round_number)

    return block


def ruleA(w1, w2, w3, w4, alg_round_number):
    new_w1 = permutationG(w1, alg_round_number) ^ w4 ^ alg_round_number
    new_w2 = permutationG(w1, alg_round_number)
    new_w3 = w2
    new_w4 = w3

    return [new_w1, new_w2, new_w3, new_w4]


def ruleB(w1, w2, w3, w4, alg_round_number):
    new_w1 = w4
    new_w2 = permutationG(w1, alg_round_number)
    new_w3 = w1 ^ w2 ^ alg_round_number
    new_w4 = w3

    return [new_w1, new_w2, new_w3, new_w4]


def permutationG(word, alg_round_number):
    for i in range(1, 5):
        if 0 != i % 2:
            byte1 = word & 255
            byte2 = (word & 65280) >> 8
        else:
            byte1 = (word & 65280) >> 8  # 1111 1111 0000 0000
            byte2 = word & 255  # 0000 0000 1111 1111

        key_index = (4 * alg_round_number + i) % 10

        res_byte = byte1 ^ key_bytes[key_index]
        replace_byte = replaceF(res_byte)

        new_byte = replace_byte ^ byte2

        if 0 != i % 2:
            low_byte = word & 255  # 0000 0000 1111 1111
            word = (new_byte << 8) | low_byte
        else:
            high_byte = word & 65280  # 1111 1111 0000 0000
            word = high_byte | new_byte

    return word


def encode_skipjack(data_bytes):
    data = bytearray(data_bytes)

    if 0 != len(data) % 8:
        for i in range(8 - len(data) % 8):
            data.append(0)

    words = []
    while len(data):
        word = (data[0] << 8) | data[1]
        del data[0:2]
        words.append(word)

    ciphertext = []
    while len(words):
        cipher_block = skipjack(words[0], words[1], words[2], words[3])
        del words[0:4]
        ciphertext = ciphertext + cipher_block

    return ciphertext
