# Crawler
### 最近学了点爬虫的小知识, 感觉有个requests库好像很腻害的样子：
楼上小孩要高考了，我入学前正好要学python，就想着做个爬虫程序试试，
于是边在网上查资料找博客，边看了点廖雪峰的教程和《python入门到精通的教程》了解了爬虫的基本知识，这个小程序只用了requests库
主要想法如下:
1. 确定爬虫目标网站: 高考填报志愿网
2. 邻居家小孩只想读医，所以只想看医科大学,所以现在上述网站上搜罗所有医科专业
3. 根据医科专业的集合搜罗所有开设了医科专业大学的名字和网站id，形成大学集合
4. 根据大学集合搜罗近三年的最低录取分数线

### 难点解析:
1. 这个爬虫程序没有什么技术上的难点，也不复杂，属于抛砖引玉，管中窥豹的类型，但是鉴于刚刚开始学习，感觉做成这样也差不多了（毕竟现学现用）
2. 最开始分析网站的请求流很麻烦，需要通过浏览器的调试工具来找到想要的请求去模拟，即使这样,由于本人能力有限，也没有找到包含网站所有信息的请求链接
3. 找到的链接有的是明文json有的进行了加密和访问核对合法性，我只能对明文的json处理，后者不知道怎么处理，期待后期学习
4. 没有使用ip代理，也没有多线程分时分部分段跑程序，网站经常会在我跑程序的时候拒绝我的访问产生timeou，这个后期也要解决(不然跑一次的成功率太低了)
5. 综合上述因素，只找到了大学近三年省录取最低分数，没有具体到专业和更长的时间跨度（每个省份的ID是不一样的，后期要筛选一下）
6. 生成了两个xls文件，result.xls是第一次跑的结果，有问题的地方在于：前期分析的时候有两个分数，我以为一个是最高分一个是最低分（不过两个分差不大，20分以内），
   结果后期校验好像不是这样的，但是又不想改程序重新跑一遍了，原因在于上面的第4点了，于是写了个文件处理程序file_change.py，把两个分数中的高分取了出来，作为
   当年的最低分。
   
### 后期展望：
1. 有一说一，感觉爬虫还是很有意思的，而且个人感觉很有用
2. 以后再b站上多学点爬虫的库和框架，同时学习一下pyhon绘图库Pandas啥的，还有操作excel的库，方便结果可视化
3. 真想成为一个数据分析师，老友记里的chandler一样
