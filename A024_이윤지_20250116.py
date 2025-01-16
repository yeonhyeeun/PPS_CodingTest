# 고객이 $5, $10, $20 지폐로 결제할 때, 주어진 돈으로 모든 고객에게 올바르게 거스름돈을 줄 수 있는지 확인하기

'''
$5 -> 거스름돈이 필요 없음. $5 지폐를 추가
$10 -> $5 지폐 하나를 거스름돈으로 줌
$20 -> 
$10 한 장과 $5 한 장을 주는 것이 가장 효율적
만약 $10이 없으면, $5 세 장으로 거스름돈을 줌
거스름돈을 줄 수 없는 경우, False를 반환
모든 고객을 처리하면 True 반환
'''

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_count = 0  # $5 지폐 개수
        ten_count = 0   # $10 지폐 개수

        for bill in bills:
            if bill == 5:
                five_count += 1  # $5는 바로 추가
            elif bill == 10:
                if five_count > 0:  # $5가 있는 경우 거스름돈 제공
                    five_count -= 1
                    ten_count += 1  # $10 지폐 추가
                else:
                    return False  # $5가 없으면 거스름돈을 줄 수 없음
            elif bill == 20:
                # $10와 $5 조합으로 거스름돈 제공
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                # $5 세 장으로 거스름돈 제공
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False  # 거스름돈을 줄 수 없음

        return True
