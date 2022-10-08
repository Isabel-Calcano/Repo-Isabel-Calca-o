lista= ([313, 6786, 5151], [1, 4, 10], [41, 53, 86, 56, 12],
[84, 4], [], [35, 4, 1, 2],
[1, 4], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9],
[100, 84, 4781], [], [53, 56, 1, 4, 45],
[84, 88, 407], [153, 25], [10, 35, 9474],)

a = 1
result= int((a * (a + 1) * (a + 2)) / 6)
for grupo in lista:
    for i in grupo:
        i= int(i)
        print(i)

        while i > result:
            result= int((a * (a + 1) * (a + 2)) / 6)
            print(result)
            result=str(result)
            i= str(i)
            if result == i:
                print("{} es piramidal triangular".format(i))
            else:
                result=int(result)
                i= int(i)
                pass
            a += 1
