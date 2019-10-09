t=int(input())
answer=[]
def solution(s):
    count=0
    vowel=['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if i in vowel:
            count+=1
    return count


for i in range(t):
    string=input()
    answer.append(solution(string))
   

for i in answer:
    print(i)
