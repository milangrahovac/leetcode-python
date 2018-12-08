65. Valid Number

class Solution:
    def isNumber(self, s):

        nums = [str(x) for x in range(10)]
        symbols = ['+', '-', '.', 'e', " "]
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
                        if (fixed.count("+") > 1 and "e" not in fixed) or fixed.count("+") > 2:
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