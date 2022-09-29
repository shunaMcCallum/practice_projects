# def birthday(s, d, m):
#     r = range(m)
#     indexes = []
#     for number in r:
#         indexes.append(number)
#     num = 0
#     result = 0
#     i = 0
   
#     while i <= len(s) - 1:
#         num = 0
#         for index in indexes:
#             if index >= len(s):
#                 break
#             else:
#                 num += s[index]
#         if num == d:
#             result += 1
        
#         indexes = [index + 1 for index in indexes]
#         i += 1
            
#     return result

# print(birthday([1,2,1,3,2], 3, 2))

