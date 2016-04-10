_computationalphysics_N2013301020101_


#第一次作业（安装）
安装狂蟒之灾，Linux与虚拟机均网络连接失败
#第二次作业（安装插件）
参考How to think like a computer scientist -- Learning with Python: Interactive Edition 2.0进行python语法练习
#第三次作业（语法练习）
做到LV2？，应该算是做到了。
  [作业](https://github.com/whuerZS/computationalphysics_N2013301020101/blob/master/EX1%20LV1-lv2.py) 
#作业列表
[第一章作业（第一次）](https://github.com/whuerZS/computationalphysics_N2013301020101/blob/master/Chapter1/%E7%AC%AC%E4%B8%80%E6%AC%A1%E4%BD%9C%E4%B8%9A.md)
#第一章作业（第二次）
####摘要：
选择第一章1.5题，两个不同的核可以相互衰变，验证了两核的个数最终达到平衡。
####背景介绍：
同样用欧拉法，在较小的时间间隔内取值，把数据制成列表并绘图。
####正文：
[此次作业链接](https://github.com/whuerZS/computationalphysics_N2013301020101/tree/master/Chapter1/Chapter1%EF%BC%88%E7%AC%AC%E4%BA%8C%E6%AC%A1%EF%BC%89)


选取初始参数：NA=100,NB=0,题中给定时间间隔tau=1s,选取合适步长为0.1,为使得图像均匀，总时间选择为t=4s。
得到的图形：


![绘图](https://raw.githubusercontent.com/whuerZS/computationalphysics_N2013301020101/master/Chapter1/Chapter1%EF%BC%88%E7%AC%AC%E4%BA%8C%E6%AC%A1%EF%BC%89/figure_1.png)

[数据](https://github.com/whuerZS/computationalphysics_N2013301020101/blob/master/Chapter1/Chapter1%EF%BC%88%E7%AC%AC%E4%BA%8C%E6%AC%A1%EF%BC%89/%E6%95%B0%E6%8D%AE.txt)


可从上面数据观察出两核个数最终在50左右波动，当把时间延长至t=13,发现粒子数在12.3s左右数目相同。


12.3 50.0000000001 49.9999999999;
12.4 50.0 50.0;
12.5 50.0 50.0;
12.6 50.0 50.0;
12.7 50.0 50.0;
12.8 50.0 50.0;
12.9 50.0 50.0;
13.0 50.0 50.0.
####结论：
当取足够大的时间时（t>12.3s),此步长下两种核的粒子数达到了平衡。








