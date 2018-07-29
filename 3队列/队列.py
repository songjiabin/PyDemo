import collections

# 创建一个队列  先进先出的原则
queue = collections.deque()

queue.append("A")
queue.append("B")
queue.append("C")
print(queue)

print(queue.popleft())
print(queue)