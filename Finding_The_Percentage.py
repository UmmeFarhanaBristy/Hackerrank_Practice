if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    qu_scores = student_marks[query_name]
    avg = sum(qu_scores) / len(qu_scores)
    print("{0:.2f}".format(avg))