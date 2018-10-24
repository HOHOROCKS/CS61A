# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """
    def __init__(self, value=0):
        self.value = value


    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value== 0:
            new = Fib()
            new.value = 1
        else:
            new = Fib()
            new.value = self.value + self.adder
        new.adder = self.value
        return new


    def __repr__(self):
        return str(self.value)
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    amount = 0
    def __init__(self, name, cost, balance = 0, stock = 0):
        self.name = name
        self.cost = cost
        self.balance = balance
        self.stock = stock


        

    def vend(self):
        if self.stock <= 0 and self.balance != 0:
            return 'Machine is out of stock. Here is your $' + str(self.balance) + '.'
        elif self.stock <= 0 and self.balance == 0:
            return 'Machine is out of stock.'
        else:
            if self.balance < self.cost:
                return 'You must deposit $' + str((self.cost - self.balance)) +' more.'
            else:
                if self.balance == self.cost:
                    self.balance -= self.cost
                    self.stock -= 1
                    return 'Here is your ' + self.name + '.'
                else:
                    change = self.balance - self.cost
                    self.balance = 0
                    self.stock -= 1
                    return 'Here is your ' + self.name + ' and $' + str(change) + ' change.'

    def deposit(self, amount):
        
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(self.balance + amount) + '.'
        else:
            self.balance += amount
            return 'Current balance: $' + str(self.balance)

    def restock(self, amount):
        self.stock += amount
        return 'Current ' + self.name + ' stock: ' + str(self.stock)