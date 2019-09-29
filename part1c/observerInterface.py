from abc import ABC, abstractmethod

"""
This module defines the interface for the observer with an abstract class.
It is inherited by zooannouncer.

This script was created with reference to slides "OOAD CL12-L14 Decorator" and the example here: 
http://www.djangospin.com/design-patterns-python/observer/
"""

class Observer(ABC):

    @abstractmethod
    def update(self, info):
        pass