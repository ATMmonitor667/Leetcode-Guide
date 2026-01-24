class Solution(object):
    def increasingTriplet(self, nums):
        # Initialize with infinity so any number will be smaller
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                # We found a new smallest number. 
                # It doesn't ruin the "second" we already found!
                first = n
            elif n <= second:
                # We found a number bigger than 'first' but smaller than 'second'.
                # Update 'second' because a smaller second makes it EASIER to find the 3rd.
                second = n
            else:
                # We found a number bigger than 'first' AND 'second'.
                # This is the 3rd number!
                return True
                
        return False