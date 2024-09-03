Stack1 = []
Stack2 = []
def enqueue(element):
    Stack1.append(element)
def dequeue():
    if not Stack2:
        if not Stack1:
            return 'Cannot dequeue because queue is empty'
        while Stack1:
            p = Stack1.pop()
            Stack2.append(p)
    return Stack2.pop()

enqueue('a')
enqueue('b')
enqueue('c')
print(dequeue())