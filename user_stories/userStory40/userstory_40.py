#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

def marriage_before_divorce_getting_error_line_no(families_dataframe):
    for i in range(len(families_dataframe)): 
        if "divorced" in families[i]:
            if type((families_dataframe[i]["married"])) != float and type((families_dataframe[i]["divorced"])) != float:
                marr = families_dataframe[i]["married"]
                divv = families_dataframe[i]["divorced"]
                if marr > divv:
                    message = "ERROR: FAMILY: US03: " + ": Divorced date " + str(divv) + ", Before Marriage date " + str(marr) + " , therefore it is not valid."
                    #print(message)
                    message1= "the line number is "+str(get_line(marr,divv,filename))
    return message1

def get_line(marr,divv,filename):
    f=open(filename).read()
    f_list=f.split("\n")
    for i in range(len(f_list)):
        if f_list[i].find(str(divv))!=-1:
            return i
        else:
            pass

