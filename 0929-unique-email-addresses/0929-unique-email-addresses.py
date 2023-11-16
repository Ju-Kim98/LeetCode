class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # 문자열.split('구분자')
        
        
        
        if len(emails) == 0:
            return 0
        elif len(emails) == 1:
            return 1
        else:
            my_set = set()
            for mail in emails:
                mail = mail.split('@')
                local = ''.join(mail[0].replace('.','').split('+')[0])
                domain = mail[-1]
                my_set.add(local+'@'+domain)
        return len(my_set)
        
