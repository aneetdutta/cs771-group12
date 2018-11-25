
# coding: utf-8

# # Cosine Similarity:

# In[93]:


import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
df=pd.read_csv('movieId_ftrd.csv')
#print(df)
vocab=['Action', 'Adventure','Animation','Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','IMAX']
list1=[]
for i in range(df.shape[0]):
    list1.append(df.iloc[i]['genres'].split('|'))
    #print(list1)
#print(df.iloc[1]['genres'].split('|'))
b=np.zeros((df.shape[0],len(vocab)),dtype=int)
#print(b)
for j in range(df.shape[0]):
    #print(list1[j])
    for i in range(len(list1[j])):
        c=vocab.index(list1[j][i])
        b[j][c]=1
        #print(c)
#print(b[1])
d=np.zeros((df.shape[0],df.shape[0]),dtype=float)
print(d.shape)
from scipy.spatial import distance
for i in range(df.shape[0]):
    for j in range(df.shape[0]):
        b[i].reshape(1,19)
        b[j].reshape(1,19)
        d[i][j]=1-distance.cosine(b[i],b[j])
       # print((b[i]-b[j]))
       # print(euclidean_distances(b[i],b[j]))
        
print(d[1][500])
print(df.iloc[1])
print(df.iloc[500])
        


# In[103]:


print(d[100][120])
print(df.iloc[100])
print(df.iloc[120])


# # Jaccard Distance:

# In[143]:


from scipy.spatial import distance
jaccard=np.zeros((df.shape[0],df.shape[0]),dtype=float)
for i in range(df.shape[0]):
    for j in range(df.shape[0]):
        A=set(df.iloc[i]['genres'].split('|'))
        B=set(df.iloc[j]['genres'].split('|'))
        #print(A)
        #print(B)
        C=A | B
        c=len(C)
        D=A & B
        d=len(D)
        num=float(c-d)
        den=float(c)
        print("-----")
        #print(D)
        jaccard[i][j]=1-(num/den)
        #print(len(C))
        #print(len(D))


# In[149]:


#A=set(df.iloc[31]['genres'].split('|'))
#B=set(df.iloc[36]['genres'].split('|'))
#C=A.union(B)
#c=len(C)
#print(c)
#D=A &B
#d=len(D)
#print(5/6)

#j=float((float(c-d))/float(c))
#print(j)
print(jaccard[45][360])
print(df.iloc[45])
print(df.iloc[360])


# ## 
