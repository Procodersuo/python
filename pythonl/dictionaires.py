
#DICTIONAIRES IN PYTHON

import pandas as pd
student = {
    "Name" : ["A","B"],
    "Class": ["Seven","SIX"],
    "Age":[8,9]
}

dataFrame= pd.DataFrame(student)
print(dataFrame)
print(dataFrame.info())
