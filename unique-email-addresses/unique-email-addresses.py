class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if len(emails) == 0:
            return 0
        elif len(emails) == 1:
            return 1
        else: 
            email_set = set()       # set = {"name@leetcode.com", "email.name@email.com", ... }
            
            for mail in emails:     # mail은 email list 요소들
                mail = mail.split('@')  #이메일을 @를 기준으로 , then mail[0](left part of list) is local part and mail[-1](right part of list) is domain part
                
                # 뒤에서부터 읽어야함
                # mail[0]부분의 요소를 + 로 split 하고 그 오른쪽 부분에서 .와  ''를 제거하고 
                # ''.join() -> join the processed string back together, but in this case, it's unnecessary
                #local = ''.join(mail[0].replace('.','').split('+')[0])  
                local = mail[0].replace('.','').split('+')[0]
                
                domain = mail[-1]       # list[-1] index is regfers the last element of the list
                email_set.add(local+'@'+domain)
        return len(email_set)
    
    
    # join() function is used when a list of strings that you want to combine into a single string. 