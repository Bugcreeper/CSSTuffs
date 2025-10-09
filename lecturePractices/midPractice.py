import numpy as np
import re
'''
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a & set_b)

list_nums = [1, 2, 2, 3]
set_nums = {1, 2, 2, 3}
print(len(list_nums))
print(len(set_nums))

zeros = np.zeros(5)
print(zeros)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix[0, 2])

word = "PYTHON"
print(word.lower())
print(word[1:4])

sentence = "Hello World Python"
words = sentence.split()
print(len(words)) # Output: 3
print(words[2]) # Output: Python
print(",".join(words)) # Output: "Hello,World,Python"
'''

print(re.findall(r'\w+', "Hello World!")) # World!