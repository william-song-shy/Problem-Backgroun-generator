# Problem-Background-generator
根据@Flamire 的生成器改编而成


用法：引入此文件

```python
gen_sentense() #生成一条语句
add_person (name :str,time=1) #在词句库中加入某个人，time表示次数（爆率）
```

示例：
```python
>>> gen_sentense()
'可笑的乌拉圭人燃烧着。'
>>> add_person("songhongyi",2)
>>> gen_sentense()
'尽管这样，但小丑还是虚幻的。'
>>> gen_sentense()
'这真的是伟大的啊！'
>>> gen_sentense()
'袋鼠欢呼着。'
>>> gen_sentense()
'现实被恶魔所憎恨。'
>>> gen_sentense()
'你考虑这样一件事情，就是说：'
>>> gen_sentense()
'由于可笑的天使手舞足蹈地是扭曲的songhongyi，智慧才能模仿世界。'
>>> add_person("le0n",999)
>>> gen_sentense()
'这真的是神圣的啊！'
>>> gen_sentense()
'可悲的le0n杀死le0n。'
>>> gen_sentense()
'但无力的le0n为什么要巧妙地捶打le0n呢？'
>>> 
```
