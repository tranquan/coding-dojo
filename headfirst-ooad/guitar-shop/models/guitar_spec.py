from enum import Enum


class Builder(Enum):
    Yamaha = 1
    Toyota = 2
    Giver = 3


class GuitarType(Enum):
    Wood = 1
    Electric = 2
    Silver = 3


class Wood(Enum):
    Olive = 1
    Oak = 2
    Yak = 3


class GuitarSpec:
    builder: Builder
    model: str
    guitar_type: GuitarType
    back_wood: Wood
    top_wood: Wood
    num_strings: int

    def __init__(self, builder: Builder, model: str, guitar_type: GuitarType,
                 back_wood: Wood, top_wood: Wood, num_strings: int) -> None:
        self.builder = builder
        self.model = model
        self.guitar_type = guitar_type
        self.back_wood = back_wood
        self.top_wood = top_wood
        self.num_strings = num_strings

    def __eq__(self, spec: "GuitarSpec"):
        if (self.builder == spec.builder and self.model == spec.model and
                self.guitar_type == spec.guitar_type and
                self.top_wood == spec.top_wood and self.back_wood == spec.back_wood):
            return True
        return False
