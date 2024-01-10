def solution(id_list, report, k):
    answer = []
    
    # 중복 신고는 1회 처리 
    report_set = set(report)
    
    # 신고 받은 회수 초기화
    bad_user_dict = dict.fromkeys(id_list, 0)

    # 신고 받은 회수 카운트
    for v in report_set:
        #print(v.split()[0], v.split()[1])
        if v.split()[1] in bad_user_dict:
            bad_user_dict[v.split()[1]] += 1
    
    # 2번 이상 신고받은 유저
    stop_user_list = [key for key, value in bad_user_dict.items() if value >= k]
    
    # 메일 받은 회수 초기화
    receive_mail_dict = dict.fromkeys(id_list, 0)
    
    # 메일 회수 카운트
    for m in report_set:
        if m.split()[1] in stop_user_list:
            receive_mail_dict[m.split()[0]] += 1
    
    #print(receive_mail_dict)
    
    return list(receive_mail_dict.values())