#Tumasis, Bleuzette Albrielle Felenash M. - 9 HELIUM

#Code Number 1
print("Code Number 1")
#print('A. If name is “Joseph The Dreamer” and nChar is 5, the output would be "Josep". This is because the function loops through the indices \nfrom 0 to 4 and in"each iteration, print(name[i]) prints the character at the index on a new line\n')
#print('B. Using the same name and nChar is 20, the output would be "Joseph The Dreamer" followed by "IndexError: string index out of range" because \nthe string "Joseph The Dreamer" only has 18 characters and the loop attempts to run 20 times, looking for indices from \n0 to 19. When the loop reaches '
      #'index 18, it shows an IndexError because that index does not exist in the string\n')
#print("C. To fix this error, we need to make sure that the loop does not exceed the actual length \nof the string, we can try using min() function to limit the range to either nChar or the length of the string\n")

  #Modified Code
def greet_students(name, nChar):
    for i in range(min(nChar, len(name))):
        print(name[i])

name = input("Enter your name: ")
nChar = int(input("Enter any numeric number: "))
nChar = int(nChar)
greet_students(name, nChar)


#Code Number 2
    #Modified Code
print("\nCode Number 2")
def greet_students(name, nChar):
    for i in range(nChar):
        print(name[0 : nChar - i])

name = input("Enter your name: ")
greet_students(name, len(name))

#print("A. The syntax error is that there is a missing input prompt quotes closing string. To fix this, I added a "
      #"closing quotation mark at the end of the input prompt string")

#Code Number 3
    #Modified Code
print("\nCode Number 3")
def sum_of_squared(max_val):
    total = 0
    for i in range(1, max_val + 1):
        total += i ** 2
    return total

n = 0
while n < 1 or n > 100:
    n = int(input("Enter a number between 1 and 100: "))

print("Sum of all squared numbers is:", sum_of_squared(n))
