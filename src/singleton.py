"""The singleton metaclass for ensuring only one instance of a class."""
import abc


class Singleton(abc.ABCMeta, type):
    """Singleton metaclass for ensuring only one instance of a class."""

    _instances: dict[type, "Singleton"] = {}

    def __call__(cls, *args, **kwargs):
        """Call method for the singleton metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AbstractSingleton(abc.ABC, metaclass=Singleton):
    """Abstract singleton class for ensuring only one instance of a class."""
