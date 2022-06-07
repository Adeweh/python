for i in range(1, 13):
    for j in range(1, 13):
        print("{:>4} * {:>2} = {:>3}".format(i, j, i * j))
        if j == 12:
            print()


