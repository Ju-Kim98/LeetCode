class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occ = {c: i for i, c in enumerate(s)} #enumerate:리스트 원소에 순서값을 부여하는 함수
        
        for i, c in enumerate(s):
            if c not in seen:
                
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
                
        return ''.join(stack)   #공백을 활용하여 문자열 붙이기(string join with space)
    
#using Stack and Greedy 