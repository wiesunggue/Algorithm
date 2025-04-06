# 비트마스킹
# int = 50

1
10&14
fullPizza = (1<<20)-1 #모든 원소 켜기
print(fullPizza)
p=10
toppings= 1<<5
toppings |= 1<<p #p번째 원소를 추가하기
p=2

# 원소의 포함 여부 확인
print(toppings&(1<<p)) #p번째 원소의 존재 여부를 확인하기 0이면 없음 2**p라면 존재

# 원소의 삭제
p=10
print(toppings)
toppings &= ~(1<<p)
print(toppings)

# 원소의 토글 값이 있다면 제거 없다면 추가
toppings ^= (1<<p) #p번째 값을 추가

print(toppings)

# 두 집합에 대해서 연산하기
print('-'*50)
print('집합 연산')
A = (1<<10)-1
B = ((1<<5)-1) & ((1<<10)-1)
print(A,B)
adder = A|B # 합집합
intersection = A&B
removed = A &~ B
toggled = A ^ B
print(adder,intersection,removed,toggled)

# 집합의 크기 구하기
def bitCount(x):
    if x==0:
        return 0
    return x%2 + bitCount(x//2)

print(bin(removed),bitCount(removed))


# 비트의 개수 세기 int.bit_count()를 사용 python버전 3.10부터 지원
i=255
print(bin(i))
print(i.bit_count())

# 최소 원소 찾기
print(bin(toppings))
firstTopping = toppings & -toppings #자기 자신과 2의 보수
print(firstTopping)

# 최소 원소 지우기
print(bin(toppings))
toppings &= toppings-1
print(bin(toppings))

# 자기자신을 제외하고 모든 부분 집합 순회하기 => 공집합을 제외한 모든 부분집합을 출력한다
print(bin(adder))

subset = removed # removed에서 1의 개수가 5개이므로 5개의 원소를 가짐 => 이 5개의 원소중 적어도 하나를 가지는 모든 집합 출력
count=0
print('-'*50)
print('순회 시작')

while subset!=0:
    subset=(subset-1)&removed
    print(bin(subset))
    count+=1

print(count) # 개수는 2^5-1인 31개
toppings=16
print(bin(toppings))
print(bin(toppings&-toppings))

# 1. 구간 합을 계산하라
# 2. 특정 값을 업데이트 하라

