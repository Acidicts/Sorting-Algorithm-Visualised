import random
import os

num = int(input("How many random numbers do you want to generate? "))
ran = int(input("What is the range of the random numbers? "))

while num > 1200:
    print("The maximum amount of numbers you can generate is 1200.")
    num = int(input("How many random numbers do you want to generate? "))

nums = []

new = num // 1
for i in range(int(new)):
    n = random.randint(0, int(ran))
    nums.append(n)

if os.path.exists("random_num.txt"):
    os.remove("random_num.txt")

with open("random_num.txt", "w") as file:
    for i in range(int(new)):
        file.writelines(str(nums[i])+"\n")
    file.close()
