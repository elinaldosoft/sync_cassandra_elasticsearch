#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
import sys, time
from daemon import Daemon
from sync import Sync
from config import CONF_DAEMON

class SycDaemon(Daemon):
        def run(self):
                while True:
                        Sync().syn_all()
                        time.sleep(CONF_DAEMON.get("LIMIT"))

if __name__ == "__main__":
    daemon = SycDaemon('/tmp/sync_daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
            sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)