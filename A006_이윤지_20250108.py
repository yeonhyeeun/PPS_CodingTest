def solution(s):
    answer = True
    
    s = s.lower()
    
    p_count = s.count('p')  
    y_count = s.count('y')  
    
    answer = p_count == y_count  

    return answer

#코드리뷰 작성 📚
#9행 빼고는 나의 코드와 똑같았다 
