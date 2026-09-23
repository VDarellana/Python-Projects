def helloworld():
    print("Hello World")

def hello_world_n_times(n):
    for i in range(n):
        helloworld()
def main():
    hello_world_n_times(2)
    hello_world_n_times(1)
    hello_world_n_times(3)
    hello_world_n_times(2)
main()

def factorial(n):
    result = n
    for i in range(n-1,0,-1):
        result = result * (i)
    return result

print(factorial(5))

def countVowels(word):
    numVowels = 0
    for letter in word.lower():
        if letter in "aeiou":
            numVowels += 1
    return numVowels

print(countVowels("AEIOu"))