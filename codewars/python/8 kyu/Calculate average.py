#(numbers) is the parameter
def find_average(numbers):
    #getting the length of the numbers using (len) and check if there is no number, if there is none then stop and return, return (0) as an average
    if len(numbers) == 0:
        return 0

    else:
        #The sum() function is used to calculate the sum of all the numbers in the numbers list, and the result is stored in the total variable.
        total = sum(numbers)
        #The average is then calculated by dividing the total by the length of the numbers list (len(numbers)), and the result is stored in the average variable.
        average = total / len(numbers)
        #return the average
        return average