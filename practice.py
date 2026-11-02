

# 1. Print Prime Numbers Between Two Numbers
def prime_numbers():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    for num in range(start, end + 1):
        if num > 1:  # Prime numbers must be greater than 1
            for i in range(2, num):
                if num % i == 0:  # Check if divisible
                    break
            else:
                print(num, end=" ")  # Print prime number
    print()


# 2. Sort List Using sort()
def sort_list():
    a = [5, 2, 8, 1, 3]
    a.sort()  # Sort in ascending order
    print(a)


# 3. Sort List Without sort()
def sort_without_sort():
    a = [5, 2, 8, 1, 3]

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:  # Compare elements
                a[i], a[j] = a[j], a[i]  # Swap elements

    print(a)


# 4. Print Fibonacci Series
def fibonacci():
    a, b = 0, 1  # First two numbers

    for i in range(10):  # Print 10 numbers
        print(a, end=" ")
        a, b = b, a + b  # Calculate next numbers
    print()


# 5. Print List in Reverse
def reverse_list():
    a = [10, 20, 30, 40, 50]
    print(a[::-1])  # Reverse the list


# 6. Check Palindrome String
def palindrome():
    text = input("Enter a string: ")

    if text == text[::-1]:  # Compare with reversed string
        print("Palindrome")
    else:
        print("Not a palindrome")


# 7. Print Duplicate Elements in a List
def duplicates():
    a = [1, 2, 3, 2, 4, 3, 5]
    result = []

    for num in a:
        if a.count(num) > 1 and num not in result:
            result.append(num)  # Store duplicate once

    print(result)


# 8. Count Words in a Sentence
def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()  # Split into words
    print("Number of words:", len(words))


# 9. Search for an Element in a List
def search_element():
    arr = [10, 20, 30, 40, 50]
    x = int(input("Enter element to search: "))

    if x in arr:  # Check if element exists
        print("Element found")
    else:
        print("Element not found")


# 10. Binary Search (List must be sorted)
def binary_search():
    arr = [10, 20, 30, 40, 50]
    x = int(input("Enter element to search: "))

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index

        if arr[mid] == x:
            print("Element found")
            return
        elif arr[mid] < x:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    print("Element not found")


# 11. Plot a Simple Bar Chart
def bar_chart():
    import matplotlib.pyplot as plt  # Import plotting library

    names = ["A", "B", "C"]
    marks = [80, 70, 90]

    plt.bar(names, marks)  # Create bar chart
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Student Marks")
    plt.show()  # Display chart


# 12. Join Two Strings Using join()
def join_strings():
    a = "Hello"
    b = "Python"

    result = " ".join([a, b])  # Join using a space
    print(result)


# 13. Extract Digits from a String
def extract_digits():
    text = input("Enter a string: ")
    digits = ""

    for char in text:
        if char.isdigit():  # Check if character is a digit
            digits += char  # Add digit to result

    print(digits)


# 14. Split String Using Newline
def split_newline():
    text = "Hello\nPython\nWorld"
    result = text.split("\n")  # Split at each newline
    print(result)


# 15. Remove Repeated Characters from a String
def remove_duplicates():
    text = input("Enter a string: ")
    result = ""

    for char in text:
        if char not in result:  # Keep first occurrence
            result += char

    print(result)

#print 2 prime numbers between 2 nos
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")


#print duplicate elements in list
a = [1, 2, 3, 2, 4, 3, 5]
result = []
for num in a:
    if a.count(num) > 1 and num not in result:
        result.append(num)
print(result)

#search for element in array
arr = [10, 20, 30, 40, 50]
x = int(input("Enter element to search: "))

if x in arr:
    print("Element found")
else:
    print("Element not found")
choice = input("Enter your choice: ")

    if choice == "1":
        prime_numbers()
    elif choice == "2":
        sort_list()
    elif choice == "3":
        sort_without_sort()
    elif choice == "4":
        fibonacci()
    elif choice == "5":
        reverse_list()
    elif choice == "6":
        palindrome()
    elif choice == "7":
        duplicates()
    elif choice == "8":
        count_words()
    elif choice == "9":
        search_element()
    elif choice == "10":
        binary_search()
    elif choice == "11":
        bar_chart()
    elif choice == "12":
        join_strings()
    elif choice == "13":
        extract_digits()
    elif choice == "14":
        split_newline()
    elif choice == "15":
        remove_duplicates()
    elif choice == "0":
        print("Program ended")
        break
    else:
        print("Invalid choice. Try again.")

 #palindrome
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#prime number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#factorial
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial:", fact)

#palindrome
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#Fibonacci
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

#sum of digits
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("Sum of digits:", total)