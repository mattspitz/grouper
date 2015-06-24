import time

from grouper.plugin import BasePlugin


class AnotherPlugin(BasePlugin):
    """ NOT TO BE CHECKED IN; just for testing """
    def start_request(self, request):
        start = time.time()
        print "GO GO GO22222"
        return start

    def finish_request(self, request, data):
        print "finish!!!!!!!!!", time.time() - data

    def user_created(self, user):
        print "CREATED!"
