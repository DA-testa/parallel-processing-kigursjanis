def parallel_processing(n, m, data):
    start = [0] * n  
    answer = []
    
    for i in range(m):
        time = start[0]
        thread = 0

        for j in range(1, n):
            if time > start[j]:
                time = start[j]
                thread = j
        answer.append((thread, start[thread])) 
        start[thread] = start[thread] + data[i]

    return answer


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
