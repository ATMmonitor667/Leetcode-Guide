class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        one approach is to have a count of the length
        a count of special characters, any point where the remove is less then the length 
        
        """
        LIMIT = 10**15 + 1          
        lens = []
        length = 0
    
        for ch in s:                
            if ch.islower():
                length += 1
            elif ch == '*':
                length = max(0, length - 1)
            elif ch == '#':
                length = min(LIMIT, length * 2)
            lens.append(length)
    
        if k >= length:          
            return '.'
    
        for i in range(len(s) - 1, -1, -1):
            ch, cur_len = s[i], lens[i]
    
            if ch.islower():        
                prev_len = cur_len - 1
                if k == prev_len:
                    return ch
                length = prev_len
    
            elif ch == '*':       
                length = cur_len + 1
    
            elif ch == '#':         
                prev_len = cur_len // 2
                if k >= prev_len:      
                    k -= prev_len
                length = prev_len
    
            elif ch == '%':         
                k = cur_len - 1 - k  
                length = cur_len
    
        return '.' 
     
