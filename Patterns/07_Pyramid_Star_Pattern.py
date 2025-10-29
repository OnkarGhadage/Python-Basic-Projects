#     *
#    ***
#   *****
#  *******
# *********

N = int(input("Size(lines to print the pyramid): "))


for i in range(1, N+1):
    print(" "*(N-i),end="")
    print('*'*(i*2-1))

for i in range(1, N+1):
    string = "*"*(i*2-1)
    print(string.center(N*2-1," "))
