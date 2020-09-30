"""
ABS class file
"""


from abc import *


class abc_class(metaclass=ABCMeta):
    @abstractmethod
    def calc_pct(self):
        pass

    def calc_meso(self):
        pass

    def calc_stat(self):
        pass

