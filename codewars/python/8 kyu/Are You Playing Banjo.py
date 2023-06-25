def areYouPlayingBanjo(name):
    #used an [0] array to point out the first letter of the string, and use .lower() to turn the first letter into lower case and compare them if its equal to 'r' which is lower case.
    #saves alot of time to use lower() so i dont need to compare the uppercase of the first letter
    if name[0].lower() == 'r':
        #stop and return when condition is true
        return name + " plays banjo"
    #if the condition is false, return the one below
    else:
        return name + " does not play banjo"

