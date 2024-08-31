class Stack:

    def __init__(self):
        self.items = []
# Add an item to the top of the stack.

    def push(self, item):
        self.items.append(item)
# Remove and return the top item from the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

# Peek at the top item without removing it

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Check if the stack is empty.
    def is_empty(self):
        return len(self.items) == 0

# Return the number of items in the stack
    def size(self):
        return len(self.items)


# push "Add an item to the top of the stack."
# pop "Remove and return the top item from the stack."
my_stack = Stack()


while True:
    item = str(input("Enter item to stack(or q to exit):"))
    if item == 'E':
        break
    my_stack.push(item)

print(my_stack.pop())
print(my_stack.peek())
print(my_stack.size())
print(my_stack.is_empty())
