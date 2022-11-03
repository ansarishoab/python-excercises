# multiple recursion
# recursion on subsequences
# get all subsequences of array


class RecursionExcercise:
    def functionName(self, subs, ind=0):
        if ind == n:
            print(subs)
            return
        subs.append(arr[ind])
        self.functionName(subs, ind + 1)
        subs.pop()
        self.functionName(subs, ind + 1)

arr = [1, 2, 3, 4]
n = len(arr)
recursionExcercise = RecursionExcercise()
recursionExcercise.functionName([], 0)
