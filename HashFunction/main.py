from encode import *

if __name__ == '__main__':

    in_file = open("file.txt", "rb")
    data = in_file.read()

    start_hash = [245, 9, 17, 86, 101, 153, 34, 0]
    result_hash = hashFoo(data, start_hash)

    print(result_hash)

    in_file.close()


