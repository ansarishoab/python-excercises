# print subsequences sum are X
class RecursionExcercise:
    def functionName(self, ind, subs, sum):
        if ind == n:
            if sum == x:
                print(subs, "whose sumation is ", x)
            return
        subs.append(arr[ind])
        sum = sum + arr[ind]
        self.functionName(ind + 1, subs, sum)

        subs.pop()
        sum = sum - arr[ind]
        self.functionName(ind + 1, subs, sum)


# given data
arr = [1, 3, 2, 4, 6, 5, 9]
n = 7
x = 9
sum = 0
recursionExcercise = RecursionExcercise()
recursionExcercise.functionName(0, [], sum)


# print any one subsequence which sum is X
class RecursionExcercise2:
    def functionName(self, ind, subs, sum):
        if ind == n:
            # condition satisfied
            if sum == x:
                print(subs, "subsequence whose elements sum is equal to", x)
                return True
            # condition not satisfied
            else:
                return False
        subs.append(arr[ind])
        sum = sum + arr[ind]
        if self.functionName(ind + 1, subs, sum) == True:
            return True

        subs.pop()
        sum = sum - arr[ind]
        if self.functionName(ind + 1, subs, sum) == True:
            return True
        return False


# given data
arr = [1, 3, 2, 4, 6, 5, 9]
n = 7
x = 9
sum = 0
recursionExcercise2 = RecursionExcercise2()
recursionExcercise2.functionName(0, [], sum)


# print all subsequences count whose sum is equal to 'x'
class RecursionExcercise2:
    def functionName(self, ind, sum):
        if ind == n:
            if sum == 0:
                return 1
            else:
                return 0
        # One approach
        # l = self.functionName(ind+1, sum- arr[ind])

        # another approach optimised, as we are not looking further if arr[ind] is greater than rest sum

        l = self.functionName(ind + 1, sum - arr[ind])
        r = self.functionName(ind + 1, sum)

        return l + r


# given data
arr = [1, 3, 4, 7, -3]
n = 5
x = 4

recursionExcercise2 = RecursionExcercise2()
print("count is: ", recursionExcercise2.functionName(0, x))
