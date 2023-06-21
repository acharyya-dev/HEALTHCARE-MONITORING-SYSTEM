

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# # USER INPUT

# In[2]:


# Pregnancies=float(input("Enter The Number of Pregnancies : "))
# Glucose=float(input("Enter Glucose level : "))
# BloodPressure=float(input("Enter the Blood Pressure : "))
# Insulin=float(input("Insulin ammount ? :"))
# BMI=float(input("BMI : "))
# DiabetesPedigreeFunction=float(input("DiabetesPedigreeFunction: " ))
# Age=float(input("AGE : "))


# In[3]:


df=pd.read_csv('E:/VS CODE/python/Health Care Monitoring System Project Py/diabetes/diabetes.csv')


# In[4]:


df


# In[5]:


print("Dimension",df.shape)


# In[6]:


print(df.groupby('Outcome').size())


# In[7]:


df.info()


# # DATA PRE-PRCOESSING

# In[8]:


dfupdated=df.drop(['Outcome','SkinThickness'],axis='columns')


# In[9]:


dfupdated


# In[10]:


outcome=df.Outcome #outcome=df['Outcome']
outcome


# In[11]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(dfupdated,outcome,stratify=outcome,train_size=.8,random_state=66)


# ## K FOLD CROSS VALIDATION
# 

# In[12]:


from sklearn.neighbors import KNeighborsClassifier
test_acc=[]
for i in range(1,16):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,Y_train)
    test_acc.append(knn.score(X_test,Y_test))
    print("KNN.SCORE : ",knn.score(X_test,Y_test),"\"FOR THE NEIGHBOR\" : ",i)
plt.figure(figsize=(10, 10))
ax=plt.axes()
ax.set_facecolor('black') #set_color
plt.plot(range(1,16),test_acc,color="yellow",marker="o")    
plt.xlabel("N Neighbors")
plt.ylabel("Accuracy")


# ## FINAL FIT OF THE MODEL USING KNN
# 

# In[13]:


knnMODEL=KNeighborsClassifier(n_neighbors=13)


# In[14]:


knnMODEL.fit(X_train,Y_train)


# ## CROSS VALIDATION OF RANDOM FOREST CLASSIFIER

# In[15]:


from sklearn.ensemble import RandomForestClassifier
rfcACC=[]
for i in range(1,101):
    rfcMODEL=RandomForestClassifier(n_estimators=i)
    rfcMODEL.fit(X_train,Y_train)
    rfcACC.append(rfcMODEL.score(X_test,Y_test))
n_est=rfcACC.index(max(rfcACC))+1 
print(rfcACC.index(max(rfcACC))+1,max(rfcACC))    
plt.figure(figsize=(10, 10))
ax=plt.axes()
ax.set_facecolor('turquoise') #set_color  
plt.plot(range(1,101),rfcACC,color="red",marker="o")    
plt.xlabel("n_estimator")
plt.ylabel("Accuracy")


# ## FINAL FIT OF MODEL USING RANDOM FOREST CLASSIFIER

# In[16]:


rfcMODEL=RandomForestClassifier(n_estimators=n_est)
rfcMODEL.fit(X_train,Y_train)


# ## FINAL FIT OF MODEL USING SUPPORT VECTOR CLASSIFIER

# In[17]:


from sklearn.svm import SVC
svcMODEL=SVC(kernel='rbf',gamma=20)
svcMODEL.fit(X_train,Y_train)


# ## FINALIZE THE OUTCOME USING VOTING CLASSIFIER FROM ENSEMBLE LEARNING 

# In[18]:


from sklearn.ensemble import VotingClassifier 
vcMODEL = VotingClassifier(estimators =[('KNN',knnMODEL),('RFC',rfcMODEL),('SVC',svcMODEL)],voting='hard')
vcMODEL.fit(X_train,Y_train)
# pred=vcMODEL.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])


# ### DUMPING THE MODEL SO THAT IT CAN BE USED FURTHER

# In[19]:


import pickle
pickle_out = open("DIABETES.pkl", "wb")
pickle.dump(vcMODEL, pickle_out)
pickle_out.close()


# In[ ]:





# ## ACCURACIES OF DIFFERENT ALGORITHMS ALONG WITH THEIR OUTCOME 

# In[20]:


# print("Kth NEAREST NEIGHBOR : ",knnMODEL.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])," : ",format(((knnMODEL.score(X_test,Y_test))*100),".2f"),"%")
# print("RANDOM FOREST CLASSIFIER : ",rfcMODEL.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])," : ",format(((rfcMODEL.score(X_test,Y_test))*100),".2f"),"%")
# print("SUPPORT VECTOR CLASSIFIER : ",svcMODEL.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])," : ",format(((svcMODEL.score(X_test,Y_test))*100),".2f"),"%")
# print("VOTING CLASSIFIER : ",vcMODEL.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])," : ",format(((vcMODEL.score(X_test,Y_test))*100),".2f"),"%")


# # FINAL OUTCOME

# In[21]:


# if pred==1:
#     print("You have Diabetes! Please take care of yourself!")
# else:
#     print("Congratulations! You don't have Diabetes ❤️")

