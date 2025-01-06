def print_tables():
    for row in range(1,10):
        for col in range(1,10):
            if col<=row:
                result = row * col
                print("%d * %d = %d" % (col, row, result),end="     ")
        print("")


if __name__ == '__main__':
    print_tables()