# 日期

- select current_date; // 获取当前日期
- select curdate(); // 获取当前日期
- select current_time; // 获取当前时间
- select now(); // 获取当前日期和时间

## 年龄
- 对于用户的信息，尤其是年龄不会进行存储，而是存储用户的出生年月日，进行计算获取。
- 因为如果数据库中存储了用户的年龄信息，那么到了明年，年龄信息就不准确了，

## timestampdiff 计算俩个日期的差值
- timestampdiff(year, birth, curdate()); 计算年龄，以出生日期和当前日期并且以年为单位的差值进行计算年龄。

