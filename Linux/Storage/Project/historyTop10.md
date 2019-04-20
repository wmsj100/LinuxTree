# 收集history的top10命令

- wget http://labfile.oss.aliyuncs.com/courses/1/data1 获取到数据

- cat data1 | cut -c 8- | cut -d ' ' -f 1 | sort | uniq -dc | sort -nr | head -n 10 > result
