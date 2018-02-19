Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> raw_input('year: ')[3]
year: 2005
'5'
>>> "sssd"[3]
'd'
>>> 15*['sd']
['sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd', 'sd']
>>> 3*['sd
   
SyntaxError: EOL while scanning string literal
>>> 3*['ds']
['ds', 'ds', 'ds']
>>> ending=['st
	
SyntaxError: EOL while scanning string literal
>>> endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 17 * ['th'] + ['st']
>>> endings
['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'st']
>>> year = raw_input("Year: ")
Year: 2017
>>> year
'2017'
>>> month = raw_input("month: ")
month: 05
>>> month
'05'
>>> int(month)
5
>>> day = raw_input("day: ")
day: 09
>>> month_num = int(month)
>>> month_num
5
>>> day_num = int(day)
>>> day_num
9
>>> months = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
>>> month_name = months[month_num - 1]
>>> month_name
'\xce\xe5\xd4\xc2'
>>> months = ['january', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
>>> month_name = months[month_num - 1]
>>> month_name
'May'
>>> day_name = endings[day_num - 1]
>>> day_name
'th'
>>> day_name += day_num - 1;

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    day_name += day_num - 1;
TypeError: cannot concatenate 'str' and 'int' objects
>>> day_name += str(day_num - 1)
>>> day_name
'th8'
>>> day_name = day + endings[day_num - 1]
>>> day_name
'09th'
>>> print month_name + ' ' + day_name + ', ' + year
May 09th, 2017
>>> 
