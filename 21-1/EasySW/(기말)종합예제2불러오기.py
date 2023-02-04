file=open('./문제지.txt','r')
scores=open('./채점지.txt','w')
stu_ans=file.readlines()

name=stu_ans[0]
stu_ans.pop(0)
stu_ans[0].replace
print(stu_ans)


for idx,ans in enumerate(stu_ans):
    ans.replace('n','')
    stu_ans[idx]=ans.split(' ')

print('')
print(stu_ans[0][-1])
