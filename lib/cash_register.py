#!/usr/bin/env python3

class CashRegister:

  def __init__(self, name, price, total = 0, discount = None):
    self.name = name
    self.price = price
    self.total = total
    self.discount = discount
    self.items = []

    # def get_discount(self):
    #     return self._discount

    # def set_discount(self, discount):
    #     if type(discount) == int:
    #         self._discount = discount
    #     else:
    #         print("size must be an integer")

    # discount = property(get_discount, set_discount,)


  def add_item(self, name, price, quantity = 1):
    for i in list(range(quantity)):
      self.items.append({"name": name, "price": price})
      self.total += price
    return self.total


  def apply_discount(self):
    if self.discount > 0:
      discount = self.discount/100
      disc_total = self.total * (1-discount)
      print(f"After the discount, the total comes to {disc_total}.")
      return disc_total
    else:
      print("There is no discount to apply.")

  def item_names(self):
    names = [self.get_attr(item, "name") for item in self.items]
    return names

  def void_last_item(self):
    if self.items:
      removed_item = self.items.pop()
    else:
      return "There are no items in your cart!"
    self.total -= removed_item['price']
