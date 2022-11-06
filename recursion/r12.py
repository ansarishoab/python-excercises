#given an array of distinct integers, return all the possible permutations. You can retur answer in any order
import copy
class RecursionExcercise:
    def functionName(self,combi):
        if len(combi) == n:
            ans.append(copy.deepcopy(combi))
            return 
        for i in range(n):
            if arr[i] not in combi:
                combi.append(arr[i])
                self.functionName(combi)
                combi.pop()

arr = [1,2,3]
n = 3
ans = []
recursionExcercise = RecursionExcercise()
recursionExcercise.functionName([])
print(ans)