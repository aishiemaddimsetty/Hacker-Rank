class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def delete(self,data):
        self.stack.remove(data)

    def print(self):
        print(self.stack)

    def Maxele(self):
        print(max(self.stack))

array = Stack()
array.push(2)
array.push(4)
array.push(5)
array.print()

array.Maxele()


#Code that passed the challenge

n = int(input().strip())
stack = []
stackmax = [0]

for i in range(n):

    q = list(map(int, input().strip().split(' ')))

    if q[0] == 1:

        stack.append(q[1])
        if q[1] >= stackmax[-1]:
            stackmax.append(q[1])

    elif q[0] == 2:

        if stack.pop() == stackmax[-1]:
            stackmax.pop()

    else:
        print (stackmax[-1])