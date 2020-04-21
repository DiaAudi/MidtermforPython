with open('/Users/sjy/Desktop/testfile/score.txt') as f:
    origin_data =[l.strip('\n') for l in f.readlines()]
#print(origin_data)

num = len(origin_data) - 1
head = ['名次']+origin_data[0].split(' ')+['总分']+['平均分']+['\n']
final_rank= [0,0]
avg_sub = [0,0,0,0,0,0,0,0,0]
subject = [0,0,0,0,0,0,0,0,0]
total_ = 0
nameinfo = {}
namefrank = []
score_rank = {}
stu_rank = []
name_= []
#print(num)
#print (head)#
for i in origin_data[1:]:
    #print(i)
    total = 0
    fail = []
    score = i.split(' ')
    #print(score)#
    score2 = ([l if int(l)>=60 else '不及格' for l in score[1:10]])
    #print(score2)
    
    for z in score[1:10]:
        #print(z)#
        total += int(z)
        subject[score.index(z)-1] += int(z)

        '''if int(z) < 60:
            fail.append(score.index(z))
        '''
    name = score[0]
    #print(name)

        

        
    #print(subject)    
    #print(fail)
    #print(total)#
    avg = round(total/9,2)
    #print(avg) 
    #print(score2)
    total_ += total    
    nameinfo[name] = name +' ' + ' '.join(score2) + ' '+str(total) + ' '+str(avg) + '\n'
    #print(nameinfo[name])
    stu_rank.append('1')
    #print(nameinfo[name])
    namefrank.append(name)
    score_rank[name] = total
    name_.append('1')
#print(namefrank)
#print(total_)
#print(len(stu_rank))
for j in range (9):
    avg_sub[j] = str(round(subject[j]/num,2))
#print(avg_sub)
avg_total = round(total_/num,2)
avg_avg = round(avg_total/9,2)
print(avg_avg)
print(avg_total)
final_rank[1] ='0' + ' ' + '平均'+ ' ' + ' '.join(avg_sub) + ' '  + str(avg_total) + ' ' + str(avg_avg)  + '\n'

#print(namefrank)
#print(stu_rank)

for n in range (num):
    cr = 0
    #print(n)
    rep = []
    re = 0
    for k in range (num):
        if k != n:
            if score_rank[namefrank[n]] > score_rank[namefrank[k]]:
                cr += 1
            elif score_rank[namefrank[n]] == score_rank[namefrank[k]]:
                re +=1
                rep.append(namefrank[k])
    position = num-cr
    if re > 0:
        rep.append(namefrank[n])
        print(rep)
        for u in range (2):
            name_[position-u-1] = str(position-1) + ' ' + nameinfo[rep[u]]
    else:
        name_[position-1] = str(position) + ' ' + nameinfo[namefrank[n]]
        #print(name_[position-1])
        #stu_rank[position-1] = name_[position-1]
#print(stu_rank)
final_rank[0] = ' '.join(head)
for r in range (2,num+2):
    final_rank.append(name_[r-2])
print(final_rank)

with open('/Users/sjy/Desktop/testfile/result.txt', 'w') as f:
    f.writelines(final_rank)








