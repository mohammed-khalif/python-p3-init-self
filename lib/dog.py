#!/usr/bin/env python3

class Dog:
    pass
# lib/dog.py

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

    def sit(self):
        print(f"The dog {self.name} is sitting.")
