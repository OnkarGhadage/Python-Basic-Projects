# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4

N = int(input())
size = N * 2 - 1
for i in range(size):
    for j in range(size):
        print(N - min(i,j,(size-i-1),(size-j-1)), end=" ")        
    print()
