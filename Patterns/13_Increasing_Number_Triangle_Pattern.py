# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

N = int(input("Rows: "))
no = 1
for i in range(1, N+1):
    for j in range(1, i+1):
        print(no, end=" ")
        no += 1
    print()
