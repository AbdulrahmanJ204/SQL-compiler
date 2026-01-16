from abc import ABC, abstractmethod


class ASTNode(ABC):

    def self_print(self, spacer, to_print=""):
        if to_print != "":
            to_print = f" : {to_print}"
        to_print = self.__class__.__name__ + to_print
        print(spacer, to_print)

    @abstractmethod
    def print(self, spacer="  ", level=0):
        pass
