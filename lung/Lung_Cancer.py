

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# # USER INPUT

# In[137]:


#  s1="USER INPUT"
# print(s1.center(50,'-'))

# GENDER=int(input("PRESS '0' for 'FEMALE' and '1' for 'MALE' : "))
# AGE = int(input("Enter Your Age : "))
# s2=" press '2' for 'YES' and press '1' for 'NO' "
# print(s2.center(60))
# SMOKING=int(input("Do You Smoke ? 1/2 : "))
# YELLOW_FINGERS = int(input("Do You have Yellow Fingers ? 1/2 : "))
# ANXIETY = int(input("Do You have Anxiety ? 1/2 : "))
# PEER_PRESSURE = int(input("Do You have Peer Pressure ? 1/2 : "))
# CHRONIC_DISEASE = int(input("Do You have any Chronic Disease ? 1/2 : "))
# FATIGUE	= int(input("Do You have Fatigue ? 1/2 : "))
# ALLERGY = int(input("Do You have Allergy ? 1/2 : "))
# WHEEZING = int(input("Do You suffer from Wheezing ? 1/2 : "))
# ALCOHOL_CONSUMING = int(input("Do You Consume Alcohol ? 1/2 : "))
# COUGHING = int(input("Do You have coughing issues ? 1/2 : "))
# SHORTNESS_OF_BREATH = int(input("Do You suffer from Shortness Of Breathing ? 1/2 : "))
# SWALLOWING_DIFFICULTY = int(input("Do You suffer from Swalloing Difficulty ? 1/2 : "))
# CHEST_PAIN = int(input("Do You suffer from Chest Pain ? 1/2 : "))


# In[138]:



df=pd.read_csv('E:/VS CODE/python/Health Care Monitoring System Project Py/lung/cancer.csv')
df
print(df.groupby('LUNG_CANCER').size())


# # DATA PREPROCESSING USING LABEL ENCODER

# In[139]:


from sklearn.preprocessing import LabelEncoder as LE
le = LE() #LE alias for LabelEncoder()
df['LUNG_CANCER']=le.fit_transform(df['LUNG_CANCER'])
df['GENDER']=le.fit_transform(df['GENDER'])
df.head()


# In[140]:


outcome=df.LUNG_CANCER
outcome.head()


# In[141]:


dfupdated=df.drop(['LUNG_CANCER'],axis='columns')
dfupdated.head()


# ## SPLITTING THE MODEL USING TRAIN_TEST_SPLIT

# In[142]:


from sklearn.model_selection import train_test_split as tts
X_train,X_test,Y_train,Y_test=tts(dfupdated,outcome,stratify=outcome,train_size=.8,random_state=66)


# In[143]:


X_train


# In[144]:


Y_train


# ## CROSS VALIDATION OF RANDOM FOREST CLASSIFIER

# In[145]:


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


# ### FINAL FIT OF MODEL USING RANDOM FOREST CLASSIFIER

# In[146]:


rfcMODEL=RandomForestClassifier(n_estimators=n_est)
rfcMODEL.fit(X_train,Y_train)

import pickle
pickle_out = open("LUNG CANCER.pkl", "wb")
pickle.dump(rfcMODEL, pickle_out)
pickle_out.close()


# ## CONFUSION MATRIX

# In[147]:


# from sklearn.metrics import confusion_matrix
# cm=confusion_matrix(Y_test,rfcMODEL.predict(X_test))
# cm


# ## PLOTTING THE CONFUSION MATRIX USING HEATMAP

# In[148]:



# import matplotlib.pyplot as plt
# import seaborn as sn
# plt.figure(figsize=(10,7))
# sn.heatmap(cm, annot=True)
# plt.xlabel('Predicted')
# plt.ylabel('Truth')


# ## ACCURACY OF THE MODEL

# In[149]:


# print("ACCURACY OF THE MODEL : ",format(((rfcMODEL.score(X_test,Y_test))*100),".2f"),"%")


# ## FINAL OUTCOME

# In[150]:


# if Y_predict==1:
#     print("You Got Lung Cancer!")
# else:
#     print("Congratulations❤️ You don't have Lung Cancer")

