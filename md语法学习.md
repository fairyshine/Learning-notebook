# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题

**这是加粗的文字** 
*这是倾斜的文字*
***这是斜体加粗的文字***
~~这是加删除线的文字~~

>这是引用的内容
>>这是引用的内容
>>>>>这是引用的内容
>>>>>
>>>>>>可无限嵌套

---
----
分割线
***
效果相同
*****

![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

[超链接名](超链接地址 "超链接title")
title可加可不加

[简书](http://jianshu.com)
[百度](http://baidu.com)

- 列表内容
+ 列表内容
* 列表内容

注意：- + * 跟内容之间都要有一个空格

1. 列表内容
2. 列表内容
3. 列表内容

注意：序号跟内容之间要有空格

|表头|表头|表头|
|---|:--:|---:|
|内容|内容|内容|
|内容|内容|内容|

第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
-两边加：表示文字居中
-右边加：表示文字居右
注：原生的语法两边都要用 | 包起来。此处省略

姓名|技能|排行
:-:|:-:|:-:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

`代码内容`

`create database hero;`

```
  代码...
  代码...
  代码...
```

```javascript
    function fun(){
         echo "这是一句非常牛逼的代码";
    }
    fun();
```

```flow
st => start:开始
op => operation: My Operation
cond => condition: Yes or No?
e => end
st -> op -> cond
cond(yes) -> e
cond(no) -> op
```

```flow                     // 流程
st=>start: 开始|past:> http://www.baidu.com // 开始
e=>end: 结束              // 结束
c1=>condition: 条件1:>http://www.baidu.com[_parent]   // 判断条件
c2=>condition: 条件2      // 判断条件
c3=>condition: 条件3      // 判断条件
io=>inputoutput: 输出     // 输出
//----------------以上为定义参数-------------------------

//----------------以下为连接参数-------------------------
// 开始->判断条件1为no->判断条件2为no->判断条件3为no->输出->结束
st->c1(yes,right)->c2(yes,right)->c3(yes,right)->io->e
c1(no)->e                   // 条件1不满足->结束
c2(no)->e                   // 条件2不满足->结束
c3(no)->e                   // 条件3不满足->结束
```


```flow                             // 流程
st=>start: 启动|past:>http://www.baidu.com[blank] // 开始
e=>end: 结束                      // 结束
op1=>operation: 方案一             // 运算1
sub2=>subroutine: 方案二|approved:>http://www.baidu.com[_parent]  // 运算2
sub3=>subroutine: 重新制定方案        // 运算2
cond1=>condition: 行不行？|request  // 判断条件1
cond2=>condition: 行不行？          // 判断条件2
io=>inputoutput: 结果满意           // 输出

// 开始->方案1->判断条件->
st->op1->cond1
// 判断条件1为no->方案2->判断条件2为no->重新制定方案->方案1
cond1(no,right)->sub2->cond2(no,right)->sub3(right)->op1
cond1(yes)->io->e       // 判断条件满足->输出->结束
cond2(yes)->io->e       // 判断条件满足->输出->结束
```

```sequence
起床->吃饭: 稀饭油条
吃饭->上班: 不要迟到了
上班->午餐: 吃撑了
上班->下班:
Note right of 下班: 下班了
下班->回家:
Note right of 回家: 到家了
回家-->>起床:
Note left of 起床: 新的一天
```

- [x] 选项一

- [ ] 选项二 

- [ ] [选项3]

$$
x \href{why-equal.html}{=} y^2 + 1
$$


$$
x \href{why-equal.html}{=} y^2 + 1
$$


