# 常用命令收集

## 读取命令
- nl f1  读取文件f1，但是忽略空白行
'''linux
     1	asdfoiuu0234
     2	1 hello:world
     3	3453
       
       
     4	hello wmsj100 hello worls a  hello:wq
       
       
     5	asdfpiou
       
     6	waahello worldasdf
       
     7	oo9hello
       
     8	history | cut -c 8- | cut -d ' ' -f 1| sort | uniq -dc | sort -nr | head -n 10 > /home/wmsj100/Documents/git/linux/projec/historyRank/$(date +\%Y-\%m-\%d).top10
'''

## 提取html也没的内容
‘<b>This</b> is what <span style="text-decoration: underline;">I</span> meant. Understand?’
- sed 's/<[^>]*>//g' // 这样就可以了。
