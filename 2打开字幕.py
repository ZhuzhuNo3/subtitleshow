from tkinter import *
import time,threading,os,signal,importlib
from datetime import datetime

def openwin():
    global tk
    global trans
    tk=Tk(className=' ')
    sw=tk.winfo_screenwidth()
    sh=tk.winfo_screenheight()
    #width的值为百分比
    trans=Label(tk,width=60,text='^_^\n',font=('Menlo','20'), fg='black', bg='white')
    trans.master.geometry("+%d+%d"%(int(sw*0.2),int(sh*0.8)))
    #trans.master.lift()
    trans.master.wm_attributes("-topmost", True)
    trans.master.wm_attributes("-alpha", 0.9)
    trans.pack()
    global text
    text=StringVar()
    text.set('▶︎')
    butt=Button(tk,textvariable=text,height=3,width=5,fg='red',bg='white',command=thread_it)
    butt.pack(before=trans,side=LEFT)
    #keepwin(tk,trans)
    tk.mainloop()

#打包函数进进程,防止卡死
def thread_it():
    global tagstop
    t = threading.Thread(target=substop,args=(tagstop,)) 
    t.setDaemon(True)
    t.start()

def substop(ss):
    global tagstop
    global text
    sign=('▶︎','■')
    if ss==0 or ss==3:#3为初始状态
        ss=1
        tagstop=1
        for i in range(3):
            text.set(str(3-i))
            time.sleep(1)
    else:
        ss=0
        tagstop=0
    print('tagstop=%d'%tagstop)
    time.sleep(0.1)
    text.set(sign[ss])
    time.sleep(0.2)

def keepwin(tk,trans,texts):
    trans.configure(text=texts)
    try:
        tk.update()
    except:
        print('窗口已关闭,结束进程')
        os.kill(os.getpid(), signal.SIGKILL)

def xuanze():
    b=[]
    for a,e,c in os.walk('.'):
        b=c
        break
    i=0
    while 1:
        try:
            if b[i][-3:]!='.py':
                del b[i]
            else:
                i+=1
        except:
            break
    k=0
    for i in b:
        print('%d %s'%(k,i))
        k+=1
    return b[int(input('choose num:'))][:-3]

#zimu=[(time1,time2,content),]
def display():
    global tagstop
    global starttime
    global stoptime
    global tempt
    global tk
    global trans
    global q
    global jj
    global kk
    while 1:
        #tagstop 1,start 2,keep 0,stop
        if tagstop==1:
            print('start')
            time.sleep(3)
            tagstop=2
            starttime=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            q=0
        if tagstop==2:
            nt=datetime.now()
            if jj==len(szimu):
                jj-=1
                tagstop=0
            a1=datetime.strptime(timeadd(timecut(starttime,stoptime),szimu[jj][0]),'%Y-%m-%d %H:%M:%S.%f')
            a2=datetime.strptime(timeadd(timecut(starttime,stoptime),szimu[jj][1]),'%Y-%m-%d %H:%M:%S.%f')
            if a1 <= nt < a2:
                tex1=szimu[jj][2]
                jj+=1
            elif a2 < datetime.now():
                jj+=1
            if kk==len(tzimu):
                kk-=1
            b1=datetime.strptime(timeadd(timecut(starttime,stoptime),tzimu[kk][0]),'%Y-%m-%d %H:%M:%S.%f')
            b2=datetime.strptime(timeadd(timecut(starttime,stoptime),tzimu[kk][1]),'%Y-%m-%d %H:%M:%S.%f')
            #print(a1,a2,b1,b2,nt)
            if b1 <= nt < b2:
                tex2=tzimu[kk][2]
                kk+=1
            elif b2 < datetime.now():
                kk+=1
            try:
                #if tempt!=tex1+'\n'+tex2:
                tempt=tex1+'\n'+tex2
                send2=tex2
                if len(tex2)>35:
                    l2=36
                    send2=tex2[:36]
                    if len(tex2[36:])>35:
                        l2=71
                        send2+='\n'+tex2[36:71]
                        if len(tex2[71:])>35:
                            l2=106
                            send2+='\n'+tex2[71:106]
                    send2+='\n'+tex2[l2:]
                keepwin(tk,trans,tex1+'\n'+send2)
            except:
                pass
        if tagstop==0 and q==0:
            print('stop')
            stoptime=timeadd(timecut(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],starttime[10:]),stoptime)[10:]
            #print('stoptime is %s'%stoptime)
            tagstop=0
            q=1
            jj-=1
            kk-=1
        try:
            tk.update()
        except:
            pass
        time.sleep(0.05)

def timeadd(ta,tb):
    #tb->H M S f ,ta->Y m d H M S f
    tb=tb.split(':')
    ta=ta.split(' ')
    if ta[1]=='':
        del ta[1]
    ta[1]=ta[1].split(':')
    k=0
    ta12=(float(ta[1][2])+float(tb[2]))
    if ta12>=60:
        ta12-=60
        k=1
    else:
        k=0
    ta[1][2]='%.3f'%ta12
    ta11=int(ta[1][1])+int(tb[1])+k
    if ta11>=60:
        ta11-=60
        k=1
    else:
        k=0
    ta[1][1]=str(ta11)
    ta[1][0]=str(int(ta[1][0])+int(tb[0])+k)
    return '%s %s:%s:%s'%(ta[0],ta[1][0],ta[1][1],ta[1][2])

def timecut(ta,tb):
    #ta-tb tb->H M S f ,ta->Y m d H M S f
    ta=ta.split(' ')
    ta[1]=ta[1].split(':')
    tb=tb.split(':')
    k=0
    if float(ta[1][2])<float(tb[2]):
        ta12=(float(tb[2])-float(ta[1][2]))
        k=1
    else:
        ta12=float(ta[1][2])-float(tb[2])
    ta[1][2]='%.3f'%ta12
    if int(ta[1][1])-k>=int(tb[1]):
        ta11=int(ta[1][1])-int(tb[1])-k
        k=0
    else:
        ta11=int(tb[1])-int(ta[1][1])+k
        k=1
    ta[1][1]=str(ta11)
    ta[1][0]=str(int(ta[1][0])-k-int(tb[0]))
    return '%s %s:%s:%s'%(ta[0],ta[1][0],ta[1][1],ta[1][2])



if __name__=='__main__':
    zimu=importlib.import_module(xuanze())#加载字幕
    texts=0
    tagstop=3
    tempt=0
    q=1
    jj=0
    kk=0
    stoptime='0:0:0.0'
    shutdown=0
    szimu=zimu.szimu
    tzimu=zimu.tzimu
    t = threading.Thread(target=display) 
    t.setDaemon(True)
    t.start()
    openwin()

