'''
Created on 19 Feb 2021

@author: gh
'''

class cell(object):
        
    def __init__(self, status):
        self.status = status # 1 = ALIVE, 0 = DEAD
        self.neighbours = []