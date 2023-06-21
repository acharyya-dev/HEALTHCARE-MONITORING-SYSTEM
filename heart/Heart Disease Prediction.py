#!/usr/bin/env python
# coding: utf-8

# # Heart Disease Predictor

# ## importing dependencies

# In[45]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ## Data Collection and Processing

# In[46]:


# loading csv data to a Pandas DataFrame
heart_data = pd.read_csv('E:/VS CODE/python/Health Care Monitoring System Project Py/heart/data.csv')

# Parameters (columns)
# 1) age
# 2) sex
# 3) chest pain type (4 values)
# 4) resting blood pressure
# 5) serum cholestoral in mg/dl
# 6) fasting blood sugar > 120 mg/dl
# 7) resting electrocardiographic results (values 0,1,2)
# 8) maximum heart rate achieved
# 9) exercise induced angina
# 10) oldpeak = ST depression induced by exercise relative to rest
# 11) the slope of the peak exercise ST segment
# 12) number of major vessels (0-3) colored by flourosopy
# 13) thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
# 14) The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.


# In[47]:


# print first 5 rows of the dataset
heart_data.head()


# In[48]:


# print last 5 rows of the dataset
heart_data.tail()


# In[49]:


# number of rows and column in the dataset
heart_data.shape


# In[50]:


# getting some info about the data
heart_data.info()


# In[51]:


#Checking for missing values
heart_data.isnull().sum()


# In[52]:


#Statistical measures of the data
heart_data.describe()


# In[53]:


# Checking the distribution of Terget variable
heart_data['target'].value_counts()


# ### 1 represents - Defective Heart
# ### 0 represents - Healthy Heart

# ## Spliting the Features and Target column

# In[54]:


X = heart_data.drop(columns='target',axis=1)
Y = heart_data['target']


# In[55]:


print(X)


# In[56]:


print(Y)


# ## Splitiing the data into Training Data and Test Data

# In[57]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)


# In[58]:


print(X.shape,X_train.shape,X_test.shape)


# ## Model Training

# ### Logistic Regression Model

# In[59]:


model = LogisticRegression()


# In[60]:


# Training logistic regression model with Training data
model.fit(X_train,Y_train)


# ## Model evaluation

# ### Accuracy Score

# In[61]:


# Accuracy on the training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)


# In[62]:


print('Accuracy on Training Data: ',training_data_accuracy)


# In[63]:


# Accuracy on the training data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)


# In[64]:


print('Accuracy on Test Data: ',test_data_accuracy)


# # PICKLE
# 
# 

# In[65]:


import pickle
pickle_out = open("heart.pkl", "wb")
pickle.dump(model, pickle_out)
pickle_out.close()


# # Building a Predictive System

# In[66]:


# input_data = (54,1,0,122,286,0,0,116,1,3.2,1,2,2)

# # change input data to a numpy array
# input_data_as_numpy_array = np.asarray(input_data)

# # reshape the numpy array as we are predicting for only one instance
# input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# prediction = model.predict(input_data_reshaped)

# print(prediction)
# if(prediction[0]==0):
#     print('The person DOES NOT HAVE a Heart Disease. ')
# else:
#     print('The person HAS a Heart Disease. ')


# In[ ]:




