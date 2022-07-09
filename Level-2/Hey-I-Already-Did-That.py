""" Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep her minions on their toes. 
But you've noticed a flaw in the algorithm - it eventually loops back on itself, so that instead of assigning new minions as it iterates, 
it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. You think proving this to 
Commander Lambda will help you make a case for your next promotion.

You have worked out that the algorithm has the following process:

1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k. x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y. Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be 
n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. 
For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay 
in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 
7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, 
write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n. 
For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 
when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

"""

def to_base_ten(n, b): 
    """
    to_base_ten 

    This function takes the sorted ID numbers, and puts them into base 10 to be subtracted from each other. 

    Args:
        - n: The number which will be converted to base ten. 
        - b: The base that it is currently in. 

    Output:
        - The base ten equivalent of n. 
    """
    string_n = ''.join(n[::-1]) #create a string with the sorted list values backwards to help convert it to base 10

    b_10 = []   
    power = 0

    for x in string_n:
        b_10.append((b ** power * int(x))) #convert each number to its base ten equivalent
        power += 1 #increment the power 


    summation = sum(map(int, b_10[::1]))  #take the sum in-order to have the base ten equivalent

    return summation 

def to_anybase(n, b):
    """

    to_anybase 

    This function converts a number from base 10 to any base, 
    and will be used to convet z back to the original base

    Args:
        - n: The number which will be converted t a particular base.
        - b: The base that it will be converted to. 
    
    Output:
        - The number n, in base b. 
    """

    if n == 0:
        return n

    any_base = [ ]
    while n:
        n_int = int(n)
        remainder = n_int % b
        any_base.append(remainder)
        n = int(n) // b 

    #loop backwards through the values to form the number in the new base
    return ''.join(map(str, any_base[::-1])) 

id_list = [ ] #an empty list to store the minion ID's in 
end_cycle = [ ] #an empty list to store the value at the start of the ending cycle 

def solution(n, b):
    """
    solution 

    A function which returns the length of the ending cycle of the algorithm described by commander lambda. 

    Args:
        - n: The initial ID.
        - b: The base of the number. 

    Output:
        - len_cycle: The length of the ending cycle of the algorithm 
    
    
    """

    n = list(str(n)) #takes the first ID and makes it a list so its easier to deal with
    k = len(n)   
    y = sorted(n) #ascending order 
    x = sorted(n, reverse = True) #descending order

    z = to_base_ten(x, b) - to_base_ten(y, b) #set z to base x - y in base 10 



    z1 = to_anybase(z, b) #set the new value of z to its value in the original base
    z2 = list(str(z1)) #create a list version of z for easier manipulation

    if len(z2) != k:
        z1 = str(z1).zfill(k - len(z2)) #add leading zeros if z is smaller than k 

    if id_list.count(z1) == 0:
        id_list.append(z1)
        solution(z1, b)    #check if z is in the id_list, if it isnt then loop back through to create next ID
        
    elif id_list.count(z1) != 0:
        end_cycle.append(z1) #if z is already in the list then it is the start of the end cycle 

    if len(end_cycle) == 1:
        val = end_cycle[0]  #set the value at the start of the end cycle to be used as an index

    len_cycle = abs(len(id_list) - id_list.index(val)) #find the length of the end cycle by subtracting the start of the loop from the total length

    return len_cycle 