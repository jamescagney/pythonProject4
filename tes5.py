import numpy as np
import matplotlib.pyplot as plt
#build a 2 by 2 array with the values .8  .2  .9  .1
a = np.array([[.8, .2], [.9, .1]])
#build a 1 x 2 array with the values 150 150
b = np.array([[150.0], [150.0]])
print(a)
print("Humans",b[0][0])
print("Zombies",b[1][0])
human_list = [150]
zombie_list = [150]
for i in range(10):
    #muliply the two arrays
    c = np.multiply(a, b)
    print(c)
    b[0][0] = c[0][0]+c[1][1]
    b[1][0] = c[0][1]+c[1][0]
    print("Humans",b[0][0])
    print("Zombies",b[1][0])
    human_list.append(b[0][0])
    zombie_list.append(b[1][0])
plt.plot(zombie_list, label='Zombies')
plt.plot(human_list, label='Humans')
plt.legend()
plt.show()





