# n = 5

# outer loop

# for i in range(1, n+1): # 1----(5) 6
#     # inner loop
#     for j in range(1, n+1): # 1----(5) 6
#         print("*", end=" ")
#     print()



# for i in range(1, n+1): # 1----(5) 6
#     # inner loop
#     for j in range(1, i+1): # 1----i
#         #  1----(3) 4
#         print("*", end=" ")
#     print() #nextline


# for i in range(1, n+1): # 1----(5) 6
#     # inner loop
#     for j in range(1, i+1): # 1----i
#         #  1----(3) 4
#         if((i+j) % 2 == 0):
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print() #nextline

# c = 1
# for i in range(1, n+1): # 1----(5) 6
#     # inner loop
#     for j in range(1, i+1): # 1----i
#         #  1----(3) 4
#         print(c, end=" ")
#         c+=1
#     print() #nextline


# for i in range(1, n+1): # 1----(5) 6
#     # inner loop
#     for j in range(1, i+1): # 1----i
#         #  1----(3) 4
#         print(j, end=" ")
#     print() #nextline




# for i in range(1, n+1): # 1----(5) 6
#     # inner loop
#     for j in range(1,(n-i+1)+1): # 1----i
#         #  1----(3) 4
#         print("*", end=" ")
#     print() #nextline


# for i in range(1, n+1): 
#     # space  - i - 1
#     for j in range(1, (i-1)+1):
#         print(" ", end=" ")
#     # star
#     for j in range(1,(n-i+1)+1):
#         print("*", end=" ")
#     print()

# n = 4
# m = 5

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print("*",end=" ")
#     print()

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         # boundary print krne ka logic
#         if(i == 1 or i == n or j == 1 or j == m):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# rohmbus
# n = 4 

# for i in range(1,n+1):
#     # space
#     for j in range(1, (n-i)+1):
#         print(" ",end=" ")

#     # star
#     for j in range(1, n+1):
#         if(i == 1 or i == n or j == 1 or j == n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 5

# for i in range(1,n+1):
#     # space
#     for j in range(1, (n-i)+1):
#         print(" ",end=" ")

#     for j in range(1, ((2 *i)-1)+1):
#         print("*",end=" ")

#     print()

# for i in range(n-1,0,-1):
#     # space
#     for j in range(1, (n-i)+1):
#         print(" ",end=" ")

#     for j in range(1, ((2 *i)-1)+1):
#         print("*",end=" ")

#     print()



n = 5

for i in range(1, n + 1):
    # star
    for j in range(1, i + 1):
        print("*",end=" ")
    # space
    for j in range(1, (2 * (n-i))+1):
        print(" ",end=" ")

    # star
    for j in range(1, i + 1):
        print("*",end=" ")
    print()

for i in range(n-1, 0,-1):
    # star
    for j in range(1, i + 1):
        print("*",end=" ")
    # space
    for j in range(1, (2 * (n-i))+1):
        print(" ",end=" ")

    # star
    for j in range(1, i + 1):
        print("*",end=" ")
    print()