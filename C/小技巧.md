## 解决 C/C++ 程序执行一闪而过的方法

### 简述
在 VS 编写控制台程序的时候，包括使用其他 IDE（Visual C++）编写 C/C++ 程序，经常会看到程序的执行结果一闪而过，要解决这个问题，可以在代码的最后加上 system("pause")、getchar()、cin.get()。



### 推荐方法
比较常用的做法是使用 system("pause")，但这篇文章：Things to Avoid in C/C++ -- system("pause") 不推荐使用 system("pause")，因为：

不可移植：只适合 Dos 或 Windows，不适合 Linux 等。
耗费系统资源：调用系统命令 system() 去做”暂停程序”的事情有点大材小用。
必须添加头文件：stdlib.h 或 cstdlib。
所以，应该尽量摒弃。

推荐方法：

在 C 中，使用 getchar()。
在 C++ 中，使用 cin.get()。
替代方法
丰富一下两种替代方法：

在 C 中：

printf("按任意键继续……");
getchar();

在 C++ 中：

cout<<"按任意键继续……";
cin.clear();
cin.sync();
cin.get();

加上 cin.clear()、cin.sync() 这两句，是清空缓存区，让 cin.get() 真正接收到你的键盘输入。
————————————————
版权声明：本文为CSDN博主「一去丶二三里」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liang19890820/article/details/51785211