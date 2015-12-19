set sw=2
set ts=8
set sts=2
set aw
set ai
set sm
set notagbsearch
set expandtab
set incsearch 
set notagbsearch
if filereadable('.local.vim')
  so .local.vim
endif
map q !}fmt
map!  
map [24~ :!sh ./go
map <F1> :bnext
map <F2> :n#
map <F5> ]s
map <F6> zg
map <F7> :cn
set makeprg=sh\ go
" map ` :make
map ` :!sh go
nnoremap <silent> <F8> :TlistToggle<CR>
set viminfo='10,\"100,:20,%,n~/.viminfo
" set tags=../src/TAGS
let loaded_matchparen = 1
au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal g'\"" | endif
au BufReadPost *.py setlocal sw=4 ts=8 sts=4
au BufReadPost *.[sS] setlocal sw=8 ts=8 sts=8
au BufReadPost *.asm setlocal sw=8 ts=8 sts=8
au BufNewFile,BufReadPost *.sl setlocal filetype=forth
au BufNewFile,BufReadPost *.sl setlocal iskeyword=!,@,33-35,%,$,38-64,A-Z,91-96,a-z,123-126,128-255
au BufNewFile,BufReadPost *.sl setlocal sw=4 ts=8
au BufNewFile,BufReadPost *.fs setlocal filetype=forth
au BufNewFile,BufReadPost *.fs setlocal iskeyword=!,@,33-35,%,$,38-64,A-Z,91-96,a-z,123-126,128-255
au BufNewFile,BufReadPost *.fs setlocal sw=4 ts=4 sts=4
au BufNewFile,BufReadPost *.fs syntax off
au BufNewFile,BufReadPost *.fs highlight Comment term=standout cterm=bold ctermfg=3
au! Syntax forth source $HOME/.vim/forth.vim
syntax off
nnoremap <F9> "=strftime("(                                            JCB %H:%M %m/%d/%y)\n")<CR>P3<Bar>R
map <F8> :r !xclip -o
set wildignore=*.o,*.bin*,*.jpg,*.png,*.pdf,*.exe,*.a
set t_Co=256
" local