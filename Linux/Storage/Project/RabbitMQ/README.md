# RabbitMQ

- 是一个由erlang开发的AMQP 高级消息队列协议的开源消息代理软件。
- Rabbitmq是一个消息代理，它的核心原理非常简单：接收和发送消息。

## 生产者消费者问题 
- 也称为有限缓冲为题：
- 是一个多线程同步问题的经典案例
- 问题描述了俩个共享固定大小缓冲区的线程--即所谓的生产者和消费者
- 生产者主要负责生产一定量的数据行道缓冲区中，然后重复此过程
- 消费者在缓冲区中消费数据
- 该问题的关键是保证生产者在缓冲区满的时候不注入数据；消费者不再缓冲区空的时候消费数据。

- 生产者 产生消息并发送到消息队列中的程序
- 队列： 是一种特殊的线性表，用于存放消息。
- 队列没有任何限制，要存储多少消息都可以。是一个无限缓冲
- 多个生产者可以把消息发送给一个队列
- 多个消费者可以从一个队列中获取数据

- 需要指出的是生产者/ 消费者/ 代理一般不会放置在同一个设备上；