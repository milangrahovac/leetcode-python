# 949. Largest Time for Given Digits

# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.
# Starting from 00:00, a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.
# If no valid time can be made, return an empty string.

# Example 1:
# Input: [1,2,3,4]
# Output: "23:41"

# Example 2:
# Input: [5,5,5,5]
# Output: ""

# Note:
# A.length == 4
# 0 <= A[i] <= 9


from itertools import permutations


class Solution(object):
    def largestTimeFromDigits(self, A):

        s = ""  # string
        m = A  # minutes
        times = []
        hours, minutes = 0, 0

        for x in A:
            s += str(x)

        for x in permutations(s, 2):
            m.remove(int(x[0]))
            m.remove(int(x[1]))

            if int("".join(x)) < 24 and min(m) < 60:

                i = str(m[0]) + str(m[1])
                imax = max(int(i), int(i[::-1]))
                imin = min(int(i), int(i[::-1]))

                if imax < 60:
                    times.append("".join(x) + format(imax, "02d"))
                elif imin < 60:
                    times.append("".join(x) + format(imin, "02d"))

            m.append(int(x[0]))
            m.append(int(x[1]))

        times = list(set(times))

        if len(times) == 0:
            return ""
        elif len(times) == 1:
            return "{}:{}".format(times[0][:2], times[0][2:])
        else:
            for time in times:
                hours = max(hours, int(time[:2]))

            for time in times:
                if hours == int(time[:2]):
                    minutes = max(minutes, int(time[2:]))

            hours = format(hours, "02d")
            minutes = format(minutes, "02d")

            return "{}:{}".format(hours, minutes)
