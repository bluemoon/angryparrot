from core.irc import Irc
from core.hooks import handle
from plugins import plugins

class Bot(object): # don't inherit from Irc, keeps things flat :D
    '''Instantiates Irc, loops over `Irc.conn.iqueue` and sends data through 
       `dispatch()`. Pass True if using SSL/TLS.
    '''

    def __init__(self, settings):
        self.plugins = settings['plugins']
        self.channels = settings['channels']
        self.irc = Irc(settings)
        self.cmd_prefix = settings['prefix']
        self._dispatch_events()

    def _dispatch_events(self):
        while True: # magic loop
            event = self.irc.events.get()
            sieve = handle(self, event) # this takes an event, and determines whether we should parse it as a command or a subscription
