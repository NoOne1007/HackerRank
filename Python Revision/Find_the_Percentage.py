if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg = 0
    for i in student_marks[query_name]:
        avg = avg + i
    print(f"{avg/3:.2f}")