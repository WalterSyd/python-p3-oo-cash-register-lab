#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.items.append((title, price, quantity))
    self.total += price * quantity