---
title: ThreadPool
date: 2020-08-11 14:21:56
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# ThreadPool

## 概要

- 这是python中的线程池模块，可以通过这个模块来执行异步的任务

## 范例

```python
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed


class ThreadPool (object):
    def __init__(self):
        pass

    def get_data(self, page):
        sleep = random.randint (1, 10)
        time.sleep (sleep)
        print(f'task{page} finished')
        return sleep

    def start(self):
        with ThreadPoolExecutor(max_workers = 10) as t:
            all_task = [ t.submit(self.get_data, page) for page in range(1,11) ]

            for future in as_completed(all_task):
                data = future.result()
                print(f'main: {data}')

if __name__ == '__main__':
    tp = ThreadPool ()
    tp.start ()
```

## 参考

- [python threadpool](https://zhuanlan.zhihu.com/p/65638744)
