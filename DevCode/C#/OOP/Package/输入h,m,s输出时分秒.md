---
title: 输入h,m,s输出时分秒
date: 2016-08-16
tags: [C#]
categories: Language
---

```c#
    class Time
    {
        private int hour;
        private int minute;
        private int second;
        
        public int Hour
        {
            get
            {
                return hour;
            }
            set
            {
                hour = ((value >= 0 && value < 12) ? value : 0);
            }
        }
        public int Minute
        {
            get
            {
                return minute;
            }
            set
            {
                minute = ((value >= 0 && value < 60) ? value : 0);
            }
        }
        public int Second
        {
            get
            {
                return second;
            }
            set
            {
                second = ((value >= 0 && value < 60) ? value : 0);
            }
        }

        private void SetTime(int h, int m, int s)
        {
            Hour = h;
            Minute = m;
            Second = s;
        }

        public Time()
        {
            SetTime(0,0,0);
        }
        public Time(int hourValue)
        {
            SetTime(hourValue,0,0);
        }
        public Time(int hourValue, int minuteValue, int secondValue)
        {
            SetTime(hourValue, minuteValue, secondValue);
        }

        public string ToString24()
        {
            string outPut = Hour + ":" + Minute + ":" + Second;
            return outPut;
        }

        public string ToString12()
        {
            Hour = (Hour == 0 || Hour == 12 ? 12 : Hour % 12);
            string AMPM = (Hour < 12 ? "AM" : "PM");
            string output = Hour + ":" + Minute + ":" + Second + " " + AMPM;
            return output;
        }

    }
```

上面是封装的一个`Time`类库，下面是对它的调用

```c#
Time t1 = new Time(11,22,35);
string show = t1.ToString12();
```
