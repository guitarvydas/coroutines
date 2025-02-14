bookmark = {"A": None, "B": None}
next_routine = "A"

class A:
    def __init__(self):
        self.bookmark = bookmark
        bookmark["A"] = self.idle
        
    def idle(self):
        print("this is A idling")
        bookmark["A"] = self.running
        global next_routine
        next_routine = "B"
        
    def running(self):
        print("this is A running")
        bookmark["A"] = self.idle
        global next_routine
        next_routine = "B"

class B:
    def __init__(self):
        self.bookmark = bookmark
        bookmark["B"] = self.idle
        
    def idle(self):
        print("this is B idling")
        bookmark["B"] = self.running
        global next_routine
        next_routine = "A"
        
    def running(self):
        print("this is B running")
        bookmark["B"] = self.idle
        global next_routine
        next_routine = "A"

def coroutine_manager():
    A()
    B()
    i = 10
    while i > 0:
        try:
            coroutine = bookmark[next_routine]
            coroutine()
            i -= 1
        except Exception as error:
            print(f"Error: {error}")
            break

if __name__ == "__main__":
    coroutine_manager()
