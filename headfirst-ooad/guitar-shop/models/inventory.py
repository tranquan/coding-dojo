from typing import List
from .guitar_spec import GuitarSpec
from .guitar import Guitar


class Inventory:
    guitars: List[Guitar]

    def __init__(self, guitars: List[Guitar]) -> None:
        self.guitars = guitars

    def add_guitar(self, guitar: Guitar):
        self.guitars.append(guitar)

    def search(self, spec: GuitarSpec) -> List[Guitar]:
        results = list()

        for g in self.guitars:
            if g.spec == spec:
                results.append(g)

        return results
