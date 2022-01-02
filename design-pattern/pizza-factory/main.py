class Pizza:
    name = "Unknown"

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.name} Pizza"


class NormalPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Normal"


class CheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Cheese"


class ButterPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Butter"


class NormalPizzaStockholm(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Stockholm Normal"


class CheesePizzaStockholm(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Stockholm Cheese"


class AbstractPizzaFactory:
    @staticmethod
    def create_pizza(type: str):
        pass


class GotPizzaFactory(AbstractPizzaFactory):
    @staticmethod
    def create_pizza(type: str):
        if type == "cheese":
            return CheesePizza()
        if type == "butter":
            return ButterPizza()
        else:
            return NormalPizza()


class StkPizzaFactory(AbstractPizzaFactory):
    @staticmethod
    def create_pizza(type: str):
        if type == "cheese":
            return CheesePizzaStockholm()
        else:
            return NormalPizzaStockholm()


class PizzaStore:
    factory: AbstractPizzaFactory

    def __init__(self, factory: AbstractPizzaFactory) -> None:
        self.factory = factory

    def order_pizza(self, type: str) -> Pizza:
        pizza = self.factory.create_pizza(type)
        # preparing pizza here
        # pizza.prepare()
        # pizza.bake()
        # pizza.cut()
        return pizza


def main():
    p1 = NormalPizza()
    p2 = CheesePizza()
    print(p1)
    print(p2)

    p3 = GotPizzaFactory.create_pizza("cheese")
    print(p3)
    p4 = GotPizzaFactory.create_pizza("yummy")
    print(p4)

    store = PizzaStore(StkPizzaFactory())
    p = store.order_pizza("cheeses")
    print(p)


main()
