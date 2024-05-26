#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if isinstance(size, int):
            self.size = size
        else:
            print("size must be an integer")
        self.condition = 'New'

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = 'New'