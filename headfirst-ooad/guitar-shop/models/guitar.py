from .guitar_spec import GuitarSpec, GuitarType, Wood, Builder


class Guitar:
    serial_number: str
    price: float
    spec: GuitarSpec

    def __init__(self, serial_number: str, price: float, spec: GuitarSpec) -> None:
        self.serial_number = serial_number
        self.price = price
        self.spec = spec


# def main():
#     g0 = Guitar()
#     g = Guitar("001", 200.56, GuitarSpec("Zen", "V12", GuitarType.Electric, Wood.Oak, Wood.Olive))
