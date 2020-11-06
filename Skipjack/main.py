from encode import *
from decode import *

if __name__ == '__main__':

    in_file = open("file.txt", "rb")
    data = in_file.read()

    ciphertext = encode_skipjack(data)
    open_data = decode_skipjack(ciphertext)

    print(open_data)

    in_file.close()
