#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []

  #adds items, accepts optional quantity to calculate totals with multiple items
  def add_item(self, title, price, quantity = 1):
    self.items.append((title, price, quantity))
    self.total += price * quantity

  def apply_discount(self):
    if self.discount > 0:
      self.total -= (self.total *(self.discount / 100))
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")