from typing import Self


class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        #two-pointer approach
        left, right = 0, len(chars) - 1
        
        while left < right:
            
            if chars[left] in vowels and chars[right] in vowels:
                
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            elif chars[left] in vowels:
                right-=1
            else:
                left+=1
        return ''.join(chars)
        
    str =  "hello World"
    print(reverseVowels(Self, str))