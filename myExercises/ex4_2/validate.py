class Validator:
    
    @classmethod
    def check(cls, value):
        return value

class Typed(Validator):
    expected_type = object
    
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)
    
class Positive(Validator):
    
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)
    
class NonEmpty(Validator):
    
    @classmethod
    def check(cls, value):
        if value == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
    
class Integer(Typed):
    expected_type = int
    
class Float(Typed):
    expected_type = float
    
class String(Typed):
    expected_type = str
    
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

class Stock:
    def __init__(self, name, shares, price):
        self._name = name
        self._shares = shares
        self._price = price
        
    # Get methods 
    @property
    def name(self):
        return self._name
     
    @property
    def shares(self):
        return self._shares
    
    @property
    def price(self):
        return self._price
    
    # Set methods
    @name.setter
    def name(self, value):
        self._name = NonEmptyString.check(value)
    
    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value) 
        
    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)