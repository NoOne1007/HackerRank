if __name__ == '__main__':
    students = []
    scorelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scorelist.append(score)
        students.append([name, score])
        
    sec_low = sorted(set(scorelist))[1]

    for n, s in sorted(students):
        if s == sec_low:
            print(n)
    
    # L = []
    # for n, s in students:
    #     if s == sec_low:
    #         L.append(n)
        
    # L.sort()
    # for i in L:
    #     print(i)