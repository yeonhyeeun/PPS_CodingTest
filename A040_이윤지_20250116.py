
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set("aeiouAEIOU")
        
        # 문자열을 절반으로 나누기
        mid = len(s) // 2
        a, b = s[:mid], s[mid:]
        
        # 모음 개수를 계산하는 함수
        def count_vowels(substring):
            return sum(1 for char in substring if char in vowels)
        
        # 두 절반의 모음 개수 비교
        return count_vowels(a) == count_vowels(b)
