import re
import string

def arithmetic_arranger(problems, show_answers=False):

    # Patterns to extract
    num1Pattern = '\d+ '
    num2Pattern = ' \d+'
    symbols = string.punctuation
    digits = string.digits
    sgnPattern = fr'[{symbols}]'
    errorPattern = fr'[^{symbols + digits + " "}]'

    # Error Checking
    error_digit = any(re.findall(errorPattern, n) for n in problems)
    error_sign = not all( (re.findall(sgnPattern, n) == ["+"] or re.findall(sgnPattern, n) == ["-"]) for n in problems)
    error_numLen = any(
        len(re.findall(num1Pattern, n)[0]) >5 or 
        len(re.findall(num2Pattern, n)[0]) >5 
        for n in problems)
    error_numProb = len(problems) > 5

    if error_digit or error_sign or error_numLen or error_numProb:
        if error_numProb:
            problems = 'Error: Too many problems.'
        elif error_digit:
            problems = "Error: Numbers must only contain digits."
        elif error_sign: 
            problems = "Error: Operator must be '+' or '-'."
        elif error_numLen:
            problems = 'Error: Numbers cannot be more than four digits.'
        else:
            print("Unknown Error Occured")
    else:
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""
        lineAll = ""
        count = 0
        for i in problems:
            count += 1
            # print(re.findall(errorPattern, i))
            
            if re.findall(num1Pattern, i) and re.findall(num2Pattern, i):
                num1 = re.findall(num1Pattern, i)[0]
                num2 = re.findall(num2Pattern, i)[0]

                num1_int = int(num1)
                num2_int = int(num2)
 
                sign = re.findall(sgnPattern, i)
                ans = num1_int + num2_int if sign == ['+'] else num1_int- num2_int

                
                # Printing the Result

                maxNum1Num2Len = max(len(str(num1_int)),len(str(num2_int)))
                line1 += " " * (maxNum1Num2Len + 2 - len(str(num1_int))) + str(num1_int)
                line2 += sign[0] + " "*(maxNum1Num2Len +1 - len(str(num2_int))) + str(num2_int)
                line3 += "-"*(max(len(str(num1_int)),len(str(num2_int))) + 2) 

                line4 += " " * (maxNum1Num2Len + 1 - len(str(ans)) + 1  ) + str(ans)

                if count < len(problems):
                    line1 += " " * 4
                    line2 += " " * 4
                    line3 += " " * 4
                    line4 += " " * 4
                else:
                    line1 += "\n"
                    line2 += "\n"
                    if show_answers:
                        line3 += "\n"
            else:
                print("Error")

        problems = line1 + line2 + line3

        if show_answers:
            problems += line4

    return problems

# print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')

s = arithmetic_arranger(["3801 - 2", "123 + 49"], True)
print("\n" + s)
