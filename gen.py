import re
import random
sentenses = ["%a%s%b%v%a%o。","正因为如此，所以%a%s%b%v%a%o。","由于%a%s%b%v%a%o，%a%s才能%b%v%a%o。","但%a%s为什么要%b%v%a%o呢？","这真的是%A啊！","你考虑这样一件事情，就是说：","尽管这样，但%n还是%A。","%a%o被%a%s所%b%v。","%a%s%b%w着。"]
n=["袋鼠","乌拉圭人","小丑","天使","恶魔","世界","城市","木偶","人们","现实","智慧"]
suj=["袋鼠","乌拉圭人","小丑","天使","恶魔","世界","城市","木偶","人们","现实","智慧"]
obj=["袋鼠","乌拉圭人","小丑","天使","恶魔","世界","城市","木偶","人们","现实","智慧"]
vt=["怀念","捶打","是","玩弄","憎恨","歌颂","控制","模仿","怀疑","编造","成为","反抗","遗弃","杀死","反杀"]
vi=["消逝","叹息","欢呼","爬","暴毙","幻想","燃烧","爬来爬去","歌唱","忏悔","无能狂怒"]
adj=["扭曲的","可悲的","悲哀的","可怜的","黑暗的","善良的","无力的","无助的","虚幻的","可笑的","残酷的","伟大的","神圣的"]
adv=["愤怒地","无知地","手舞足蹈地","狂笑着","公然","巧妙地","小心地"]

def add_person (name :str,time=1):
    for i in range (time):
        n.append(name)
        suj.append(name)
        obj.append(name)

def delete_person (name:str):
    global n,suj,obj
    n = list(filter(lambda x:x!=name,n))
    suj = list(filter(lambda x:x!=name,suj))
    obj = list(filter(lambda x:x!=name,obj))

def put_in (matched):
    f=matched.group()
    f=f[1::]
    flag=random.randint(0,1)
    if f=="a":
        if flag:
            return random.choice(adj)
    if f=="b":
        if flag:
            return random.choice(adv)
    if f=="s":
        return random.choice(suj)
    if f=="o":
        return random.choice(obj)
    if f=="n":
        return random.choice(n)
    if f=="w":
        return random.choice(vi)
    if f=="A":
        return random.choice(adj)
    if f=="v":
        return random.choice(vt)
        

def gen_sentense():
    form=random.choice(sentenses)
    return re.sub('%[A-Z,a-z]', put_in, form)
