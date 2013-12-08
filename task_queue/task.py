# threading queue test
# Priyaank Choubey - mail@priyaank.com

#
#   Task.
#
#   It's an abstract base class.
#   From which you have to derive your own task classes by overriding the run()-method
#
#   Example:
#
#   class SimpleTask(Task):
#
#       def run(self):
#           print self.name()
#
#

class Task(object):
    def __init__(self):
        print self.__name__

    def run(self):
        print "Start Processing Task"

