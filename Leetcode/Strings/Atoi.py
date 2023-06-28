class solution:
    def atoi (self, s):
        # Remove leading whitespace
        s= s.strip()

        # Check if the string is empty after removing whitespace
        if not s:
            return 0
        
        # Check if the first character is a sign ('-' or '+')
        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            s= s[1:]

        # Convert the remaining characters into an integer
        num = 0
        for i in s:
            if not i.isdigit():
                break
            num = num * 10 + int(i)
        
        # Apply the sign
        if negative:
            num = -num

        # Clamp the integer to the 32-bit signed range
        int_max = 2**31 -1
        int_min = - 2**31
        num = max(int_min, min(int_max,num))

        return num
    
solution = solution()
s = str(input("Type Any String containing numbers in it : "))
print(solution.atoi(s))