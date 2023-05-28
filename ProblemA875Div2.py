num = int(input())
for i in range(num):
    n = int(input())
    A = list(map(int, input().split()))
    # Construct permutation B 
    B = [n + 1 - A[i] for i in range(n)]
    print(' '.join(map(str, B)))
