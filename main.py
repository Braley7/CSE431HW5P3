import timeit
import random
import matplotlib.pyplot as plt
import collections

# Function to generate a random dataset of tuples of a given size with a uniform distribution
def uniform(size):
    return [(i, random.randint(1, 1000)) for i in range(size)]

hashTblTimeLst = []
bTreeTimeLst = []
for n in range(300):
    data = uniform(n)
    hashTblTime = timeit.timeit(stmt="for key, value in data: hashTbl[key] = value", setup="hashTbl = {}",
                                globals=locals(), number=1000)
    hashTblTimeLst.append(hashTblTime)

    bTreeTime = timeit.timeit(stmt="for key, value in data: bTree[key] = value",
                              setup="bTree = collections.OrderedDict()", globals=locals(), number=1000)
    bTreeTimeLst.append(bTreeTime)


plt.plot(hashTblTimeLst, label='Hash Table')
plt.plot(bTreeTimeLst, label='Binary Tree')
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Hash Table vs. Binary Tree")
plt.legend()
plt.show()
