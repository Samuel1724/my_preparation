# def findoccurance(num):
    
#     return num.count(19) == 2 and num.count(5)>=3
    


# num = [19, 19, 5, 5, 5, 5, 5]
# occ = findoccurance(num)

# print(occ)


# def calclength(nums):
#     return len(nums) == 8 and nums.count(nums[4]) >= 3
    
    

# nums = [19, 15, 11, 7, 5, 6, 2]
# check = calclength(nums)
# print(check)


# def palindrome(num):
#     # result = 0
#     # dup = num
#     # while num > 0:
#     #     digit = num % 10
#     #     num = int(num / 10)

#     #     result = result * 10 + digit
#     #     print(result)
#     #     return result
        
#     # if result == dup:
#     #     return True
    
#     # return False
    
# palindrome(123)


# def armstrongNumber (n):
#     # code here 
#     p_num = 0
#     n_str = str(n)
#     for i in n_str:
#         i_int = int(i)
#         # print(i_int)
#         # c_num =  c_num + (i_int * i_int * i_int)                         #i_int ** len(n_str)
#         # p_num = p_num * 1+ c_num
#         p_num = p_num + (i_int * i_int * i_int)
#         # print(p_num)
    
#     if n == p_num:
#         print('Yes')
#     else:
#         print('No')

# armstrongNumber(152)

# import math

# def sum_of_divisors(n):
#     ans = []
#     for i in range(1, int(math.sqrt(n))):
#         if (n % i == 0):
#             ans.append(i)
#             if ((n/i) != i):
#                 ans.append(int(n/i))
#     return sum(ans)
            
# N = 4
# print("Sum of divisors from 1 to", N, "is:", sum_of_divisors(N))  # Output: 28

# n = int(input("Enter the number: "))

# for i in range(3, int(n**0.5)+1, 2):
#     print(i)
#     if (n%i)==0:
#         print("Not a prime number")


# class Recursion:
#     def __init__(self):
#         self.count = 0

#     def test(self,n):
#         if self.count == n:
#             return
#         print(self.count,'\n')
#         self.count+=1
#         self.test(n)


# t = Recursion()
# t.test(10)


# def sumOfSeries(n):
#         #code here
        
#         if n == 0:
#             return 0
#         # sumOfSeries(n)
#         print((n * (n + 1) // 2 )** 2)

# sumOfSeries(5)

# def twosum(nums, target):
    
#     numMap = {}
#     n = len(nums)
#     print(range(n - 1))
#     for i in range(n):
#         complement = target - nums[i]
#         if complement in numMap:
#             return [numMap[complement], i]
#         numMap[nums[i]] = i

#     return [] 


# n = [2,7,11,15]
# target = 9

# ans = twosum(n, target)
# print(ans)

# def dupornot(nums):
#     n = len(nums)
#     for i in range(n - 1):
#         print(nums[i],'Im from i')
#         for j in range(i +1, n):
#             print(nums[j])
#             if nums[i] == nums[j]:
#                 print(nums[i], "i am form if" , nums[j])
#                 return True
#     return False



# n = [1,2,3,1]
# dupornot(n)

# def product_except_self(nums):
#     n = len(nums)
    
#     # Initialize the prefix and suffix product arrays
#     prefix_products = [1] * n
#     suffix_products = [1] * n
#     answer = [1] * n
    
#     # Fill the prefix products array
#     for i in range(1, n):
#         prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
#         print(prefix_products, 'Im from prefix')
    
#     # Fill the suffix products array
#     for i in range(n - 2, -1, -1):
#         suffix_products[i] = suffix_products[i + 1] * nums[i + 1]
        
#         print(suffix_products, 'Iam from suffix')
    
#     # Combine the prefix and suffix products to get the final answer
#     for i in range(n):
#         answer[i] = prefix_products[i] * suffix_products[i]
    
#     return answer

# # Example usage:
# nums = [1, 2, 3, 4]
# print(product_except_self(nums))  # Output: [24, 12, 8, 6]

# x = input("Enter your Name here: ")
# print(f'Hello {x}')

# x = int(input('Enter your salary here: '))

# if x > 10000:
#     x += 2000
#     print(f'Your salary with bonus is: {x}')
# else:
#     x += 1000
#     print(f'Your salary with bonus is: {x}')


# import math
# x = int(input("Enter the number here: "))
# if x <= 1:
#     print(f"{x} is neither prime nor composite.")
# c = 2

# while c*c <= x:
#     if x % c == 0:
#         print(f'The given number {x} is not a prime number.')
#         break
#     c += 1
# else:
#     print(f'The given number {x} is a prime number.')