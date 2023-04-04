# Original Code That needs Debuging :




# import os
# import random
# from collections import Counter, defaultdict
# from datetime import datetime
# def create_file():
#     """Create a new file with a random filename and some random contents."""
#     filename = f'file_{datetime.now().strftime("%Y%m%d%H%M%S%f")}.txt'
#     with open(filename, 'w') as f:
#         for i in range(10):
#             f.write(f'Line {i}: {random.randint(1, 100)}\n')
#     return filename
# def read_file(filename):
#     """Read the contents of a file and return as a string."""
#     with open(filename, 'r') as f:
#         return f.read()
# def count_numbers(text):
#     lines = text.splitlines()
#     counts = defaultdict(int)
#     for line in lines:
#         words = line.split()
#         for word in words:
#             if word.isdigit():
#                 counts[int(word)] += 1
#     return Counter(counts)
# if __name__ == '__main__':
#     filename = create_file()
#     text = read_file(filename)
#     counts = count_numbers(text)
#     print(f'Counts for file {filename}: {counts}')
#     os.remove(filename)
#     print(f'Total count: {sum(counts)}')






# The Fixed Version :




import os
import random
from collections import Counter, defaultdict
from datetime import datetime
def create_file():
    """Create a new file with a random filename and some random contents."""
    filename = f'file_{datetime.now().strftime("%Y%m%d%H%M%S%f")}.txt'
    with open(filename, 'w') as f:
        for i in range(10):
            f.write(f'Line {i}: {random.randint(1, 100)}\n')
    return filename
def read_file(filename):
    """Read the contents of a file and return as a string."""
    with open(filename, 'r') as f:
        return f.read()
def count_numbers(text):
    lines = text.splitlines()
    counts = defaultdict(int)
    for line in lines:
        words = line.split()
        for word in words:
            if word.isdigit():
                counts[int(word)] += 1
    return Counter(counts)
if __name__ == '__main__':
    filename = create_file()
    text = read_file(filename)
    counts = count_numbers(text)
    print(f'Counts for file {filename}: {counts}')
    os.remove(filename)
    print(f'Total count: {sum(counts)}')





