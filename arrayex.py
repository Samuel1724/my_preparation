# exp = [2200, 2350, 2600, 2130, 2190]
# print(exp)
# print(f'In feb I have spent {exp[1] - exp[0]} Dollars.')
# print(f'The first quarter expense is {exp[0]+exp[1]+exp[2]}')
# print(f'Did I ever spent 2000 Dollars in this year? {2000 in exp}')
# exp.append(1090)
# print(exp)
# exp[3] = exp[3] - 200
# print(f'I april month I returned a product and I got 200$ refund x{exp}')

# heros=['spider man','thor','hulk','iron man','captain america']

# print(len(heros))
# heros.insert(3, 'Black Panther')
# print(heros)
# heros[1:3] = ['Doctor Strange']
# print(heros)
# heros.sort()
# print(heros)

max = int(input('Enter the size of List: '))

odd_nums = [i for i in range(max) if i % 2 != 0]
print(odd_nums)