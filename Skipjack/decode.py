from table import *


def skipjack_back(w1, w2, w3, w4):
    block = [w1, w2, w3, w4]
    alg_round_number = 33
    for i in range(2):

        for j in range(8):
            alg_round_number = alg_round_number - 1
            block = ruleB_back(block[0], block[1], block[2], block[3], alg_round_number)

        for j in range(8):
            alg_round_number = alg_round_number - 1
            block = ruleA_back(block[0], block[1], block[2], block[3], alg_round_number)

    return block


def ruleA_back(w1, w2, w3, w4, alg_round_number):
    old_w1 = permutationG_back(w2, alg_round_number)
    old_w2 = w3
    old_w3 = w4
    old_w4 = w1 ^ w2 ^ alg_round_number

    return [old_w1, old_w2, old_w3, old_w4]


def ruleB_back(w1, w2, w3, w4, alg_round_number):
    old_w1 = permutationG_back(w2, alg_round_number)
    old_w2 = permutationG_back(w2, alg_round_number) ^ w3 ^ alg_round_number
    old_w3 = w4
    old_w4 = w1

    return [old_w1, old_w2, old_w3, old_w4]


def permutationG_back(word, alg_round_number):
    for i in reversed(range(1, 5)):
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


def decode_skipjack(words):
    open_data = bytearray([])

    while len(words):
        open_block = skipjack_back(words[0], words[1], words[2], words[3])
        del words[0:4]

        for w in open_block:
            high_byte = (w & 65280) >> 8
            low_byte = w & 255
            open_data.append(high_byte)
            open_data.append(low_byte)

    return open_data
