t = int(input())

while t:
    n = int(input())
    s = [int(x) for x in input().split(' ')]
    sum = 0
    for i in range(n - 1):
        sum += abs(s[i] - s[i + 1]) - 1
    print(sum)
    t -= 1