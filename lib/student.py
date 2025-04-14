#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # Each student starts with an empty list for knowledge
        self.knowledge = []

    def learn(self, fact):
        self.knowledge.append(fact)