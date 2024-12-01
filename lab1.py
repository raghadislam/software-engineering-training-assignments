# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QMHTN4Zef8k-iXrExCoKY5n5bmOBsQth
"""

class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print("{} is eating".format(self.name))

  def sleep(self):
    print("{} is sleeping".format(self.name))


class Dog(Animal):
  def bark(self):
    print("{} is barking".format(self.name))

class Cat(Animal):
  def meow(self):
    print("{} is mewoing".format(self.name))


dog1 = Dog("doggy")
dog1.eat()
dog1.sleep()
dog1.bark()

print('\n')

cat1 = Cat("memyy")
cat1.eat()
cat1.sleep()
cat1.meow()