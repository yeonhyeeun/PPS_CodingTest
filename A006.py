def solution(s):
    answer = True
    
    s = s.lower()
    
    p_count = s.count('p')  
    y_count = s.count('y')  
    
    answer = p_count == y_count  

    return answer
