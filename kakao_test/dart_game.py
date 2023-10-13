def isint(a):
    return a >= '0' and a <= '9'


def solution(dartResult):
    length = len(dartResult)
    dartResult = dartResult + '0'
    answer = 0
    before = 0
    arr = []
    ans = []
    idx = 0
    for idx in range(length):
        if isint(dartResult[idx]):
            if dartResult[idx - 1] == '1' and dartResult[idx] == '0':
                continue
            arr.append(dartResult[before:idx])
            before = idx
    arr.append(dartResult[before:length])
    arr.pop(0)
    print(arr)
    for idx in range(3):
        arr[idx] = arr[idx].replace('S', '**1')
        arr[idx] = arr[idx].replace('D', '**2')
        arr[idx] = arr[idx].replace('T', '**3')
    for idx in range(3):
        if arr[idx][-1] == '#':
            ans.append(-eval(arr[idx][:-1]))
        elif arr[idx][-1] == '*':
            ans.append(eval(arr[idx][:-1]))
            if idx == 0:
                ans[0] *= 2
            else:
                ans[idx], ans[idx - 1] = ans[idx] * 2, ans[idx - 1] * 2
        else:
            ans.append(eval(arr[idx]))
    
    return sum(ans)

solution("10T10T10T")