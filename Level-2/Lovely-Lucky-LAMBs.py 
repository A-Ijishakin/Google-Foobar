""" Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs 
(Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their 
bunks, or even a third daily meal!

However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - 
or else the henchmen will revolt and you'll all get demoted back to minions again! 

There are 4 key rules which you must follow in order to avoid a revolt: 
1. The most junior henchman (with the least seniority) gets exactly 1 LAMB. (There will always be at least 1 henchman on a team.) 
2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do. 
3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get. 
(Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them. The 2nd most junior henchman 
would require at least as many LAMBs as the most junior henchman.) 
4. You can always find more henchmen to pay - the Commander has plenty of employees. If there are enough LAMBs left over such that 
another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive 
integer number of LAMBs.

Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. 
It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs 
(that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the 
above rules to avoid a revolt. For instance, if you had 10 LAMBs and were as generous as possible, 
you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, 
you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts: you can expect total_lambs to always 
be between 10 and 1 billion (10 ^ 9).
""" 

def myLog(x, b):
    """
    myLog

    A function which computes the log of a number, with a particular base. 

    Args:
        - x: The number who's log will be computed 
        - b: The base which the log is computed with respect to. 

    Output:
        - The log base b of x. 
    
    """
    if x < b:
        return 0  

    return 1 + myLog(x/b, b) 


def fibonacciVal(n, fibonacci_c):
    """
    
    fibonacciVal 

    A function which calculates the fibonacci number at index n.

    Args:
        - n: The index of the fibonacci number which should be computed.
        - fibonacci_c: A dictionary which is used to store fibonacci numbers. 

    Output:
        - value: The fibonacci number at index n. 

    """
    if n in fibonacci_c:
        return fibonacci_c[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2: 
        value = fibonacciVal(n - 1) + fibonacciVal(n - 2)

    fibonacci_c[n] = value 
    return value 



def calculateSum(fibonacci_c, valueOne, total_lambs):
    """
    calculateSum

    Args:
        - 
    Output:
        - 
    
    
    """
    countOne = 0
    val = 0
    val2 = 0
    while val <= total_lambs:
        val = fibonacciVal(val2 + 2, fibonacci_c) - 1
        val2 += 1
        countOne += 1


    countTwo = countOne - 2 


    sum = abs(countTwo - valueOne) 

    return sum


def answer(total_lambs): 
  """
  answer 

  A function which calculates how to distribute lambs in the most generous and greedy cases given the conditions of the rules set 
  by Commander Lambda. 

  Args:
    - total_lambs: The total amount of lambs that must be distributed. 
  
  Output:   
    -   difference: The difference between the amount of henchmen who get paid under the most generous and most stingy distributions of lambs. 
  
  """
  valueOne = int(myLog(total_lambs + 1, 2)) 
  
  fibonacci_c = dict()
 
  difference = calculateSum(fibonacci_c, valueOne, total_lambs)  

  return difference 