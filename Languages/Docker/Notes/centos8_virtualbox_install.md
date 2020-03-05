---
title: centos8_virtualbox_install
date: 2020-03-05 07:30:27
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# centos8_virtualbox_install

## 概要

- 安装virtualbox的过程

## 安装

- `sudo yum install VirtualBox-6.1.x86_64` 开始下载和安装virtualbox
- 下载完成后会提示缺少一些库，需要单独安装，还有virtualbox kernel
- `sudo yum install gcc make perl`
- `sudo yum install kernel-devel kernel-devel-4.18.0-147.5.1.el8_1.x86_64`
- `sudo /sbin/vboxconfig` 重启和构建kernel
- 如果构建失败，就去看失败日志，`/var/log/vbox-setup.log`提示缺少文件，下载安装
- `sudo yum install elfutils-libelf-devel`
- `sudo /sbin/vboxconfig` 重启和构建kernel
```
[wmsj100@localhost ~]$ sudo /sbin/vboxconfig
vboxdrv.sh: Stopping VirtualBox services.
vboxdrv.sh: Starting VirtualBox services.
vboxdrv.sh: Building VirtualBox kernel modules.
```

## 步骤

```
[wmsj100@localhost Downloads]$ yum search virtualbox
Oracle Linux / RHEL / CentOS-8 / x86_64 - VirtualBox                                                                                 214  B/s | 181  B     00:00
Oracle Linux / RHEL / CentOS-8 / x86_64 - VirtualBox                                                                                 853  B/s | 1.7 kB     00:02
Importing GPG key 0x98AB5139:
 Userid     : "Oracle Corporation (VirtualBox archive signing key) <info@virtualbox.org>"
 Fingerprint: 7B0F AB3A 13B9 0743 5925 D9C9 5442 2A4B 98AB 5139
 From       : https://www.virtualbox.org/download/oracle_vbox.asc
Is this ok [y/N]: y
Oracle Linux / RHEL / CentOS-8 / x86_64 - VirtualBox                                                                                  52 kB/s |  66 kB     00:01
Last metadata expiration check: 0:00:01 ago on Thu 05 Mar 2020 07:21:48 AM CST.
================================================================ Name & Summary Matched: virtualbox =================================================================
VirtualBox-5.2.x86_64 : Oracle VM VirtualBox
VirtualBox-6.0.x86_64 : Oracle VM VirtualBox
VirtualBox-6.1.x86_64 : Oracle VM VirtualBox
[wmsj100@localhost Downloads]$ sudo yum install VirtualBox-6.1.x86_64
Last metadata expiration check: 0:02:46 ago on Thu 05 Mar 2020 07:19:26 AM CST.
Dependencies resolved.
=====================================================================================================================================================================
 Package                                      Architecture                    Version                                      Repository                        Size
=====================================================================================================================================================================
Installing:
 VirtualBox-6.1                               x86_64                          6.1.4_136177_el8-1                           virtualbox                       94 M
Installing dependencies:
 pcre2-utf16                                  x86_64                          10.32-1.el8                                  base                             228 k
 SDL                                          x86_64                          1.2.15-36.el8_1                              AppStream                        218 k
 qt5-qtbase                                   x86_64                          5.11.1-7.el8                                 AppStream                        3.3 M
 qt5-qtbase-common                            noarch                          5.11.1-7.el8                                 AppStream                        39 k
 qt5-qtbase-gui                               x86_64                          5.11.1-7.el8                                 AppStream                        6.0 M
 qt5-qtx11extras                              x86_64                          5.11.1-2.el8                                 AppStream                        34 k
 xcb-util-image                               x86_64                          0.4.0-9.el8                                  AppStream                        21 k
 xcb-util-keysyms                             x86_64                          0.4.0-7.el8                                  AppStream                        16 k
 xcb-util-renderutil                          x86_64                          0.3.9-10.el8                                 AppStream                        19 k
 xcb-util-wm                                  x86_64                          0.4.1-12.el8                                 AppStream                        32 k

Transaction Summary
=====================================================================================================================================================================
Install  11 Packages

Total size: 104 M
Total download size: 94 M
Installed size: 237 M
Is this ok [y/N]: y
Downloading Packages:
[SKIPPED] pcre2-utf16-10.32-1.el8.x86_64.rpm: Already downloaded
[SKIPPED] SDL-1.2.15-36.el8_1.x86_64.rpm: Already downloaded
[SKIPPED] qt5-qtbase-5.11.1-7.el8.x86_64.rpm: Already downloaded
[SKIPPED] qt5-qtbase-common-5.11.1-7.el8.noarch.rpm: Already downloaded
[SKIPPED] qt5-qtbase-gui-5.11.1-7.el8.x86_64.rpm: Already downloaded
[SKIPPED] qt5-qtx11extras-5.11.1-2.el8.x86_64.rpm: Already downloaded
[SKIPPED] xcb-util-image-0.4.0-9.el8.x86_64.rpm: Already downloaded
[SKIPPED] xcb-util-keysyms-0.4.0-7.el8.x86_64.rpm: Already downloaded
[SKIPPED] xcb-util-renderutil-0.3.9-10.el8.x86_64.rpm: Already downloaded
[SKIPPED] xcb-util-wm-0.4.1-12.el8.x86_64.rpm: Already downloaded
(11/11): VirtualBox-6.1-6.1.4_136177_el8-1.x86_64.rpm                                                                                277 kB/s |  94 MB     05:49
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                276 kB/s |  94 MB     05:49
warning: /var/cache/dnf/virtualbox-251a95df6cac77a1/packages/VirtualBox-6.1-6.1.4_136177_el8-1.x86_64.rpm: Header V4 DSA/SHA1 Signature, key ID 98ab5139: NOKEY
Oracle Linux / RHEL / CentOS-8 / x86_64 - VirtualBox                                                                                 851  B/s | 1.7 kB     00:02
Importing GPG key 0x98AB5139:
 Userid     : "Oracle Corporation (VirtualBox archive signing key) <info@virtualbox.org>"
 Fingerprint: 7B0F AB3A 13B9 0743 5925 D9C9 5442 2A4B 98AB 5139
 From       : https://www.virtualbox.org/download/oracle_vbox.asc
Is this ok [y/N]: y
Key imported successfully
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                        1/1 Installing       : xcb-util-wm-0.4.1-12.el8.x86_64                                                                                                            1/11
  Running scriptlet: xcb-util-wm-0.4.1-12.el8.x86_64                                                                                                        1/11
  Installing       : xcb-util-renderutil-0.3.9-10.el8.x86_64                                                                                                2/11
  Running scriptlet: xcb-util-renderutil-0.3.9-10.el8.x86_64                                                                                                2/11
  Installing       : xcb-util-keysyms-0.4.0-7.el8.x86_64                                                                                                    3/11
  Running scriptlet: xcb-util-keysyms-0.4.0-7.el8.x86_64                                                                                                    3/11
  Installing       : xcb-util-image-0.4.0-9.el8.x86_64                                                                                                      4/11
  Running scriptlet: xcb-util-image-0.4.0-9.el8.x86_64                                                                                                      4/11
  Installing       : SDL-1.2.15-36.el8_1.x86_64                                                                                                             5/11
  Running scriptlet: SDL-1.2.15-36.el8_1.x86_64                                                                                                             5/11
  Installing       : pcre2-utf16-10.32-1.el8.x86_64                                                                                                         6/11
  Installing       : qt5-qtbase-common-5.11.1-7.el8.noarch                                                                                                  7/11
  Running scriptlet: qt5-qtbase-5.11.1-7.el8.x86_64                                                                                                         8/11
  Installing       : qt5-qtbase-5.11.1-7.el8.x86_64                                                                                                         8/11
  Running scriptlet: qt5-qtbase-5.11.1-7.el8.x86_64                                                                                                         8/11
  Installing       : qt5-qtbase-gui-5.11.1-7.el8.x86_64                                                                                                     9/11
  Running scriptlet: qt5-qtbase-gui-5.11.1-7.el8.x86_64                                                                                                     9/11
  Installing       : qt5-qtx11extras-5.11.1-2.el8.x86_64                                                                                                    0/11
  Running scriptlet: VirtualBox-6.1-6.1.4_136177_el8-1.x86_64                                                                                               1/11
  Installing       : VirtualBox-6.1-6.1.4_136177_el8-1.x86_64                                                                                               1/11
  Running scriptlet: VirtualBox-6.1-6.1.4_136177_el8-1.x86_64                                                                                               1/11

Creating group 'vboxusers'. VM users must be member of that group!

This system is currently not set up to build kernel modules.
Please install the gcc make perl packages from your distribution.
Please install the Linux kernel "header" files matching the current kernel
for adding new hardware support to the system.
The distribution packages containing the headers are probably:
    kernel-devel kernel-devel-4.18.0-147.5.1.el8_1.x86_64
This system is currently not set up to build kernel modules.
Please install the gcc make perl packages from your distribution.
Please install the Linux kernel "header" files matching the current kernel
for adding new hardware support to the system.
The distribution packages containing the headers are probably:
    kernel-devel kernel-devel-4.18.0-147.5.1.el8_1.x86_64

There were problems setting up VirtualBox.  To re-start the set-up process, run
  /sbin/vboxconfig
as root.  If your system is using EFI Secure Boot you may need to sign the
kernel modules (vboxdrv, vboxnetflt, vboxnetadp, vboxpci) before you can load
them. Please see your Linux system's documentation for more information.

  Verifying        : pcre2-utf16-10.32-1.el8.x86_64                                                                                                         1/11
  Verifying        : SDL-1.2.15-36.el8_1.x86_64                                                                                                             2/11
  Verifying        : qt5-qtbase-5.11.1-7.el8.x86_64                                                                                                         3/11
  Verifying        : qt5-qtbase-common-5.11.1-7.el8.noarch                                                                                                  4/11
  Verifying        : qt5-qtbase-gui-5.11.1-7.el8.x86_64                                                                                                     5/11
  Verifying        : qt5-qtx11extras-5.11.1-2.el8.x86_64                                                                                                    6/11
  Verifying        : xcb-util-image-0.4.0-9.el8.x86_64                                                                                                      7/11
  Verifying        : xcb-util-keysyms-0.4.0-7.el8.x86_64                                                                                                    8/11
  Verifying        : xcb-util-renderutil-0.3.9-10.el8.x86_64                                                                                                9/11
  Verifying        : xcb-util-wm-0.4.1-12.el8.x86_64                                                                                                        0/11
  Verifying        : VirtualBox-6.1-6.1.4_136177_el8-1.x86_64                                                                                               1/11

Installed:
  VirtualBox-6.1-6.1.4_136177_el8-1.x86_64    pcre2-utf16-10.32-1.el8.x86_64             SDL-1.2.15-36.el8_1.x86_64             qt5-qtbase-5.11.1-7.el8.x86_64
  qt5-qtbase-common-5.11.1-7.el8.noarch       qt5-qtbase-gui-5.11.1-7.el8.x86_64         qt5-qtx11extras-5.11.1-2.el8.x86_64    xcb-util-image-0.4.0-9.el8.x86_64
  xcb-util-keysyms-0.4.0-7.el8.x86_64         xcb-util-renderutil-0.3.9-10.el8.x86_64    xcb-util-wm-0.4.1-12.el8.x86_64

Complete!
```

## 参考

