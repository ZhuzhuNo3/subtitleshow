from translate import Translator
import os

'''
仅支持一种格式😂 不打算改
example:
    1
    00:00:00.620 --> 00:00:01.540
    bulabulabula( /./!)
    
    num
    time --> time
    texts

'''

def entozh(sotext):
    tr=Translator(to_lang='chinese')
    return tr.translate(sotext)

def xuanze():
    tt=[]
    for a,b,c in os.walk('.'):
        tt=c
        break
    i=0
    while 1:
        try:
            if tt[i][-3:]!='txt':
                del tt[i]
            else:
                i+=1
        except:
            break
    j=0
    for i in tt:
        print('%d %s'%(j,i))
        j+=1
    return tt[int(input('choose num:'))]


def main():
    with open('%s'%(xuanze()),'r') as f:
        data=f.read().split('\n')
    sub=[]
    
    #格式化部分
    for i in range(len(data)):
        if data[i]=='':
            continue
        try:
            int(data[i])
            subtime1=data[i+1][:12]
            subtime2=data[i+1][17:]
            scontent=''
            try:
                for k in (2,3,4,5):
                    if data[i+k]!='':
                        scontent+=' '+data[i+k]
                    else:
                        break
            except:
                pass
            finally:
                sub.append([subtime1,subtime2,scontent])
        except:
            pass
    sub1=[]
    for i in sub:
        sub1.append([i[0],i[1],i[2]])
    i=0
    while 1:
        try:
            for k in range(9):
                if sub1[i+k][2][-1]=='.' or sub1[i+k][2][-1]=='!':
                    if k==0:
                        break
                    for q in range(k):
                        sub1[i][2]+=' '+sub1[i+1][2]
                        sub1[i][1]=sub1[i+1][1]
                        del sub1[i+1]
                    break
            i+=1
        except:
            break
    #格式化结束

    k=len(sub1)
    for i in range(k):
        os.system('clear')
        if i+1!=k:
            print('翻译中',end='')
        else:
            print('已完成',end='')
        print('%d/%d'%(i+1,k))
        sub1[i][2]=entozh(sub1[i][2])
    with open('zimu.py','w') as f:
        f.write('szimu='+str(sub)+'\n\n'+'tzimu='+str(sub1))

    print('ok!')

if __name__=='__main__':
    main()
