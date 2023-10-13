# https://www.acmicpc.net/problem/20665
# 독서실 거리두기 문제

Max_time=60*12
MAX_NUM=10**9
# 시간을 대응하는 index로 변환하기
def time_converter(state):
    hour=int(state[:2])
    minute=int(state[2:])
    converted_time=(hour-9)*60+minute
    return converted_time

def add_schedule(start,end):
    if start==720:
        return
    # 아무도 안 쓰는 경우
    if sum(arr[start]) == 0:
        idx=0
    else:# 1명 이상 사용중인 경우
        pos_arr=[]

        # 사용 중인 자리 찾기
        for i in range(N):
            if arr[start][i]!=0:
                pos_arr.append(i)
        print(pos_arr)
        # 위치에서 거리 비용 계산
        idx=0
        mscore = 0
        for i in range(N):
            score = MAX_NUM
            for j in pos_arr:
                score=min(abs(i-j),score)
            #print(score)
            print(i,score,mscore)
            if score==0:
                continue
            if score>mscore:
                mscore=score
                idx=i
    print(idx)
    if start==end:
        arr[start][idx]=1
    for i in range(start,end):
        arr[i][idx]=1

N,T,P=map(int,input().split())
arr = [[0 for i in range(N)] for _ in range(Max_time)]

time_arr = [list(map(time_converter,input().split())) for i in range(T)]
time_arr.sort()
#print(time_arr)
for i in range(T):
    add_schedule(*time_arr[i])
#print(*arr,sep='\n')
cnt=0
for i in range(Max_time):
    cnt+=arr[i][P-1]
print(Max_time-cnt)