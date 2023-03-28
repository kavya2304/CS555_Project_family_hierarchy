import pytest
import pandas as pd
import user_stories
from user_stories import individual_ages1

def test_individual_ages1():
    details = [{
           'id': 'I1',
            'name': ' Tom /Brindley/',
            'age': 23}]
    print(individual_ages1(details))
    str1= str(individual_ages1(details)) 
    strout="Name: Tom  Brindley --->Age:23"
    
    #print("-->"+str1)
    assert strout == individual_ages1(details)
    