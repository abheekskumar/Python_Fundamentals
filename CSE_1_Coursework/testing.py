# stringa = str()
# print(stringa)

# stringb = stringa + "d"
# stringb += stringa
# stringb += "d"
# print(stringb)

# x = {0: 2, 1: 1, 2: 0, 3: 0, 8: 0}
# s1 = "Hello World"
# l1 = s1.split()
# print(l1.reverse())

# def memo_fib(n,d= {1:1,2:1}):
#     """
#     Fibonacci number using memoization with a default dictionary
#     """
#     if n in d: # if it is in the dict
#         return d[n]
#     else: # if it isn't in the dict
#         ans = memo_fib(n-1,d) + memo_fib(n-2,d) # recursively calculate it
#         d[n] = ans # add to dict
#         return ans # return to above recursive call
    
# dict1 = {'a':2,'b':3,"c":0}

# for letter in dict1:
#     print(letter)
# for letter in dict1.keys():
#     print(letter)
# for letter in dict1.keys():
#     if dict1[letter]==0:
#         print(letter)
#         print(dict1[letter])
#         del dict1[letter] 
#         print(dict1)

# x = y =0
# print(x,y)



# # enumeration
# L = "Hello World!" 
# for idx,value in enumerate(L):
#     print(idx,value)

# # D = 
# # zip
# L1 = [element for element in range(0,11)]
# L2 = [element for element in range(11,22)]
# for v1, v2 in zip(L1,L2): # for both values
#     print(v1,v2)

# # for index along with elements from multiple lists:
# for idx, (v1,v2) in enumerate(zip(L1,L2)):
#     print(idx,v1,v2)

