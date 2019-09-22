
## stage
- download vim ftp://ftp.vim.org/pub/vim/unix/vim-8.1.tar.bz2
- install relase
	- yum install asciidoc docbook2X xmlto texinfo sgml2xml autoconf openjade -y
	- yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker -y
- cd git
- make configure
- ./configure --prefix=/usr/local/git
- make all doc
- make install install-doc install-html
- vim /etc/profile
	- export GIT_HOME=/usr/local/git
	- export PATH=$PATH:$GIT_HOME/bin
- source /etc/profile
