#multiple recursion call
#fibonacci series
class RecursionExcercise:
    def functionName(self, n):
        if n<=1:
            return n
        last = self.functionName(n-1)
        secondLast = self.functionName(n-2)
        return last + secondLast


recursionExcercise = RecursionExcercise()
result = recursionExcercise.functionName(10)
print(result)