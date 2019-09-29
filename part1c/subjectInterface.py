from abc import ABC, abstractmethod

"""
This module defines the interface for the subject (i.e. Observable, what is being observed) with an abstract class.
It is inherited by zookeeper.SubjectConcrete to create a concrete subject.

This script was created with reference to slides "OOAD CL12-L14 Decorator" and the example here: 
http://www.djangospin.com/design-patterns-python/observer/
"""

class Subject(ABC):

    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self, **kwargs):
        pass

    @abstractmethod
    def stateChange(self, **kwargs):
        """specify the sate of the subject"""
        pass





