# given collection of candidates number, find unique combination where candidates numbers sum to 'target'
# Each number in candidates may only used once in the combination
# it should not contain duplicate set
class RecursionExcercise:
    def functionName(self, ind, combi, target):
        if target == 0:
            print(combi)
            return
        for i in range(ind, n ):
            if i > ind and arr[i] == arr[i - 1]:
                continue
            if arr[i] > target:
                break
            combi.append(arr[i])
            self.functionName(i + 1, combi, target - arr[i])
            combi.pop()


arr = [1,1,1,2, 2]
n = 5
target = 4
# expected output [1,1,2] [2,2]
recursionExcercise = RecursionExcercise()
recursionExcercise.functionName(0, [], target)
