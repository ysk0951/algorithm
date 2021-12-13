#순차 점검 프로세스 각각 10문제씩 돌면서 정답률 30%까지 접근
#탐 : 탐욕법에 의한 풀이인가? Y 정답률 43% 수준
#정 : 정렬에 의한 풀이인가? Y
#이 : 이진탐색(중간분할)이 포함된 문제인가? -
#D : DFS적요소가 있는가? N
#B : DFS적요소가 있는가? N
#다 : Caching을 사용하여 단순화가 필요한 문제인가? Y
#그 : 기타그래프이론(다익스트라, 플로이드워셜, # 크루스칼)의 관한 문제인가? N


N = int(input());
arr = [];
for i in range(N):
    arr.append(input().split(" "));

arr.sorted(lambda x : x[1]);
print(arr);