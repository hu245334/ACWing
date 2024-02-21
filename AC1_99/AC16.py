class Solution(object):
    def replaceSpaces(self, s):
        """
        :type s: str
        :rtype: str
        直接使用replace方法。
        """
        return s.replace(" ", "%20")
