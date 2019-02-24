import os
import sys
import math


# 3.5 Sort Stack such that the smallest items are on the top
# -> using another temprary stack to store items while finding the largest to put on bottom at each loop
def sortStack(stack):
  
  temp = list()
  n = len(stack)
  i = 0

  while i < n:

    # find largest
    largest = None
    while len(stack) > i:
      item = stack.pop()
      if largest == None or item > largest:
        if largest != None:
          temp.append(largest)
        largest = item
      else:
        temp.append(item)
    
    # put largest at bottom and find next largest
    stack.append(largest)
    while len(temp) > 0:
      item = temp.pop()
      stack.append(item)

    i += 1


# Test
# lst = list()
# lst.append(1)
# lst.append(4)
# lst.append(10)
# lst.append(5)
# lst.append(6)
# sortStack(lst)
# print(lst)


# 3.6 Animal Shelter
class Animal:
  animal_type = 0 # 0: dog, 1: cat
  animal_name = ""

  def __init__(self, animal_type, animal_name):
    self.animal_type = animal_type
    self.animal_name = animal_name


class AnimalShelter:
  queue = list()

  def enqueue(self, animal):
    queue = list()
    self.queue.insert(0, animal)

  def dequeueAny(self):
    if len(self.queue) == 0:
      return None
    else:
      return self.queue.pop()

  def dequeueCat(self):
    if len(self.queue) == 0:
      return None
    else:
      temp = list()
      cat = self.queue.pop()

      while cat.animal_type != 1:
        temp.insert(0, cat)
        cat = self.queue.pop()
      while len(temp) > 0:
        animal = temp.pop()
        self.queue.append(animal)

      if cat.animal_type == 1:
        return cat
      else:
        return None

  def dequeueDog(self):
    if len(self.queue) == 0:
      return None
    else:
      temp = list()
      dog = self.queue.pop()

      while dog.animal_type != 0:
        temp.insert(0, dog)
        dog = self.queue.pop()
      while len(temp) > 0:
        animal = temp.pop()
        self.queue.append(animal)

      if dog.animal_type == 0:
        return dog
      else:
        return None

# Test
# shelter = AnimalShelter()
# shelter.enqueue(Animal(1, "cat1"))
# shelter.enqueue(Animal(1, "cat2"))
# shelter.enqueue(Animal(1, "cat3"))
# shelter.enqueue(Animal(0, "dog1"))
# shelter.enqueue(Animal(0, "dog2"))

# animal = shelter.dequeueAny()
# print(animal.animal_name)

# animal = shelter.dequeueDog()
# print(animal.animal_name)

# animal = shelter.dequeueCat()
# print(animal.animal_name)