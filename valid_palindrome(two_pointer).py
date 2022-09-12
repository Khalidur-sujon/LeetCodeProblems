class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re 
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        
        length = len(s)
        first_index = 0
        last_index = length - 1
          
        while (first_index < last_index):
            if (s[first_index] == s[last_index]):
                first_index += 1
                last_index -= 1
            else:
                return False
        return True