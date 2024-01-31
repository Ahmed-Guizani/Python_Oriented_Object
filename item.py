import csv

class item:
    pay_rate = 0.8 # 20% discount defined in the class level
    list = [] # the list of all data
    def __init__(self, electronic: str, price: float, quantity: int):
        
        # run validation to received argument
        assert price >= 0, f"Price {price} is not greater or equal than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not equal or greater than zero!"
        
        # les variable a definir pour l'objet
        self.__electronic = electronic
        self.price = price
        self.quantity = quantity
        # ici on va ajouter les data a la list
        self.list.append(self)

    # to let the electronic not mofied but for read only
    @property
    def electronic(self):
        return self.__electronic
    # to give some rules to modify electronic
    @electronic.setter
    def electronic(self, value):
        if len (value) > 20:
            raise Exception("the name you give it is too long!")
        else:
            self.__electronic=value

    # methode to calculate the total of price quantity
    def calculate_total_price (self):
        return self.quantity * self.price
    
    # here the discount are token from the class level if not defined as entry
    def apply_discount (self):
        self.price = self.price * self.pay_rate
    # use of static method
    @staticmethod
    def is_integer(num):
        # i will check if the entry is a integer or not for i.e: 5.0, 10.0$
        if isinstance(num, float):
            # count out if the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return True
    # to have the data in csv file and use it
    @classmethod
    def instanciate_from_csv(classmethod):
        # to open the file
        with open("table.csv", 'r') as f:
            # convert to python dictionnary
            reader = csv.DictReader (f)
            items = list(reader)
        # initiate instances
        for i in items:
            item(
                electronic=i.get('electronic'),
                price=float(i.get('price')),
                quantity=int(i.get('quantity')),
            )
    # here the function fo the visualisation of the all data
    def __repr__(self) -> str:
        # in order to know which class the super or the child we will use {self.__class__.__name__}
        return f"{self.__class__.__name__} ('{self.electronic}', {self.price}, {self.quantity})"
    @property
    def read_only_name(self):
        return "AAA"