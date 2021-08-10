import numpy as np


class Patient:
    def __init__(self):
        self.id = ""
        self.outcome = ""
        self.treatment = ""
        self.mutation = ""
        self.tcell = {}
        self.bcell = {}
        self.monotypes = {}
        self.neu = {}
    
    def set_id(self, pid):
        self.id = pid

    def set_mutation(self, mutation):
        self.mutation = mutation
    
    def set_outcome(self, outcome):
        self.outcome = outcome

    def set_treatment(self, treatment):
        self.treatment = treatment
    
    def set_tcell(self, tcell):
        self.tcell = tcell
    
    def set_bcell(self, bcell):
        self.bcell = bcell
    
    def set_monotypes(self, monotypes):
        self.monotypes = monotypes

    def set_neu(self, neu):
        self.neu = neu
