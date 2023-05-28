def solve():
    # Read the input values
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    # Store the counts of repeating elements in each array
    count_a = {}
    count_b = {}

    # Calculate the counts for array 'arr'
    count = 1
    for i in range(1, n + 1):
        if i == n:
            count_a[arr[i - 1]] = max(count, count_a.get(arr[i - 1], 0))
            break
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count_a[arr[i - 1]] = max(count, count_a.get(arr[i - 1], 0))
            count = 1

    # Calculate the counts for array 'brr'
    count = 1
    for i in range(1, n + 1):
        if i == n:
            count_b[brr[i - 1]] = max(count, count_b.get(brr[i - 1], 0))
            break
        if brr[i] == brr[i - 1]:
            count += 1
        else:
            count_b[brr[i - 1]] = max(count, count_b.get(brr[i - 1], 0))
            count = 1

    ans = 0

    # Find the maximum count of repeating elements from both arrays
    for e in arr:
        ans = max(ans, count_a.get(e, 0) + count_b.get(e, 0))
    for e in brr:
        ans = max(ans, count_b.get(e, 0) + count_a.get(e, 0))

    # Print the result
    print(ans)

num = int(input())

for i in range(num):
    solve()
