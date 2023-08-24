import abc

class CommandInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass
