from ast import Param


class ParameterizeExcercise:
    def sumOfN(self, n, sum=0):
        if n<1:
            print(sum)
            return
        self.sumOfN(n-1, n+sum)

parameterizeExcercise = ParameterizeExcercise()
parameterizeExcercise.sumOfN(5) 

class FunctionalWay:
    def sumOfN(self, n):
        if n==0:
            return 0
        return n+ self.sumOfN(n-1)
    def factorialOfN(self, n):
        if n==0:
            return 1
        return n * self.factorialOfN(n-1)

functionalWay = FunctionalWay()
print(functionalWay.sumOfN(5))
print(functionalWay.factorialOfN(5))