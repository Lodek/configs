source ~/.zshrc-arch
source ~/.zshfunc
source ~/.zshalias
source ~/.zshexports
source ~/.zshpaths
eval "$(direnv hook zsh)"

source /usr/share/fzf/completion.zsh
source /usr/share/fzf/key-bindings.zsh
source ~/.local/share/pickem/core.zsh
source ~/configs/zsh/pickem.zsh
. ~/configs/zsh/z.sh


[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

alias lo="tmux capture-pane -p -e | vim -c 'AnsiEsc' -"
