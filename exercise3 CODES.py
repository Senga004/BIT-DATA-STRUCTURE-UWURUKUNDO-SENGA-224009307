
stack = []


stack.extend(["Dial", "PIN", "Confirm"])
print("MoMo stack:", stack)


stack.pop()
stack.pop()
print("After undo 2:", stack)


lectures = ["LectureA", "LectureB", "LectureC"]
for _ in range(len(lectures)):
    lectures.pop()
print("After popping all lectures:", lectures)


word = "QUEUEORDER"
stack = list(word)  
reversed_word = ""
while stack:
    reversed_word += stack.pop()
print("Reversed QUEUEORDER:", reversed_word)



from collections import deque


queue = deque(range(1, 11))
for _ in range(6):  
    queue.popleft()
print("Front citizen after 6 served:", queue[0])


queue = deque(range(1, 6))
print("Second in ATM queue:", queue[1])
