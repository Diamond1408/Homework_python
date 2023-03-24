import re
 
s = input('введите слово: ')
d = {'[AEIOULNSTR]': '1', '[DG]': '2', '[BCMP]': '3', '[FHVWY]': '4', 'K': '5', '[JX]': '8', '[QZ]': '10', '[АВЕИНОРСТ]': '1', '[ДКЛМПУ]': '2', '[БГЁЬЯ]': '3', '[ЖЗХЦЧ]': '5', '[ШЭЮ]': '8', '[ФЩЪ]': '10'}
for k in d:
    s = re.sub(k, d[k], s)
print(sum(map(int, s)))

# import re
 
# s = input()
# d = {'[AEIOULNSTR]': '1', '[DG]': '2', '[BCMP]': '3', '[FHVWY]': '4', 'K': '5', '[JX]': '8', '[QZ]': '19'}
# for k in d:
#     s = re.sub(k, d[k], s)
# print(sum(map(int, s)))