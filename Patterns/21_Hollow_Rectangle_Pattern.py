# *****
# *   *
# *   *
# *   *
# *****

N = int(input())

for i in range(N):
    if i == 0 or i == N-1:
        print("*"*N)
        continue
    space = " "*(N-2)
    print(space.center(N,"*"))
