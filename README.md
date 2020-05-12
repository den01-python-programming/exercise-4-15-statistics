# Exercise 4.15 Statistics

Create a class `Statistics` that has the following functionality (the file for the class is provided in the in the exercise template):

- a method `add_number` adds a new number to the statistics
- a method `get_count` tells the number of added numbers

The class does not need to store the added numbers anywhere, it is enough for it to remember their count. At this stage, the `add_number` method can even neglect the numbers being added to the statistics, since the only thing being stored is the count of numbers added.

The method's body is the following:

```python
class Statistics:

    def __init__(self):
        # initialize the variables count and sum here

    def add_number(self,number):
        # write code here

    def get_count(self):
        # write code here
```

The following program introduces the class' use:

```python
main():
    statistics = Statistics()
    statistics.add_number(3)
    statistics.add_number(5)
    statistics.add_number(1)
    statistics.add_number(2)
    print("Count: " + str(statistics.get_count()))
```

The program prints the following:

```plaintext
Count: 4
```

## Sum and average

Expand the class with the following functionality:

- the `sum` method tells the sum of the numbers added (the sum of an empty number statistics object is 0)
- the `average` method tells the average of the numbers added (the average of an empty number statistics object is 0

The class' template is the following:

```python
class Statistics:

    def __init__(self):
        # initialize the variables count and sum here

    def add_number(self,number):
        # write code here

    def get_count(self):
        # write code here

    def sum(self):
        # write code here

    def average(self):
        # write code here
```

The following program demonstrates the class' use:

```python
main():
    statistics = Statistics()
    statistics.add_number(3)
    statistics.add_number(5)
    statistics.add_number(1)
    statistics.add_number(2)
    print("Count: " + str(statistics.get_count())))
    print("Sum: " + str(statistics.sum))
    print("Average: " + str(statistics.average()))
```

The program prints the following:

```plaintext
Count: 4
Sum: 11
Average: 2.75
```

## Sum of user input

Write a program that asks the user for numbers until the user enters -1. The program will then provide the sum of the numbers.

The program should use a `Statistics` object to calculate the sum.

**NOTE:** Do not modify the Statistics class in this part. Instead, implement the program for calculating the sum by making use of it.

```plaintext
Enter numbers:
**4**
**2**
**5**
**4**
**-1**
Sum: 15
```

## Multiple sums

Change the previous program so that it also calculates the sum of even and odd numbers.

**NOTE**: Define _three_ Statistics objects in the program. Use the first to calculate the sum of all numbers, the second to calculate the sum of even numbers, and the third to calculate the sum of odd numbers.

**For the test to work, the objects must be created in the main program in the order they were mentioned above (i.e., first the object that sums all the numbers, then the one that sums the even ones, and then finally the one that sums the odd numbers)!**

**NOTE:** Do not change the Statistics class in any way!

The program should work as follows:

```plaintext
Enter numbers:
**4**
**2**
**5**
**2**
**-1**
Sum: 13
Sum of even numbers: 8
Sum of odd numbers: 5
```
