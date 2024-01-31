from item import item
class Phone(item):
    # to have access to all attribute of the class parent we need to use super
    def __init__(self, electronic: str, price: float, quantity: int, brokens=0):
        super().__init__(electronic, price, quantity)   
        assert brokens>=0, f'the {brokens} is not greater or equal than 0!'
        # assign to self object
        self.brokens=brokens