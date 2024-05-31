# myList = [11,13,14,15]

# # myList = list(set(myList))
# myList.sort()
# print(myList)
# init = 1
# reps = 0
# # print(myList)
# for nums in myList:
#     if nums == init:
#         # print(nums)
#         init += 1
#         continue
#     else:
#         # while nums != init:
#             if nums < init:
#                 reps += init -  nums
#                 nums = init
#                 # nums += 1
#                 # reps += 1
#                 # print(reps,nums)
#             else:
#                 # print(nums,init)
#                 reps += nums - init 
#                 # print(reps)
#                 nums = init
#                 # print(reps,nums)
               
#                 # nums -= 1
#                 # reps += 1
#             myList[init-1] = nums
#             init += 1
        
# print(myList)
myList = [11, 13, 14, 15]

# myList = list(set(myList))  # Remove duplicates if any (not necessary here)
myList.sort()  # Ensure the list is sorted
print(myList)

init = 1
reps = 0

for i in range(len(myList)):
    nums = myList[i]
    if nums != init:
        reps += abs(nums - init)
        myList[i] = init
    init += 1

print("Transformed list:", myList)
print("Total steps required:", reps)
