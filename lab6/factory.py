from enum import Enum

class PizzaType(Enum):
    Margarita=0,
    Mexico=1
    Stella=2

class Pizza:
    def __init__(self,price: float):
        self.price=price
    def get_price(self)->float:
        return self.price

class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)

class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)
        
class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)
def create_pizza(pizza_type:PizzaType)->Pizza:
    factory_dist={
        PizzaType.Margarita:PizzaMargarita,
        PizzaType.Mexico:PizzaMexico,
        PizzaType.Stella:PizzaStella,
    }
    return factory_dist[pizza_type]()
if __name__=='__main__':
    for pizza in PizzaType:
        my_pizza=create_pizza(pizza)
        print(f'Pizza type:{pizza},price{my_pizza.get_price()}')
