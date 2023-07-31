def solution(survey, choices):
    answer = ''
    R, T, C, F, J, M, A, N = 0, 0, 0, 0, 0, 0, 0, 0
    RT, CF, JM, AN = "R", "C", "J", "A"
    
    for i in range(len(survey)):
        # 동의 영역 점수일 때
        if choices[i] > 4:
            if survey[i] == "RT":
                T += choices[i] - 4 # 성격 유형 점수로 환산
                if T > R: # 해당 점수가 높으면 높은 유형으로 저장
                    RT = "T"
            elif survey[i] == "TR":
                R += choices[i] - 4
                if R > T:
                    RT = "R"
            elif survey[i] == "FC":
                C += choices[i] - 4
                if C > F:
                    CF = "C"               
            elif survey[i] == "CF":
                F += choices[i] - 4
                if F > C:
                    CF = "F"
            elif survey[i] == "MJ":
                J += choices[i] - 4
                if J > M:
                    JM = "J"
            elif survey[i] == "JM":
                M += choices[i] - 4
                if M > J:
                    JM = "M"
            elif survey[i] == "AN":
                N += choices[i] - 4
                if N > A:
                    AN = "N"
            elif survey[i] == "NA":
                A += choices[i] - 4 
                if A > N:
                    AN = "A"        
                    
        # 비동의 영역 점수일 때            
        elif choices[i] < 4:
            if survey[i] == "RT":
                R += 4 - choices[i]
                if R > T:
                    RT = "R"
            elif survey[i] == "TR":
                T += 4 - choices[i]
                if T > R:
                    RT = "T"
            elif survey[i] == "FC":
                F += 4 - choices[i]
                if F > C:
                    CF = "F" 
            elif survey[i] == "CF":
                C += 4 - choices[i] 
                if C > F:
                    CF = "C"   
            elif survey[i] == "MJ":
                M += 4 - choices[i]      
                if M > J:
                    JM = "M"
            elif survey[i] == "JM":
                J += 4 - choices[i]
                if J > M:
                    JM = "J"
            elif survey[i] == "AN":
                A += 4 - choices[i] 
                if A > N:
                    AN = "A"
            elif survey[i] == "NA":
                N += 4 - choices[i]
                if N > A:
                    AN = "N"
                    
        # 같은 점수일 때 사전순으로 저장    
        if T == R:
            TR = "R"                    
        if F == C:
            CF = "C"                    
        if M == J:
            JM = "J"                    
        if N == A:
            AN = "A"
                             
    answer += RT+CF+JM+AN
    
    return answer
