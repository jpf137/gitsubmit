
# take two rand5: rand51, rand52

#      12345
#     111167
#     222267
#     333367
#     4444xx
#     5555xx

# if rand51<4:rand7=rand52
# if rand51==4:if rand52<4:rand7=6
# if rand51==5:if rand52<4:rand7=7

import random
import matplotlib.pyplot as mpl

storeme5=[]
storeme7=[]

for i in range(10000):
    rand51=random.randint(1,5)
    storeme5.append(rand51)
    rand52=random.randint(1,5)
    storeme5.append(rand52)
    if rand51<4:
        rand7=rand52
    if rand51==4:
        if rand52<4:rand7=6
    if rand51==5:
        if rand52<4:rand7=7
    storeme7.append(rand7)

mpl.hist(storeme5)
mpl.hist(storeme7)

mpl.show()
