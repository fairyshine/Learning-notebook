## 终端操作与shell命令1
ls		目录下文件查看     -a显示目录所有文件及文件夹（包括隐藏）-l详细信息
cd		目录切换   cd ..返回上一级
pwd  当前目录路径显示
uname  系统信息查看 -a全部信息
clear    清屏（往上拉还有）
cat     打开文件显示内容
sudo   临时切换用户身份（root，管理员模式）
sudo su    	永久切换用户

touch 创建文件
mkdir  创建文件夹
cp   源文件名  拷贝文件名   文件拷贝
rm    删除文件   -r递归（子目录）  -f强制
rmdir 删除目录
mv   移动文件

## 终端操作与shell命令2
ctrl+c 打断操作

ifconfig  网络信息   -a
ifconfig 网卡名 up/down  打开/关闭   reload重启
ifconfig  网卡名  ip地址
ifconfig -h  帮助

reboot  重启系统
poweroff  关闭系统
man     系统帮助
例：man printf
sync   数据同步写入磁盘
find  查找文件  
find -name
grep  查找内容 -nr  -ir忽略大小写
du   文件夹大小查看
df   磁盘检查
gedit   打开（类似记事本）文件
ps   显示当前的系统进程
top  查看进程实时运行状态（任务管理器）
file  查看文件类型

## Ubuntu文件系统结构
根目录“/”

/bin  存放二进制可执行文件
/boot  linux内核、启动
/cdrom 光盘
/dev   设备驱动文件
/etc  配置文件
/home 用户主文件夹
/lib /lib64 库文件
/media  放置可插拔设备  u盘
/mnt   用户可使用的挂载点
/opt  可选的文件和程序存放目录
/proc  虚拟文件系统
/sbin   同为二进制可执行文件 一般为开机过程中需要的命令
/srv   服务相关目录
/sys  记录内核信息
/tmp  临时目录
/var  存放一些变化的文件，如日志文件
/usr  存放系统用户的相关文件

绝对路径与绝对路经
从“/”是绝对路径
.或./代表当前路径

## 磁盘管理

## linux链接文件/连接文件
符号连接（软连接）和硬连接（inode）
ln命令创建连接文件
ln[选项] 源文件  目标文件

## vim编辑器
a       在当前光标后转入输入模式
i        在光标前转入输入模式
esc   退出输入模式

:从指令模式进入底行模式
q   wq保存推出  q！不保存退出

输入模式——一般模式——命令模式

一般模式下：
dd  删除光标所在行  ndd删除掉光标所在及其下共n行
u   撤销上一步
.. 重复前一操作
yy 复制光标所在行  nyy
p复制到光标下一行  P复制到光标上一行

## linux C编程


































