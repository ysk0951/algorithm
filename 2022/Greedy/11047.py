#탐 : 최선의 경우를 만드는방식이 탐욕법에 가깝다고 생각이듬
#정 : 이미되어있음
#이 : 이진탐색(중간을 자르는경우)를 생각할수 없음
#디 : 재귀는 필요할수도있다고 생각이듬
#비 : 최단경로등이 그래프로 표현안되어있음
#다 : 캐싱 없음

#idea : 가장 큰수를 빼고 아래차수중 어떠한 수로도 나눌수있으면 더빼본다는 Greedy
first = list(map(int,input().split(" ")));
N = first[0];
K = first[1];
answer = 0;
value = [];
for i in range(N):
  value.append(int(input()));

value = value[::-1];
print(N,K,value);

for i in value:
  canDivide = False;
  idx = value.index(i)+1;
  print(idx);
  while(True):
    num = K - i ;
    isCountinue = False;
    for j in range(idx,N):
      if num%value[j]==0:
         isCountinue = True;
         K = num;
         answer+=1;
         print("inner",isCountinue)
         break
    print("Outer",isCountinue,answer)
    break;
      
    # if isCountinue == False :
    #   break
    
  # while(true):
  #   num = K - i;
  #   canDivide = False;
  #   idx = index 
  #   answer++
  
  # if(K%i == 0):
  #   answer += K/i;
    
#try2 : 가장 큰수를 빼고 아래차수중 어떠한 수로도 나눌수있으면 더빼본다는 Greedy
N,K=map(int,input().split());a=[]
for i in range(0,N):
    a.append(int(input()))
a.sort(reverse=True)
count=0
for i in a:
    if K>=i:
        count+=K//i
        K-=i*(K//i)
print(count,end='')

## 놓친점 :: A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) 라는 조건때문에 그리디가 가능 아니면 dp로 풀어야됬어야함.. 문제를 잘못읽음
  
