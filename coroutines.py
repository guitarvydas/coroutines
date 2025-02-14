class A:
    def __init__(self):
        self.A1 = lambda: self._A1()
        self.A2 = lambda: self._A2()
    
    def _A1(self):
        print("A 1")
        return self.A2
    
    def _A2(self):
        print("A  2")
        return self.A1

class B:
    def __init__(self):
        self.B1 = lambda: self._B1()
        self.B2 = lambda: self._B2()
    
    def _B1(self):
        print("B 1")
        return self.B2
    
    def _B2(self):
        print("B  2")
        return self.B1

def dispatcher():
    continuations = []
    continuations.append(A().A1)
    continuations.append(B().B1)
    i = 10
    while i > 0:
        # circular queue - pull ready continuation from front of queue
        f = continuations.pop(0)  # equivalent to JavaScript's shift()
        # resume continuation, when it yields, it returns the next continuation
        cont = f()
        # push resulting next continuation onto back of queue
        continuations.append(cont)
        i -= 1

dispatcher()
