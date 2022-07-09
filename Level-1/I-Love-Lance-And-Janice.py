""" You've caught two of your fellow minions passing coded notes back and forth — while they're on duty, no less! Worse, you're pretty 
sure it's not job-related — they're both huge fans of the space soap opera “”Lance & Janice””. You know how much Commander Lambda hates 
waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it'll put you that much closer to a 
promotion.

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced 
with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched. That is,
 'a' becomes 'z', 'b' becomes 'y, 'c' becomes 'x', etc. For instance, the word “”vmxibkgrlm””, when decoded, would become “”encryption””.
Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the commander proof that 
these minions are talking about “”Lance & Janice”” instead of doing their jobs. 

Examples:
wrw blf hvv ozhg mrtsg'h vkrhlwv? >> did you see last night's episode?
Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!! >> Yeah! I can't believe Lance lost his job at the colony!!” 
"""

import string 

def solution(s):
    """
    solution 

    A function which takes in a phrase, and decrypts it based on the rule that lowercase letters [a..z] are replaced with their corresponding
    one [z..a]

    Args:
        - s: The encrypted message. 

    Output:
        - decrypted: The decrypted phrase. 
    
    """

    encrypted = [letter for letter in s] 

    alphabet = list(string.ascii_lowercase) 

    for idx, letter in enumerate(encrypted):
        if letter.islower():
            index = alphabet.index(letter) 
            encrypted[idx] = alphabet[25-index] 

    decrypted = ''.join(map(str, encrypted)) 

    return decrypted 

print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")) 
        

