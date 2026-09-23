from operator import index


def z_first_sort(words):
    zresult = []
    result = []
    for word in words:
        if word.lower()[0] == 'z':

            zresult.append(word)
        else:

            result.append(word)
            zresult.sort()
            result.sort()
    return zresult + result

words=["hello","good","nice","as","zealot","at","baseball","absorb","sword","silver","hi",
"pool","zoo","we","seven","do","you","watermelon","awake","zebra","xylophone","asparagus"]

print(z_first_sort(words))

digits = 1
unique = []
'''
while digits <= 5:
        digit_Input = int(input(f"Give me 5 unique digits this is you digit #{digits}: "))
        if digit_Input not in unique :
            unique.append(digit_Input)
            digits += 1
            print(unique)
        else :
            print("Not a unique number already in list")

print(unique)
'''
values = [1,2,3,4,5]
newvalues = values.copy()
for i in range(len(values)):
    newvalues[i] +=1
    print("Old value at index {} is : {}".format(i, values[i]))
    print("New value at index {} is : {} \n".format(i, newvalues[i]))