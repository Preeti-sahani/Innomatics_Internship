#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import library

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np


# In[2]:


# loading the dataset

df=pd.read_csv("diamonds.csv")
df.head()


# In[3]:


# Step - 2: Perform the EDA on the given dataset

df.describe()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


sn.boxplot(x="x",data=df)


# In[7]:


sn.boxplot(x="y",data=df)


# In[8]:


sn.boxplot(x="z",data=df)


# In[9]:



# In x,y,z features ther are some outliers and also some data points are at zero so we have to remove them 

df=df.drop(df[df['x']==0].index)
df=df.drop(df[df['y']==0].index)
df=df.drop(df[df['z']==0].index)


# In[10]:


df.shape


# In[11]:


sn.pairplot(df,hue="cut")


# In[12]:


sn.boxplot(x="z",data=df)


# We have remove all the outliers from x y z columns

# In[13]:


sn.barplot(x="cut",y="price",data=df)


# It is clear that premium cut diamond is most expensive and ideal cut is most cheaper in price
# 

# In[14]:


sn.barplot(x="color",y="price",data=df)


# It is clear that j color diamond is very expensive compared to E color
# 

# In[15]:


sn.barplot(x="clarity",y="price",data=df)


# We can sea s12 clarity diamond are most expensive

# In[16]:


sn.histplot(x="table",data=df,kde=True)


# In[17]:


sn.boxplot(x="table",data=df)


# In[18]:


q1 = df['table'].quantile(0.25)
q3 = df['table'].quantile(0.75)
print(q1,q3)


# In[19]:


iq =q3-q1
iq


# In[20]:


df = df[(df["table"]<63.5)&(df["table"]>51.5)]


# In[23]:


sn.boxplot(x="table",data=df)


# We remove outliers from table coulms also
# 

# In[24]:


sn.boxplot(x="depth",data=df)


# In[25]:


q1_d = df['depth'].quantile(0.25)
q3_d = df['depth'].quantile(0.75)
print(q1_d,q3_d)
iqr_d=q3_d-q1_d
upper = q3_d+ 1.5 * iqr_d
lower = q1_d - 1.5 * iqr_d
print(upper,lower)


# In[26]:


df = df[(df["depth"]<64.6)&(df["depth"]>59)]


# In[27]:


sn.boxplot(x="depth",data=df)


# In[28]:


sn.boxplot(x="carat",data=df)


# # Step - 3: Handle Categorical Columns
# 

# In[29]:



from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df['color']= label_encoder.fit_transform(df['color'])
df['cut']= label_encoder.fit_transform(df['cut'])
df['clarity']= label_encoder.fit_transform(df['clarity'])


# In[30]:


df


# In[31]:


correrlation= df.corr()
sn.heatmap(correrlation,annot=True)


# We can see that price has maximum correlation with carat,x,y,z and the leat correlation is with clarity,depta
# 

# # Step - 4: Normalize the data

# In[34]:


from sklearn.preprocessing import StandardScaler
standardized_df = StandardScaler().fit_transform(df)
print(standardized_df.shape)


# # Step - 5: Split the data - Test and Train

# In[35]:


x=df[['carat','cut','color','clarity','depth','table','x', 'y','z']]


# In[36]:


y=df['price']


# In[37]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)


# In[38]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print(knn.predict(X_test))


# In[39]:


# accuracy of model
print(knn.score(X_test, y_test))


# In[44]:


from sklearn.linear_model import LinearRegression

lr = LinearRegression()


# # Linear regression model
# 

# In[47]:


lr.fit(X_train,y_train)

y_pred =print(lr.predict(X_test))


# In[48]:


lr.coef_


# In[49]:


cofficent=pd.DataFrame(lr.coef_,x.columns,columns=['Coeff'])
cofficent


# # Accuracy of model

# In[50]:


print(lr.score(X_test, y_test))


# In[52]:


from sklearn import metrics

result=lr.predict(X_test)
print("Mean absolute error is ",metrics.mean_absolute_error(y_test,result))


# In[53]:


print("Mean Squared error is ",metrics.mean_squared_error(y_test,result))


# In[54]:


print("Root-mean-square error is ",np.sqrt(metrics.mean_squared_error(y_test,result)))


# # Random forest model

# In[55]:


from sklearn.ensemble import RandomForestRegressor

RF= RandomForestRegressor()
RF.fit(X_train,y_train)


# In[59]:


y_pred =print(RF.predict(X_test))


# In[60]:


pred_RF=RF.predict(X_test)


# In[62]:


r2=metrics.explained_variance_score(y_test,pred_RF)
r2

