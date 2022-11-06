arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 8
x = 8


def functionName(ind, subs, sum):
    if sum == x:
        print(subs)
        return

    for i in range(ind, n):
        if i > ind and arr[i] == arr[i - 1]:
            continue
        if arr[i] + sum > x or len(subs)==2:
            break
        sum += arr[i]
        subs.append(arr[i])
        functionName(ind + 1, subs, sum)
        sum -= arr[i]
        subs.pop()


functionName(0, [], 0)
