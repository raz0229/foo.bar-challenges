"""""""""""""""
Minimal python program to convert plan text to Braille
  (Output: '1' represents a bump, '0' represents no bump)
  
Rules:
Your function should be able to encode the 26 lowercase letters, handle capital letters 
 by adding a Braille capitalization mark before that character, 
 and use a blank character (000000) for spaces
"""""""""""""""
def solution(s):
    to_convert = ""
    s = list(s)
    for x in s:
        if x.isupper():
            x = "000001" + x.lower()
        to_convert += x
    to_convert = to_convert.replace(" ", "000000").replace("a", "100000").replace("b","110000").replace("c","100100").replace("d","100110").replace("e","100010").replace("f","110100").replace("g","110110").replace("h","110010").replace("i","010100").replace("j","010110").replace("k","101000").replace("l","111000").replace("m","101100").replace("n","101110").replace("o","101010").replace("p","111100").replace("q","111110").replace("r","111010").replace("s","011100").replace("t","011110").replace("u","101001").replace("v","111001").replace("w","010111").replace("x","101101").replace("y","101111").replace("z","101011")
    return to_convert
  #All Test Cases Passed
