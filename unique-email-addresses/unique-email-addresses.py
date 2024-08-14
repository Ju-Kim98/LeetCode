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
            email_set = set()
            for mail in emails: 
                mail = mail.split('@')
                local = ''.join(mail[0].replace('.','').split('+')[0])
                domain = mail[-1]
                email_set.add(local+'@'+domain)
        return len(email_set)
