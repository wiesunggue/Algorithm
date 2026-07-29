# 알고리즘 문제 풀이를 위한 C++ STL 핵심 정리

오랜만에 C++로 알고리즘 문제를 풀 때 빠르게 기억을 되살리기 위한
C++17 기준 요약 문서이다.

## 1. 기본 템플릿

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    return 0;
}
```

`#include <bits/stdc++.h>`는 대부분의 알고리즘 대회 환경에서 사용할 수
있지만 표준 헤더는 아니다. 일반 프로젝트에서는 필요한 헤더를 개별적으로
포함하는 편이 좋다.

자주 사용하는 자료형:

```cpp
int x = 1;                   // 약 ±21억
long long big = 1LL << 60;   // 큰 정수
double value = 3.14;
char ch = 'A';
string text = "hello";
bool visited = false;
```

곱셈 결과가 `int` 범위를 넘을 수 있으면 연산 전에 `long long`으로
변환한다.

```cpp
long long result = 1LL * a * b;
```

## 2. 입출력

```cpp
int n;
cin >> n;

vector<int> numbers(n);
for (int& value : numbers) {
    cin >> value;
}

cout << n << '\n';
```

줄 전체 입력:

```cpp
string line;
getline(cin, line);
```

`cin >>` 다음에 `getline`을 사용하면 남아 있는 개행 문자를 제거해야 한다.

```cpp
cin.ignore(numeric_limits<streamsize>::max(), '\n');
getline(cin, line);
```

소수점 출력:

```cpp
cout << fixed << setprecision(10) << value << '\n';
```

`endl`은 줄바꿈과 함께 버퍼를 비우므로, 일반적으로 `'\n'`이 더 빠르다.

## 3. 반복문과 범위 기반 for

```cpp
for (int i = 0; i < n; ++i) {
    cout << numbers[i] << ' ';
}

for (int value : numbers) {
    cout << value << ' ';
}

// 원본 값을 변경하려면 참조를 사용한다.
for (int& value : numbers) {
    value *= 2;
}

// 복사 없이 읽기만 한다.
for (const int& value : numbers) {
    cout << value << ' ';
}
```

## 4. vector

크기가 변할 수 있는 동적 배열이다. 임의 접근은 `O(1)`이고, 뒤쪽 삽입과
삭제는 평균 `O(1)`이다.

```cpp
vector<int> values;
values.push_back(10);
values.push_back(20);
values.pop_back();

int last = values.back();
int first = values.front();
int size = static_cast<int>(values.size());
bool empty = values.empty();
```

초기화:

```cpp
vector<int> a(5);          // 크기 5, 모두 0
vector<int> b(5, -1);      // 크기 5, 모두 -1
vector<int> c = {1, 2, 3};

vector<vector<int>> graph(n + 1);
vector<vector<int>> matrix(n, vector<int>(m, 0));
```

크기와 용량:

```cpp
values.resize(10);       // 실제 원소 개수를 변경
values.reserve(100000);  // 메모리 재할당을 줄이도록 용량만 확보
```

원소 삭제:

```cpp
values.erase(values.begin() + index);  // 중간 삭제 O(N)
values.clear();
```

특정 값을 모두 제거하는 erase-remove:

```cpp
values.erase(
    remove(values.begin(), values.end(), target),
    values.end()
);
```

중복 제거:

```cpp
sort(values.begin(), values.end());
values.erase(unique(values.begin(), values.end()), values.end());
```

`unique`는 연속된 중복을 뒤로 밀기 때문에 먼저 정렬해야 전체 중복이
제거된다.

## 5. array

컴파일 시점에 크기가 정해지는 고정 길이 배열이다.

```cpp
array<int, 4> direction = {0, 1, 2, 3};
direction.fill(-1);
sort(direction.begin(), direction.end());
```

일반 배열 초기화:

```cpp
int dist[1000];
fill(dist, dist + 1000, INF);
```

## 6. string

```cpp
string s = "algorithm";

char first = s[0];
s.push_back('!');
s.pop_back();

string part = s.substr(0, 4);  // 시작 위치, 길이
size_t position = s.find("go");

if (position == string::npos) {
    // 찾지 못함
}
```

문자열과 숫자 변환:

```cpp
int number = stoi("123");
long long big = stoll("1234567890123");
string text = to_string(123);
```

문자 판별:

```cpp
isdigit(ch);
isalpha(ch);
islower(ch);
isupper(ch);
tolower(ch);
toupper(ch);
```

`char`가 음수가 될 수 있는 환경에서는 `<cctype>` 함수에 전달하기 전에
`unsigned char`로 변환하는 것이 안전하다.

## 7. pair와 tuple

두 값을 묶을 때 `pair`를 사용한다.

```cpp
pair<int, int> point = {3, 5};
cout << point.first << ' ' << point.second;

auto [x, y] = point;  // C++17 구조적 바인딩
```

`pair`는 기본적으로 `first`, 이후 `second` 순서로 비교된다.

세 개 이상의 값을 묶을 때:

```cpp
tuple<int, int, string> item = {1, 20, "name"};
auto [id, score, name] = item;
```

## 8. stack, queue, deque

### stack

후입선출(LIFO) 구조이다.

```cpp
stack<int> st;
st.push(10);
st.push(20);

int top = st.top();
st.pop();
bool empty = st.empty();
```

### queue

선입선출(FIFO) 구조로 BFS에서 주로 사용한다.

```cpp
queue<int> q;
q.push(10);
q.push(20);

int front = q.front();
q.pop();
```

### deque

양쪽 끝에서 `O(1)` 삽입과 삭제가 가능하다. 0-1 BFS에도 사용한다.

```cpp
deque<int> dq;
dq.push_front(1);
dq.push_back(2);

dq.pop_front();
dq.pop_back();
```

## 9. priority_queue

기본은 최댓값이 먼저 나오는 최대 힙이다.

```cpp
priority_queue<int> max_heap;
max_heap.push(3);
max_heap.push(10);
cout << max_heap.top();  // 10
```

최소 힙:

```cpp
priority_queue<int, vector<int>, greater<int>> min_heap;
```

다익스트라에서 자주 쓰는 형태:

```cpp
using State = pair<long long, int>;  // 거리, 정점
priority_queue<State, vector<State>, greater<State>> pq;

pq.push({0, start});

while (!pq.empty()) {
    auto [cost, node] = pq.top();
    pq.pop();

    if (cost != distance[node]) {
        continue;
    }
}
```

`priority_queue`는 중간 원소 삭제나 값 갱신을 직접 지원하지 않는다.
새 값을 다시 넣고 꺼낼 때 오래된 값인지 검사하는 방식을 사용한다.

## 10. set과 multiset

정렬된 원소 집합이며 보통 균형 이진 탐색 트리로 구현된다.

```cpp
set<int> numbers;
numbers.insert(3);
numbers.insert(1);
numbers.insert(3);  // 중복 저장 안 됨

bool exists = numbers.contains(3);  // C++20
bool exists17 = numbers.find(3) != numbers.end();  // C++17

numbers.erase(3);
```

주요 연산은 `O(log N)`이다.

경계 검색:

```cpp
auto lower = numbers.lower_bound(x);  // x 이상인 첫 원소
auto upper = numbers.upper_bound(x);  // x보다 큰 첫 원소
```

`multiset`은 중복 원소를 허용한다.

```cpp
multiset<int> values = {1, 1, 2};

values.erase(1);  // 값이 1인 원소를 모두 삭제

auto it = values.find(1);
if (it != values.end()) {
    values.erase(it);  // 한 개만 삭제
}
```

## 11. map과 unordered_map

### map

키가 정렬된 상태로 유지되며 주요 연산은 `O(log N)`이다.

```cpp
map<string, int> count;
count["apple"]++;
count["banana"] = 3;

for (const auto& [key, value] : count) {
    cout << key << ' ' << value << '\n';
}
```

존재하지 않는 키에 `operator[]`를 사용하면 기본값으로 새 원소가 생성된다.
존재 여부만 확인할 때는 `find`를 사용한다.

```cpp
if (count.find("apple") != count.end()) {
    // 존재함
}
```

### unordered_map

해시 테이블로 평균 `O(1)` 연산을 제공하지만 정렬 순서를 보장하지 않는다.
최악의 경우 `O(N)`이 될 수 있다.

```cpp
unordered_map<int, int> frequency;
frequency.reserve(n * 2);

for (int value : values) {
    frequency[value]++;
}
```

정렬 순서나 `lower_bound`가 필요하면 `map`, 빠른 키 조회만 필요하면
`unordered_map`을 우선 고려한다.

## 12. 정렬

기본 오름차순:

```cpp
sort(values.begin(), values.end());
```

내림차순:

```cpp
sort(values.begin(), values.end(), greater<int>());
```

람다 비교 함수:

```cpp
vector<pair<int, int>> points;

sort(points.begin(), points.end(), [](const auto& a, const auto& b) {
    if (a.first != b.first) {
        return a.first < b.first;
    }
    return a.second > b.second;
});
```

비교 함수는 두 값이 동등할 때 `false`를 반환해야 한다. `<=`나 `>=`를
사용하면 strict weak ordering 조건을 위반할 수 있으므로 `<` 또는 `>`를
사용한다.

안정 정렬:

```cpp
stable_sort(values.begin(), values.end());
```

일부 원소만 정렬된 위치로 만들기:

```cpp
nth_element(values.begin(), values.begin() + k, values.end());
// values[k]는 전체 정렬했을 때 k번째 값
```

## 13. 이분 탐색 함수

반드시 정렬된 범위에서 사용한다.

```cpp
sort(values.begin(), values.end());

bool exists = binary_search(values.begin(), values.end(), target);

auto lower = lower_bound(values.begin(), values.end(), target);
auto upper = upper_bound(values.begin(), values.end(), target);

int first_index = static_cast<int>(lower - values.begin());
int target_count = static_cast<int>(upper - lower);
```

- `lower_bound`: target 이상인 첫 위치
- `upper_bound`: target보다 큰 첫 위치

## 14. 자주 쓰는 algorithm 함수

```cpp
int minimum = *min_element(values.begin(), values.end());
int maximum = *max_element(values.begin(), values.end());

auto [min_it, max_it] = minmax_element(values.begin(), values.end());

int count_x = count(values.begin(), values.end(), x);

reverse(values.begin(), values.end());
rotate(values.begin(), values.begin() + k, values.end());

bool all_positive = all_of(values.begin(), values.end(),
                           [](int x) { return x > 0; });

bool has_zero = any_of(values.begin(), values.end(),
                       [](int x) { return x == 0; });
```

최대공약수와 최소공배수:

```cpp
int g = gcd(a, b);
int l = lcm(a, b);
```

순열 생성:

```cpp
sort(values.begin(), values.end());

do {
    // 현재 순열 사용
} while (next_permutation(values.begin(), values.end()));
```

## 15. numeric 함수

합계:

```cpp
long long total = accumulate(values.begin(), values.end(), 0LL);
```

초깃값이 결과 자료형을 결정하므로 큰 합에는 `0`이 아니라 `0LL`을
사용한다.

연속된 값 채우기:

```cpp
vector<int> order(n);
iota(order.begin(), order.end(), 0);  // 0, 1, 2, ...
```

부분 합:

```cpp
vector<long long> prefix(n + 1, 0);

for (int i = 0; i < n; ++i) {
    prefix[i + 1] = prefix[i] + values[i];
}

// [left, right) 구간 합
long long range_sum = prefix[right] - prefix[left];
```

## 16. min, max, swap, clamp

```cpp
int smaller = min(a, b);
int larger = max(a, b);

int smallest = min({a, b, c});
int largest = max({a, b, c});

swap(a, b);

int bounded = clamp(value, low, high);  // C++17
```

`min`과 `max`의 인자 자료형은 같아야 한다.

```cpp
long long answer = min(1LL * a, b_long_long);
```

## 17. 비트 연산과 bitset

```cpp
int mask = 0;

mask |= 1 << i;          // i번째 비트 켜기
mask &= ~(1 << i);       // i번째 비트 끄기
mask ^= 1 << i;          // i번째 비트 뒤집기
bool on = mask & (1 << i);

int bit_count = __builtin_popcount(mask);
int bit_count_ll = __builtin_popcountll(long_long_mask);
```

`1 << i`에서 `i`가 31 이상일 수 있으면 `1LL << i`를 사용한다.

```cpp
bitset<100> bits;
bits.set(3);
bits.reset(3);
bits.flip(5);
bool on = bits.test(5);
int count = static_cast<int>(bits.count());
```

## 18. 사용자 정의 구조체와 비교

```cpp
struct Edge {
    int from;
    int to;
    int weight;
};

vector<Edge> edges;

sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
    return a.weight < b.weight;
});
```

`priority_queue`에서 사용자 정의 비교:

```cpp
struct Compare {
    bool operator()(const Edge& a, const Edge& b) const {
        return a.weight > b.weight;  // 작은 weight가 먼저 나오는 최소 힙
    }
};

priority_queue<Edge, vector<Edge>, Compare> pq;
```

## 19. 반복자 사용 시 주의점

`vector`에 원소를 추가하거나 삭제하면 기존 반복자가 무효화될 수 있다.

순회 중 조건부 삭제:

```cpp
for (auto it = numbers.begin(); it != numbers.end();) {
    if (*it % 2 == 0) {
        it = numbers.erase(it);
    } else {
        ++it;
    }
}
```

`erase` 이후에는 삭제된 반복자를 다시 사용하지 않고 반환된 다음 반복자를
사용한다.

## 20. 알고리즘에서 자주 쓰는 상수

```cpp
const int INF = 1'000'000'000;
const long long INF_LL = 4'000'000'000'000'000'000LL;
const int MOD = 1'000'000'007;

const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};
```

거리 덧셈 전에 현재 거리가 무한대인지 확인하면 오버플로를 막을 수 있다.

```cpp
if (distance[u] != INF_LL &&
    distance[v] > distance[u] + weight) {
    distance[v] = distance[u] + weight;
}
```

## 21. 기억해 둘 핵심 선택 기준

| 목적 | 우선 고려할 STL |
|---|---|
| 순차 저장, 임의 접근 | `vector` |
| 양쪽 끝 삽입·삭제 | `deque` |
| BFS | `queue` |
| DFS 반복 구현 | `stack` |
| 최솟값·최댓값 반복 추출 | `priority_queue` |
| 정렬된 유일 원소 | `set` |
| 정렬된 키-값 | `map` |
| 평균 O(1) 키 조회 | `unordered_set`, `unordered_map` |
| 고정 크기 배열 | `array` |
| 중복을 허용하는 정렬 집합 | `multiset` |

문제를 풀 때는 먼저 필요한 연산이 무엇인지 정리하고, 그 연산의 시간
복잡도를 만족하는 컨테이너를 선택한다.
