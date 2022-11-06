#given a list of integer
#subsequence sum in ascending order
class RecursionExcercise:
    def functionName(self, ind, ans, sum):
        if ind == n:
            ans.append(sum)
            return
        sum+=arr[ind]
        self.functionName(ind+1, ans, sum)
        sum-=arr[ind]
        self.functionName(ind+1, ans, sum)
        return ans
            

arr = [3,1,4]
n = 3

recursionExcercise = RecursionExcercise()
ans1 = recursionExcercise.functionName(0, [], 0)
ans1.sort()
print(ans1)