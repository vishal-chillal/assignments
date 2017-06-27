# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
def histogram(lst):
    for bar_length in lst:
        print bar_length*"*"
histogram([4,9,2])
