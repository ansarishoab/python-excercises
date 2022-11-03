class NTimesname:
    def __init__(self, n, name):
        self.n = n
        self.name = name

    def solution(self, count=0):
        if count > self.n:
            return
        print(self.name)
        count = count + 1
        self.solution(count)
    
    def reversePrint(self, count=1):
        if count> self.n:
            return
        print(self.n-count+1)
        count=count+1
        self.reversePrint(count)
    
    # 1 to N using backtrack
    def backtrackPrint(self, m):
        if m<1:
            return
        self.backtrackPrint(m-1)
        print(m)



ntimesname = NTimesname(5, "mohammed")
# ntimesname.solution() 
# ntimesname.reversePrint(1)
ntimesname.backtrackPrint(10)
