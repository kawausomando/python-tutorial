from collections import deque

queue = deque(["Bill", "Earl", "Sam"])
queue.append("Andy")
queue.append("Chris")
print(queue.popleft())
# Bill
print(queue.popleft())
# Earl
print(queue)
# deque(['Sam', 'Andy', 'Chris'])