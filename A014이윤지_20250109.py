#연속된 숫자들을 그룹화하여 범위를 나타내는 문자열을 반환

'''
입력: 정렬된 고유한 정수 배열 nums가 주어짐
목표: 배열에서 연속된 숫자들을 그룹화하여 가장 작은 범위 리스트를 반환해야 함
연속된 숫자의 범위는 [a, b]로 표현
범위가 단일 숫자라면 "a"로, 여러 숫자를 포함하면 "a->b"로 표현

** 각 숫자는 정확히 하나의 범위에 포함되어야 함
** 정렬된 결과 리스트를 반환
** 배열이 비어 있을 경우 빈 리스트 []를 반환

풀이
1. 빈 리스트인 경우 즉시 반환
2. 배열을 한 번 순회하면서,
3. 연속되는 숫자인지 확인
4. 연속되지 않으면 이전 범위를 기록하고 새로운 범위를 시작
5. 마지막 범위를 처리 후 결과 반환
'''

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:  # 빈 리스트 처리
            return []
        
        ranges = []
        start = nums[0]  # 현재 범위의 시작점
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # 연속되지 않으면
                # 현재 범위를 결과에 추가
                if start == nums[i - 1]:
                    ranges.append(str(start))  # 단일 숫자
                else:
                    ranges.append("{}->{}".format(start, nums[i - 1]))  # 범위
                start = nums[i]  # 새로운 범위 시작
        
        # 마지막 범위 추가
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append("{}->{}".format(start, nums[-1]))
        
        return ranges


# 코드리뷰 
# 문제에 필요한 메서드를 적절히 사용하여 간략하게 잘 작성하였다
