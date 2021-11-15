" Neovim configuration file
" Author: Maarten Bruyninx

"Options
syntax on
set mouse=a
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set relativenumber
set number
set nohlsearch
set hidden
set noerrorbells
set nowrap
set smartcase
set ignorecase
set noswapfile
set nobackup
set undofile
set undodir=~/.config/nvim/undodir
set incsearch
set scrolloff=8
set noshowmode
set signcolumn=yes
set termguicolors
set clipboard+=unnamedplus
set encoding=UTF-8
set completeopt-=preview
set pyx=3

" Plugins
call plug#begin('~/.vim/plugged')
    "Plug 'neovim/nvim-lspconfig'
    "Plug 'onsails/lspkind-nvim'
    "Plug 'glepnir/lspsaga.nvim'
    Plug 'simrat39/symbols-outline.nvim'
    Plug 'nvim-lua/popup.nvim'
    Plug 'nvim-lua/plenary.nvim'
    Plug 'nvim-telescope/telescope.nvim'
    Plug 'nvim-telescope/telescope-fzy-native.nvim'
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
    Plug 'nvim-treesitter/playground'
    Plug 'kyazdani42/nvim-web-devicons'
    Plug 'ryanoasis/vim-devicons'
    Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
    Plug 'preservim/nerdtree'
    Plug 'sbdchd/neoformat'
    Plug 'arcticicestudio/nord-vim'
    Plug 'ap/vim-css-color'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'romgrk/barbar.nvim'
    Plug 'nvim-lualine/lualine.nvim'
    Plug 'psliwka/vim-smoothie'
call plug#end()

colorscheme nord

" Remaps
let mapleader = " "
nnoremap <leader>ts :lua require('telescope.builtin').grep_string({search = vim.fn.input("Grep For: ")})<CR>

" >> Telescope bindings
" most recently used files
nnoremap <leader>tr <cmd>lua require'telescope.builtin'.oldfiles{}<CR>

" find buffer
nnoremap ; <cmd>lua require'telescope.builtin'.buffers{}<CR>

" find in current buffer
nnoremap <leader>/ <cmd>lua require'telescope.builtin'.current_buffer_fuzzy_find{}<CR>

" bookmarks
nnoremap <leader>' <cmd>lua require'telescope.builtin'.marks{}<CR>

" git files
nnoremap <leader>tf <cmd>lua require'telescope.builtin'.git_files{}<CR>

" all files
nnoremap <leader>ta <cmd>lua require'telescope.builtin'.find_files{}<CR>

" ripgrep like grep through dir
nnoremap <leader>rg <cmd>lua require'telescope.builtin'.live_grep{}<CR>


"nnoremap <leader>h :wincmd h<CR>
"nnoremap <leader>j :wincmd j<CR>
"nnoremap <leader>k :wincmd k<CR>
"nnoremap <leader>l :wincmd l<CR>

nnoremap <leader>gd :call CocActionAsync('jumpDefinition')<CR>

" Move to previous/next
nnoremap <leader><TAB> :BufferNext<CR>
" Re-order to previous/next
nnoremap <leader>h :BufferMovePrevious<CR>
nnoremap <leader>l :BufferMoveNext<CR>
" Goto buffer in position...
nnoremap <leader>1 :BufferGoto 1<CR>
nnoremap <leader>2 :BufferGoto 2<CR>
nnoremap <leader>3 :BufferGoto 3<CR>
nnoremap <leader>4 :BufferGoto 4<CR>
nnoremap <leader>5 :BufferGoto 5<CR>
nnoremap <leader>6 :BufferGoto 6<CR>
nnoremap <leader>7 :BufferGoto 7<CR>
nnoremap <leader>8 :BufferGoto 8<CR>
nnoremap <leader>9 :BufferLast<CR>

nnoremap <leader>x :BufferClose<CR>

" Nerd Tree
nnoremap <leader>nt :NERDTreeToggle<CR>
nnoremap <leader>nf :NERDTreeFind<CR>
let g:NERDTreeDirArrowExpandable="+"
let g:NERDTreeDirArrowCollapsible="-"
let NERDTreeMinimalUI=1

source $HOME/.config/nvim/plug-config/coc.vim

lua require('evil')
