"""Pydantic model builder."""

from typing import Callable, Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BuildablePydanticBase(BaseModel):
    """A base class for pydantic models that can be built using a builder.

    Args:
        BaseModel (BaseModel): The base model

    Returns:
        BuildablePydanticBase: The buildable pydantic base
    """
    @classmethod
    def builder(cls):
        """Create a builder for this model.

        Returns:
            PydanticModelBuilder: The builder
        """
        return PydanticModelBuilder(cls)


class PydanticModelBuilder:
    """ A builder for pydantic models.

    Args:
        T (TypeVar): The type of the model to build

    Returns:
        PydanticModelBuilder: The builder
    """
    __slots__ = ("__model__", "__values__")

    def __init__(self, model: Type[T]) -> None:
        """Initialize the builder.

        Args:
            model (Type[T]): The model to build
        """
        object.__setattr__(self, "__model__", model)
        object.__setattr__(self, "__values__", {})

    def __getattr__(self, name: str) -> Callable[[T], "PydanticModelBuilder"]:
        """Get an attribute.

        Args:
            name (str): The name of the attribute

        Returns:
            Callable[[T], "PydanticModelBuilder"]: The attribute
        """
        def method(value: T) -> "PydanticModelBuilder":
            """Set a field.

            Args:
                value (T): The value of the field

            Returns:
                PydanticModelBuilder: The builder
            """
            return self.set_field(value, name)

        return method

    def __setattr__(self, key, value):
        """Set an attribute.

        Args:
            key: The key of the attribute
            value: The value of the attribute

        Raises:
            KeyError: If the attribute is not a valid field

        Returns:
            None
        """
        self.set_field(value, key)

    def set_field(self, value: object, name: str) -> "PydanticModelBuilder":
        """Set a field.

        Args:
            value (object): The value of the field
            name (str): The name of the field

        Raises:
            KeyError: If the field is not a valid field

        Returns:
            PydanticModelBuilder: The builder
        """
        if not hasattr(self.__model__, name):
            raise KeyError(
                f"'{name}' is not a valid field in '{self.__model__.__name__}'."
            )

        self.__values__[name] = value
        return self

    def build(self) -> T:
        """Build the model.

        Returns:
            T: The model
        """
        return self.__model__(**self.__values__)
