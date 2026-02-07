def move_zeros_to_end(n):
    ren = []
    
    for i in str(n):
        if i != "0":
            ren.append(int(i))

    for i in str(n):
        if i == "0":
            ren.append(int(i))

    for i in ren:
        print(i, end="")
        
nd = 1020304050

move_zeros_to_end(nd)

## 2nd method 

list = [0,3,8,0,3,7,9]

for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)

print(list)
        
