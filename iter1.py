
'''

build-in function iter() which can make iterable object as iterator

'''

#iter(IterableObject)
ita = iter([1,2,3])
print(type(ita))
print(next(ita))
print(next(ita))
print(next(ita))

# Create iterator Object
class Container:
    def __init__(self,start = 0, end = 0):
        self.start = start
        self.end = end
    def __iter__(self):
        print("[LOG] I made this iterator!")
        return self
    def next(self):
        print("[LOG] Calling __next__ method!")
        if self.start < self.end:
            i = self.start
            self.start += 1
            return i
        else:
            raise StopIteration()

c = Container(1,5)

for i in c:
    print(i)

