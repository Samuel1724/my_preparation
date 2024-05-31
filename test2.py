# def lenofalternate(nums):
#     count = 1
#     prev = nums[0]
#     n = len(nums)
#     for i in range(1, n):
#         if nums[i] != prev:
#             count += 1

#             prev = nums[i]
#     return count


# x = [0,1,0,1,0,0]
# print(lenofalternate(x))

import bisect
def frog(X: list, Y: list, S:list) -> list:
    # X = Frog position
    # Y = Flies Position
    # S = Size of the Frog's Tongue

    result = []

    Y.sort()

    for i in range(len(X)):

        flies_eaten = 0

        start = X[i] - S[i]
        end = X[i] + S[i]

        left_index = bisect.bisect_left(Y, start)

        right_index = bisect.bisect_right(Y, end)

        flies_eaten += (right_index - left_index)

        result.append(flies_eaten)

    return result


x = [1,2,3]
y = [5,6,7]
s = [4,9,2]

print(frog(x, y, s))
