#even_or_odd here is just the name of the entire function but (number) is the one that stores the data.
def even_or_odd(number):
    #as i said, (number) is the one that stores data, so we use (number) here and use (% or modular sign) to know whether the number is odd. so (% 2 == even) and (% 1 == odd) and the (0) just mean no remainder.
    if number % 2 == 0:
        #just to know whether its an even number
        return "Even"
    else:
        # just to know whether its an odd number
        return "Odd"
