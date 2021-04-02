# from models.guitar import Inventory, Guitar, GuitarSpec, GuitarType, Builder, Wood
from models.guitar import Guitar
from models.guitar_spec import GuitarSpec, GuitarType, Builder, Wood
from models.inventory import Inventory


def main():
    inventory = Inventory([])
    inventory.add_guitar(
        Guitar("001", 120.5, GuitarSpec(Builder.Toyota, "A002", GuitarType.Electric, Wood.Oak, Wood.Yak))
    )
    inventory.add_guitar(
        Guitar("002", 200, GuitarSpec(Builder.Toyota, "A002", GuitarType.Electric, Wood.Oak, Wood.Yak))
    )
    inventory.add_guitar(
        Guitar("003", 150, GuitarSpec(Builder.Toyota, "B005", GuitarType.Silver, Wood.Oak, Wood.Yak))
    )

    results = inventory.search(GuitarSpec(
        Builder.Toyota, "A002", GuitarType.Electric, Wood.Oak, Wood.Yak))

    for r in results:
        print(f'--- found guitar: {r.serial_number}, price: {r.price}')


if __name__ == "__main__":
    main()
