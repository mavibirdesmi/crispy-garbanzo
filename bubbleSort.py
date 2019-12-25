import sys
def bubblesort (mylist):
    """Takes a list as an argument, then sorts it with bubblesort algoritm"""
    while True:
        count = 0
        for i in range(len(mylist)):
            try:
                mylist[i + 1]
            except:
                continue
            if mylist[i] > mylist[i + 1]:
                a, b = mylist[i + 1], mylist[i]
                mylist[i] = a
                mylist[i + 1] = b
                count += 1
        if count == 0:
            break
    print(mylist)
bubblesort(sys.argv[1])