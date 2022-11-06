# given an integer array, it may contain duplicates, return all possible subsets (the power set)
#solution must not containt duplicate subsets. return it in any order
import copy
class RecursionExcercise:
    def functionName(self, ind, subs, ans):
        ans.append(copy.deepcopy(subs))
        for i in range(ind, n):
            if i>ind and arr[i]==arr[i-1]:
                continue
            subs.append(arr[i])
            self.functionName(i+1, subs, ans)
            subs.pop()
arr = [1,2,2,2,3,3]
n = 6
ans = []
recursionExcercise = RecursionExcercise()
recursionExcercise.functionName(0, [], ans)
print(len(ans), ans)
