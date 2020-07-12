def power(a):
        sum = 0
        for i in a:
                sum += int(i)
        return sum

for t in range(int(input())):
        w1 = 0
        w2 = 0
        for n in range(int(input())):
                c = input().split(' ')
                if power(c[0]) > power(c[1]):
                        w1 += 1
                elif power(c[0]) < power(c[1]):
                        w2 += 1
                else:
                        w1 += 1
                        w2 += 1
        if w1 > w2:
                print('0 ' + str(w1))
        elif w2 > w1:
                print('1 ' + str(w2))
        else:
                print('2 ' + str(w1))