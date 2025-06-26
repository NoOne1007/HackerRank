if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    L = list(arr)
    winner = max(L)
    D = {}
    for i in L:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    del D[winner]
    print(max(D))