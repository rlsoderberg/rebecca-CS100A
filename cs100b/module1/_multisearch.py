#here, i'm putting all these searches in one program, right? today's weird thing?

#SEQUENTIAL SEARCH
#sequential search, you go through the whole haystack, one hay at a time

#here, i'm trying to do this without looking, let's see how it goes

def sequentialsearch(haystack, searchterm): #forgot arguments
    position = 0
    for i in haystack: #i think this is supposed to be (0, len(haystack)), not sure why yet
        if(i == searchterm): #forgot parentheses
            return i

    return -1  

searchterm = input("enter a number between 1 and 10: ")
haystack = [3,5,6,7,2,4,9]

position = sequentialsearch(haystack, searchterm)


if position == -1:
    print(f"{searchterm} is not in the haystack")
else:
    print(f"i found {searchterm} at position {position}.")
