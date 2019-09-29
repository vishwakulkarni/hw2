from part1c.observerInterface import *

class ZooAnnouncer(Observer):

    def __init__(self, name):
        self.announceid = "Hi, this is the Zoo Announcer, "
        self.msg = None
        self.name = name

    def update(self, info):
        self.msg = self.announceid + self.name + '. '+ info
        print(self.msg)

    def getName(self):
        return self.name

    def __del__(self):
        print(self.name + " is deconstructed.")
