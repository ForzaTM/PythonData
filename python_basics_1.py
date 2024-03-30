# import of random module
import random

# create list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]


# create a sort function to sort list from min to max(without using sort())
def descendant_sort(lst):
    # sorting in descending
    # iterate through elements of the list lst
    for i in range(0, len(lst)):
        # iterate through next elements j of the list on position after i element
        for j in range(i + 1, len(lst)):
            # if i element equals or less than one of the next elements j
            if lst[i] <= lst[j]:
                # swap i element with j element in the provided list
                lst[i], lst[j] = lst[j], lst[i]
    # return modified list
    return lst


# use custom sort method to sort the list
descendant_sort(random_numbers)


# print the results of sorted list
print(random_numbers)


# create a variable for even numbers
even_numbers = [num for num in random_numbers if num % 2 == 0]
# create a variable for odd numbers
odd_numbers = [num for num in random_numbers if num % 2 != 0]

# create a variable for average value of even numbers
average_even = sum(even_numbers) / len(even_numbers)
# create a variable for average value of odd numbers
average_odd = sum(odd_numbers) / len(odd_numbers)

# print the average value of even numbers
print("Average of even numbers:", average_even)
# print the average value of odd numbers
print("Average of odd numbers:", average_odd)
