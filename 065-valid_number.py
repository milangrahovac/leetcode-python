# 65. Valid Number

# Validate if a given string can be interpreted as a decimal number.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false

# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
# However, here is a list of characters that can be in a valid decimal number:

# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# Of course, the context of these characters also matters in the input.

# Update (2015-02-10):
# The signature of the C++ function had been updated.
# If you still see your function signature accepts a const char * argument,
# please click the reload button to reset your code definition.


class Solution:
    def isNumber(self, s):

        nums = [str(x) for x in range(10)]
        symbols = ["+", "-", ".", "e", " "]
        allowed = nums + symbols

        if all(x in allowed for x in s):
            if any(i in nums for i in s):
                if s.count(".") <= 1 and s.count("e") <= 1 and s.count("-") <= 1:

                    fixed = s

                    for x in fixed:
                        if x == " ":
                            fixed = fixed[1:]
                        else:
                            break

                    for y in fixed[::-1]:
                        if y == " ":
                            fixed = fixed[:-1]
                        else:
                            break

                    if " " in fixed:
                        return False

                    if "+" in fixed and "-" not in fixed:
                        if (fixed.count("+") > 1 and "e" not in fixed) or fixed.count(
                            "+"
                        ) > 2:
                            return False
                        if fixed[-1] == "+":
                            return False
                        if all(x in nums for x in fixed[1:]):
                            return True
                        if "e" not in fixed and fixed[0] != "+":
                            return False

                    if "-" in fixed:
                        if "+" in fixed and "e" not in fixed:
                            return False
                        elif all(x in nums for x in fixed[1:]):
                            return True
                        elif fixed[0] == "-" and fixed[1] == "e":
                            return False
                        elif fixed[0] == "." and "e" not in fixed:
                            return False
                        elif "e" not in fixed:
                            if fixed[0] != "-":
                                return False

                    if "." in fixed and "e" not in fixed:
                        return True

                    if "e" in fixed and len(fixed) >= 3:
                        if fixed[0] != "e" and fixed[-1] not in ["e", "."]:

                            if "-" in fixed:
                                if fixed[-1] == "-":
                                    return False
                                elif fixed.index("e") < fixed.index("-"):
                                    if not fixed.index("e") + 1 == fixed.index("-"):
                                        return False
                                elif fixed.index("-") + 1 == fixed.index("e"):
                                    return False

                            if "." in fixed:
                                if fixed[0] == "." and fixed[1] == "e":
                                    return False
                                if fixed.index(".") > fixed.index("e"):
                                    return False
                                else:
                                    return True
                            else:
                                return True

                    if all(x in nums for x in fixed):
                        return True
                    return False
        return False
