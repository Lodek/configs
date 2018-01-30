c.backend = 'webkit'
c.content.geolocation = 'ask'
config.load_autoconfig()

c.aliases['sd'] = 'config-source -c'
c.aliases['sr'] = 'config-source -c ~/.config/qutebrowser/treeline-config.py'
c.aliases['f'] = 'spawn -u ./favorites.sh'
c.aliases['w'] = 'spawn -u ./save-session.sh'

config.bind('f', 'spawn -u ./hint.py -t {url} ;; hint links userscript ./hint.py', mode='normal')
config.bind('F', 'spawn -u ./rapid.py {url} ;; hint links userscript ./rapid.py', mode='normal')
config.bind('<', 'set-cmd-text -s :spawn --userscript ./open.py -t root ', mode='normal')
config.bind('>', 'set-cmd-text -s :spawn --userscript ./open.py -t {url} ', mode='normal')  
