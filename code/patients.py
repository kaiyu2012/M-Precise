import numpy as np


class Patient:
    def __init__(self):
        self.outcome = ""
        self.mutation = ""
        self.tcell = {}
        self.bcell = {}
        self.monotypes = {}
    

    def set_mutation(self, mutation):
        self.mutation = mutation
    
    def set_outcome(self, outcome):
        self.outcome = outcome
    
    def set_tcell(self, tcell):
        self.tcell = tcell
    
    def set_bcell(self, bcell):
        self.bcell = bcell
    
    def set_monotypes(self, monotypes):
        self.monotypes = monotypes
