c.backend = 'webkit'
root_dir = '/root/tree'
c.content.geolocation = 'ask'
config.load_autoconfig()
c.aliases['sd'] = 'config-source -c'
c.aliases['sr'] = 'config-source -c ~/.config/treeline/treeline-config.py'
config.bind('F', 'hint all tab-bg', mode='normal')
