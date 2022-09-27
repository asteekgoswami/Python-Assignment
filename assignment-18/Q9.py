#  Write a python program to merge two python dictionaries into one dictionary

from heapq import merge


about_person={'name':'asteek','age':20,'gender':'male'}
about_job={'company':'google','status':'SDE','salary':'10000000$'}

# def merge(dic1,dic2):
#     res={**dic1,**dic2}
#     return res

# dic=merge(about_person,about_job)
about_person.update(about_job)
print("After merging dictionary are :  ")
print(about_person)