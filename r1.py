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


ntimesname = NTimesname(5, "mohammed")
ntimesname.solution()
