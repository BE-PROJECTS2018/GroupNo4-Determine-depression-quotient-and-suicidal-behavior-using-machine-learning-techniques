import pandas as pd
import numpy as np
sheet=pd.read_csv(r'C:\Users\Ankita\anshikaextended.csv')
sheet.head()
index=[]

columns=['score']
scoresheet=pd.DataFrame(index=index,columns=columns)
for i in range (1,1405):
    if sheet['s3'][i]==1.0 and sheet['s6'][2*i]==0.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=1
    if sheet['s3'][i]==1.0 and sheet['s6'][2*i]==0.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=2
    if sheet['s3'][i]==0.0 and sheet['s6'][2*i]==0.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=3
    if sheet['s3'][i]==0.0 and sheet['s6'][2*i]==0.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=4
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==6.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=5
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==1.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=6
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==2.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=7
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==4.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=8
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==3.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=9
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==5.0 and sheet['s2'][i]==0.0:
        scoresheet['score'][i]=10
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==6.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=11
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==2.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=12
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==4.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=13
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==1.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=14
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==3.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=15
    if sheet['s3'][i]==2.0 and sheet['s6'][2*i]==5.0 and sheet['s2'][i]==1.0:
        scoresheet['score'][i]=16
scoresheet
scoresheet.to_csv(r'C:\Users\.......\.csv')
