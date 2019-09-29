from abc import ABC, abstractmethod

"""
This module contains the strategy implementation for roam.
It makes an interface for the abstract strategy of roam, RoamStrategyAbstract();
There are three concrete implementations of the roam strategy:
    - swim, i.e. RoamBySwimStrategy();
    - fly, i.e. RoamByFlyStrategy();
    - normal roam, i.e. RoamNormalStrategy()
"""

# an abstract class to make an interface for the abstract strategy roam
class RoamStrategyAbstract(ABC):

    @abstractmethod
    def roam(self):
        pass

# first concrete implementation of the roam strategy interface
class RoamBySwimStrategy(RoamStrategyAbstract):

    def roam(self):
        return " is swimming by RoamBySwimStrategy."

# second concrete implementation of the roam strategy interface
class RoamByFlyStrategy(RoamStrategyAbstract):

    def roam(self):
        return " is flying by RoamByFlyStrategy."

# third concrete implementation of the roam strategy interface
class RoamNormalStrategy(RoamStrategyAbstract):

    def roam(self):
        return " is roaming normally by RoamNormalStrategy."
