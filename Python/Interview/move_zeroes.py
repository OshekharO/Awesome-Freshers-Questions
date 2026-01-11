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
