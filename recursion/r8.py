# get all the combination from array whose sum is 'X'
class RecursionExcercise:
    def functionName(self, ind, combiArr, target):
        if ind == n:
            if target == 0:
                print(combiArr)
            return
        if arr[ind] <= target:
            combiArr.append(arr[ind])
            self.functionName(ind, combiArr, target - arr[ind])
            combiArr.pop()
        self.functionName(ind + 1, combiArr, target)


arr = [1, 2, 3, 4]
n = 4
x = 7
recursionExcercise = RecursionExcercise()
recursionExcercise.functionName(0, [], x)
