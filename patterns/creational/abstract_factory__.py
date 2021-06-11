import random

float_list = [1, 2, 3, 4]
for i in range(5):
    # seed the random number generator
    random.seed(4)
    # print random item
    print(random.choice(float_list))
