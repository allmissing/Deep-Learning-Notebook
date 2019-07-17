# Deep-Learning-Notebook

## 1.学习资源

摘自https://blog.csdn.net/opengel/article/details/79773621

（1）李宏毅机器学习(2017)
https://www.bilibili.com/video/av10590361?from=search&seid=456509998694502607

（2）李宏毅深度学习(2017)
https://www.bilibili.com/video/av9770302?from=search&seid=456509998694502607

（3）李宏毅2017 深度学习GAN课程
https://www.bilibili.com/video/av18603573?from=search&seid=456509998694502607

（4）李宏毅深度学习合辑 Advanced Topics in Deep Learning
https://www.bilibili.com/video/av19145699?from=search&seid=456509998694502607

（5）李宏毅 深度学习理论 Deep Learning Theory
https://www.bilibili.com/video/av20961661?from=search&seid=4753772315676173168

## 2.使用tensorflow遇到的问题
#### (1)训练过程损失一直为nan：数据中包含空值、缺失值

#### (2)tensorboard必须在tensorflow运行后再打开，否则会无法理解报错
顺序使先写好tensorflow程序并运行，然后在终端启动tensorboard，启动后无法在修改summary部分，否则会报如下错误，无法理解：

        InvalidArgumentError: You must feed a value for placeholder tensor 'Network/input' with dtype float and shape [?,25]

## 3.使用Anaconda出现的问题
#### anaconda prompt快捷方式从开始中消失了怎么办？
（1） 第一种方式（不一定好使）：在cmd中切换至‘D:\ProgramData\Anaconda3\Lib’文件夹内，执行python _nsis.py mkmenus 

（2） 第二种方式（https://blog.csdn.net/ziv_jiaung/article/details/84196557）：
随便复制一个快捷方式，修改目标成这样：  

    C:\Windows\System32\cmd.exe "/K" D:\ProgramData\Anaconda3\Scripts\activate.bat D:\ProgramData\Anaconda3  

上面包括三部分：第一部分指向系统的命令行exe文件，第二部分指向安装的anaconda目录下相应环境的激活批处理文件activate.bat，第三部分为anaconda对应环境的根目录

我是为了使用tensorboard，它只安装在了之前创建的一个叫python35的环境中，所以构造的链接如下：

    C:\Windows\System32\cmd.exe "/K" D:\ProgramData\Anaconda3\envs\python35\Scripts\activate.bat D:\ProgramData\Anaconda3\envs\python35



