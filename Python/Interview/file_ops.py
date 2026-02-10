import random

with open("data.txt","a") as f:
    for i in range(100):
        rand = random.randint(1,100)
        f.write(rand + "\n")

with open("data.txt","a") as f:
    for i in range(100):
        f.write(str(i))

for i in range(100):
    with open("data.txt","a") as f:
        f.write(str(i))

names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]

with open("data.txt", "a") as file:
    for i in range(100):
        random_name = random.choice(names)
        file.write(random_name + "\n")
