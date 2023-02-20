# take input of integers list
num_list = list(map(int, input("Enter a list of integers: ").split()))

# sort the list
num_list.sort()

# take input of new number to add
new_num = int(input("Enter a new number to add to the list: "))

# find the position to add the new number
for i in range(len(num_list)):
    if new_num < num_list[i]:
        position = i
        break
else:
    position = len(num_list)

# add the new number to the list
num_list.insert(position, new_num)

# print the sorted list with the new number added
print(num_list)

class LifoQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.queue.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)
# create a LIFO queue
my_queue = LifoQueue()

# push some items onto the queue
my_queue.push(10)
my_queue.push(20)
my_queue.push(30)

# print the queue
print(my_queue)  # output: [10, 20, 30]

# pop an item off the queue
item = my_queue.pop()
print(item)  # output: 30

# print the queue again
print(my_queue)  # output: [10, 20]


