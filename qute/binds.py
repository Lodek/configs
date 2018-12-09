config.bind('pp', 'open -t -- {clipboard}')
config.bind('Pp', 'open -- {clipboard}')
config.bind('<Ctrl-d>', 'tab-close')
config.bind('<d>', 'scroll-page 0 0.6')
config.bind('<u>', 'scroll-page 0 -0.6')
config.bind('<Ctrl-u>', 'undo')
config.bind('<Shift-f>', 'hint all tab-bg')

c.aliases['l'] = 'session-load'
