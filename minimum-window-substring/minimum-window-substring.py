class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        # dictionary which keep a count of all unique char in t
        dict_t = Counter(t) 
        
        # number of unique char in t, which need to be present in  the desired window
        required = len(dict_t)
        
        l, r = 0, 0
        
        # formed: to keep track of how many unique chars in t are present in cur window in its desired frequency
        # ex) AABC -> 2 A, 1B, 1C => 3
        formed = 0
        
        window_counts = {}
        
        # answer tuple: (window length, left, right)
        ans = float("inf"), None, None
        
        while r < len(s):
            # add one char from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0)+1
            
            # if the freq. of the curr char added equals to the desired count in t, then increment the formed count by 1
            if (
                character in dict_t and window_counts[character ] == dict_t[character] ):
                formed += 1
            
            # try and contract the window till the point where it cases to be 'desireable'
            while l <= r and formed == required:
                character = s[l]
                
                # save the smallest window untill now
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                # the char at the position pointed by the left pointer is no longer a part of window
                window_counts[character] -= 1
                if (
                    character in dict_t and window_counts[character] < dict_t[character]
                ):
                    formed -= 1
                # move left pointer ahead, this help to look for new window    
                l += 1
            # keep expanding the window once we are doe contracting
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2]+1]
        