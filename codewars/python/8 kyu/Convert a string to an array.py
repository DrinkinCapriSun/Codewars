def string_to_array(s):
    #if the str is empty just return ('')
    if s == "":
        return ['']
    else:
        #s.split is used cuz i need to split each word from the string
        array = s.split()
        return array
