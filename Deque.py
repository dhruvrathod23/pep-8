import collections
# Create a deque
DoubleEnded = collections.deque(["200","300","400"])
print (DoubleEnded)

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("400")
print (DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("100")
print (DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print (DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print (DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print (DoubleEnded)
