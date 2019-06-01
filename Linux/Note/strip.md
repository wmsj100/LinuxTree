---
title: strip
date: 2019-06-01 08:15:19 Saturday
modify:
tag: [strip]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# strip

## 概述
- 多用来给C的二进制文件脱衣服，即删除多余的字符信息，
- 通过这个命令可以很明显的减少可执行文件的尺寸

## 用法
- strop a.out

## 范例
- file a.out
	a.out: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, for GNU/Linux 3.2.0, BuildID[sha1]=857a62a8fb494484daab83a94df20febfacb7cbd, not stripped
- nm a.out
	pi@raspberrypi:~/Github/study_C/mk_test1 $ nm a.out
    U abort@@GLIBC_2.4
	0002102c B __bss_end__
	0002102c B _bss_end__
	00021028 B __bss_start
	00021028 B __bss_start__
	00010350 t call_weak_fn
	00021028 b completed.10395
	00021020 D __data_start
	00021020 W data_start
	00010374 t deregister_tm_clones
	000103dc t __do_global_dtors_aux
	00020f10 t __do_global_dtors_aux_fini_array_entry
	00021024 D __dso_handle
	00020f18 d _DYNAMIC
	00021028 D _edata
	0002102c B _end
	0002102c B __end__
	000104c0 T _fini
	00010404 t frame_dummy
	00020f0c t __frame_dummy_init_array_entry
	000104e4 r __FRAME_END__
	00021000 d _GLOBAL_OFFSET_TABLE_
	         w __gmon_start__
	000102c4 T _init
	00020f10 t __init_array_end
	00020f0c t __init_array_start
	000104c8 R _IO_stdin_used
	00020f14 d __JCR_END__
	00020f14 d __JCR_LIST__
	000104bc T __libc_csu_fini
	0001045c T __libc_csu_init
	          U __libc_start_main@@GLIBC_2.4
	0001043c T main
	U puts@@GLIBC_2.4
	000103a4 t register_tm_clones
	00010314 T _start
	00021028 D __TMC_END__
- ll -h a.out # -rwxr-xr-x 1 pi pi 8.0K Jun  1 08:17 a.out
- strip a.out
- file a.out
	a.out: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, for GNU/Linux 3.2.0, BuildID[sha1]=857a62a8fb494484daab83a94df20febfacb7cbd, stripped
- nm a.out #nm: a.out: no symbols
## 参考
- []()

