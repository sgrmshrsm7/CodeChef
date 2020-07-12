for t in range(int(input())):
        n = int(input())
        points = []
        for i in range(4 * n - 1):
                p = input().split(' ')
                points.append((int(p[0]), int(p[1])))
        x = {}
        y = {}
        for i in points:
                if i[0] not in x:
                        x[i[0]] = 1
                else:
                        x[i[0]] += 1
                if i[1] not in y:
                        y[i[1]] = 1
                else:
                        y[i[1]] += 1
        for i in x:
                if x[i] % 2 != 0:
                        print(i, end=' ')
        for i in y:
                if y[i] % 2 != 0:
                        print(i)