filetype off  " required!

    set rtp+=~/.vim/bundle/vundle/
    call vundle#rc()

    " let Vundle manage Vundle
    " required!
    Bundle 'gmarik/vundle'

    " My Bundles here:
    "
    " original repos on github
    Bundle 'tpope/vim-fugitive'
    Bundle 'rstacruz/sparkup', {'rtp': 'vim/'}
    Bundle 'tpope/vim-rails.git'
    Bundle 'scrooloose/nerdtree'
    Bundle 'kien/ctrlp.vim'
    Bundle 'c.vim'
    Bundle 'msanders/snipmate.vim'
    Bundle 'mileszs/ack.vim'
    Bundle 'Shougo/neocomplcache.vim'
    Bundle 'Townk/vim-autoclose'
    "Bundle 'Valloric/YouCompleteMe' 和neocomplache 功能一样，都是提示的
    Bundle 'Lokaltog/vim-powerline'
    " vim-scripts repos
    Bundle 'L9'
    Bundle 'FuzzyFinder'
    " non github repos
    Bundle 'git://git.wincent.com/command-t.git'
    " git repos on your local machine (ie. when working on your own plugin)
    " ...

    filetype plugin indent on     " required!
    "
    " Brief help
    " :BundleList          - list configured bundles
    " :BundleInstall(!)    - install(update) bundles
    " :BundleSearch(!) foo - search(or refresh cache first) for foo
    " :BundleClean(!)      - confirm(or auto-approve) removal of unused bundles
    "
    " see :h vundle for more details or wiki for FAQ
    " NOTE: comments after Bundle command are not allowed..

    " NERDTree config
    map <F2> :NERDTreeToggle<CR>
    let NERDTreeDirArrows=0
    autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") &&  b:NERDTreeType == "primary") | q | endif

    "neocomplache config
    let g:neocomplcache_enable_at_startup = 1
    let g:neocomplcache_force_overwrite_completefunc = 1

    "other config
    set nu
    set mouse=a
    set tabstop=2
    let mapleader = ","
    let g:mapleader = ","
    map Y "+y
    map P "+p  ""

    "easymotion
    let g:EasyMotion_leader_key = '<Leader>'

    "powerline config
    set mouse=a
    set laststatus=2               
    set t_Co=256
    set encoding=utf-8
    set fillchars+=stl:\ ,stlnc:\
    set nohlsearch
    noremap <Up>    <Nop>
    noremap <Down>  <Nop>
    noremap <Left>  <Nop>
    noremap <Right> <Nop>
    "
    "" taglist
    "
    let Tlist_Show_One_File=1    "只显示当前文件的tags
    let Tlist_WinWidth=40        "设置taglist宽度
    let Tlist_Exit_OnlyWindow=1  "tagList窗口是最后一个窗口，则退出Vim
    let Tlist_Use_Right_Window=1 "在Vim窗口右侧显示taglist窗口
    " highlight CursorLine guibg=lightblue guifg=black ctermbg=lightgray ctermfg=black
    " highlight CursorColumn guibg=lightblue ctermbg=lightgray guifg=black ctermfg=black
    set cursorline
    hi CursorLine   cterm=NONE ctermbg=lightgray ctermfg=black guibg=black guifg=lightblue
    set cursorcolumn
    hi CursorColumn cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
    "  fix the bug mac delete button do not work
    set backspace=2
    " 光标停留在上次离开的位置
    au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif

