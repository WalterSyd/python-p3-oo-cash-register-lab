#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.last_transaction = (0,0)

  #adds items, accepts optional quantity to calculate totals with multiple items
  def add_item(self, title, price, quantity = 1):
    self.items.extend([title] *  quantity)
    self.total += price * quantity
    self.last_transaction = (price, quantity, title)# Update last transaction details

  def apply_discount(self):
    if self.discount > 0:
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount #subtract discount from self.total 
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    price, quantity, title = self.last_transaction # Get last transaction details by unpacking tuple
    if price > 0:   #Checks if last ransaction is valid
      self.total -= price * quantity  #Subtracts last transaction price from total price
      for _ in range(quantity):
        self.items.remove(title)  #removes the item from items list for each quantity
      self.last_transaction = (0,0,"")    #resets the last transaction details to ("") if transaction voided
    else:
      print("There is no transaction to void")