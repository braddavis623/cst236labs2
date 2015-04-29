from nose2.events import Plugin
from tests.ReqTracer import Requirements


class Lab3plugin(Plugin):
    configSection = 'requirements'

    def __init__(self):
        print "running"

    def stop_test_run(self, event):
        print "stopped"
