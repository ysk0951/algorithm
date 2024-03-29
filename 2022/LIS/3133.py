#탐 : 당장의 결정이 향후의 수를 줄여줌
#엘 : LIS(bisect)
#이 : 이진트리로 구조화 시켜야하는경우(이진탐색트리)
#디 : 전체루트를 한바퀴 검색하는경우
#비 : 한루트를 끝까지 검새하는경우
#다 : 캐싱이 반복적으로 사용되는경우
#그 : 기타 그래프 이론(사이클관련)
  # 다익스트라
  # 플로이드워셜
  # 크루스칼

#Idea
#len(LIS) 와 그 LIS를 역추적한것의 경우의수 + 시작점
#Code
N = int(input());
XY = [];
for i in range(N):
  XY.append(tuple(map(int,input().split(" "))))

XY.sort(key=lambda x:(x[0],x[1]));
sumForXY = [];
for i in XY :
  sumForXY.append(i[0]+i[1]);
print(XY);
print(sumForXY)
#Case
'''
11
8 6
7 4
5 4
5 1
5 6
6 2
3 2
4 3
4 5
3 5
2 4
>>>
4
3
'''