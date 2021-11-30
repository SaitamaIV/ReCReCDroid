​        

## 使用VirtualBox镜像运行ReCDroid

### 声明

-功能模块交互部分在工具理解ppt里。

### 准备工作

- 准备一台拥有以下推荐配置的台式计算机：32GB内存、8内核cpu、超过50GB的可用磁盘。
- 下载一个24GBVitualBox镜像(下载地址：https://drive.google.com/file/d/1vM6FiqmctBh0EaxW4MtvIFxwsGx9DfT9/view?usp=sharing).镜像的根密码是 `rec_xxx`. 
- 使用VB(we use 5.1.38) 安装VirtualBox镜像。

### 运行RecDroid

1. 打开 virtualbox 镜像
2. 启动一个安卓虚拟机， 等待几分钟直到完全开启。
```sh
   emulator -avd avd -wipe-data
```
3. 进入Artifact文件夹，里面有25个bug报告文件夹，并且有app的名字
```sh
   cd ~/Artifact-Evaluation/1.worked-in-this-VM/Android-4.4.2
   ls
```
 结果:
```sh
10.olam1_'_s            17.transistor_s     24.obdreader_s  6.acv_s
11.olam_space_s         18.zom              26.odk          7.anymemo_deafult_s
12.fastadaper_s         19.Pix-Art-share_s  27.k-9_s        8.anymemo_menu_s
13.librenews_refresh_s  1.newsblur_s        2.markor_s      9.nodepad_s
14.librenews_back_s     20.Pix-Art_s        3.birthdroid_s
15.librenews_s          22.ventriloid_s     4.carreport_s
16.smssync_s            23.news_s           5.opensudoku_s
```
4. 打开一个故障报告文件夹, 例如1.newsblur_s.
```sh
   cd 1.newsblur_s
```

5. 运行名为 "percerun_`AppName`.sh"的故障重现过程， 生成重现脚本。 
```sh
   ./percerun_newsblur.sh
```
如果显示"matchcrash" 和 "execution time"请耐心等待。 在遇到某些困难的bug时ReCDroid的运行时长可能会超过1个小时。

6. 运行 "runCrash_`AppName`.sh ".重现崩溃过程，如：
```sh
   ./runCrash_newsblur.sh
```


7. 在您想要测试另一个bug报告之前，请关闭所有终端和模拟器。

### 故障检修

如果在执行ReCDroid期间看到出现“falure”信息，请忽略。

在具有低性能硬件的系统上，ReCDroid可能无法再现VirtualBox中某些错误报告的崩溃。这是因为如果VituralBox镜像在较差的硬件基础上运行，模拟器的反应速度可能会非常慢，单击事件的响应时间可能会超过3秒，这超过了ReCDroid指定的最大响应时间。在这种情况下，ReCDroid将终止重现过程。（ReCDroid在动态探索算法中设置了响应时间限制）

## 在物理计算机上运行ReCDroid

值得注意的是，由于以下原因，在VirtualBox ubuntu系统中运行Android emulator并不理想。首先，VirtualBox中的模拟器比物理机器慢得多。此外，一些使用资源消耗型android SDK版本的模拟器可能会产生启动错误，如android 7.0.0，或者根本无法启动。（本人亲身尝试过，确实不行，Android7.0.0模拟器会爆一个奇怪的未知错误） 


##  ReCDroid生成的结果文件说明:

举一个bug报告文件夹`1.newsblur_s/` 为例：

### 输入文件

- Bug report: `nlpBugReport/percentbugreport`.

- Input APK: `newsblur-v6.10_debug.apk`.

- Robotium file: `BFS_androidtester.apk`. APK的包名和MainActivityName应该在编译前声明。

- Shell file: `percerun_newsblur.sh`. APK的包名和MainActivityName应该在里面声明。

### 输出文件

- NLP result: `middleResults/nlp.xml`.

- 探索后的事件流图: `middleResults/record.xml`.

- 可以重现崩溃的可执行脚本，该脚本有一个事件序列：`middleResults/run.xml`.

## 例子:

A bug report in https://github.com/milesmcc/LibreNews-Android/issues/22, whose description is as follows:

- Install v1.4 from FDroid.
- Launch app.
- Disable automatically refresh
- Change server address to an invalid one, e.g., xxyyzz.
- Click refresh.


###  用例输出:

run.xml (i.e., reproducing script)中的输出流如下: 

```
<step id="1"><currentClass>1</currentClass><subId>1</subId>...</step>
 
<step id="2"><currentClass>2</currentClass><subId>5</subId>...</step>

<step id="3"><currentClass>3</currentClass><subId>4</subId>...</step>

<step id="4"><currentClass>4</currentClass><subID>1</subID>...</step>

<step id="5"><currentClass>4</currentClass><subId>3</subId>...</step>

<step id="6"><currentClass>3</currentClass><subId>1</subId>...</step>
```

其中currentClass是安卓应用程序中的某个页面（吐槽一下命名）；每个页面都有一个UI列表，subID即表示currentClass页面中的某个组件的编号。当然也会有反应操作的信息等其他参数。

## 此存储库中包含的其他内容

- 评估结果：除了论文里给出的评估结果外，开发人员还提供了更详细的评估结果，并且提供了实验中使用的一组APK 
- bug报告分析: 开发人员抓取了10000多个Android bug报告，总结了22条NLP语法规则
- nlp patterns: We use the summarized rules to build NLP patterns,  which can analyzing the bug reports.
- 源代码: Robotium源代码可以支持版本低于Android 6.0的Android SDK。UIAutomator源代码可以支持版本高于或等于Android 6.0的Android SDK。


