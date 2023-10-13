from collections import deque
def find_island(arr):
    st = deque()
    st.append(-1)
    scnt=-1
    ecnt=0
    cnt=0
    for i in range(len(arr)):
        if st[-1] == arr[i]:
            continue
        if st[-1] < arr[i]:
            st.append(arr[i])
            scnt+=1
            #print(st)
        elif st[-1] == -1:
            continue
        else:
            while st:
                print(st)
                if st[-1]>arr[i]:
                    st.pop()
                    ecnt+=1
                elif st[-1]==arr[i]:
                    ecnt+=1
                    break
                else:
                    break
            st.append(arr[i])
            ecnt-=1
            scnt+=1
    print(scnt,ecnt)
    return ecnt
T = int(input())
for test in range(T):
    arr = list(map(int,input().split()))[1:]
    print(find_island(arr))

"""
0 -> 2 -> 4 -> 1 -> 0
0
0 2
0 2 4
0 1
0
"""