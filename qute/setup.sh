#!/usr/bin/zsh
mkdir -p ~/.config/qutebrowser
ln -sf $0:a:h/config.py ~/.config/qutebrowser/
ln -sf $0:a:h/binds.py ~/.config/qutebrowser/
ln -sf $0:a:h/sessions ~/.local/share/qutebrowser/
