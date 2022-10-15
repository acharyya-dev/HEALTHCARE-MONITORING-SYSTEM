import pickle

def Dpredict(p,g,bp,i,bm,d,a):
    pickle_diabetes=open('E:/VS CODE/python/Health Care Monitoring System Project Py/merged/DIABETES.pkl', 'rb')
    diabetes=pickle.load(pickle_diabetes)
    prediction=diabetes.predict([[p,g,bp,i,bm,d,a]])
    return prediction

def Lpredict(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15):
    pickel_lung=open('E:/VS CODE/python/Health Care Monitoring System Project Py/merged/LUNG.pkl','rb')
    lung=pickle.load(pickel_lung)
    prediction=lung.predict([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]])
    return prediction

def Hpredict(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13):
    pickel_heart=open('E:/VS CODE/python/Health Care Monitoring System Project Py/merged/heart.pkl','rb')
    heart=pickle.load(pickel_heart)
    prediction=heart.predict([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]])
    return prediction


def Lungpredict():
    s1="USER INPUT"
    print(s1.center(50,'-'))
    GENDER=int(input("PRESS '0' for 'FEMALE' and '1' for 'MALE' : "))
    AGE = int(input("Enter Your Age : "))
    s2=" press '2' for 'YES' and press '1' for 'NO' "
    print(s2.center(60))
    SMOKING=int(input("Do You Smoke ? 1/2 : "))
    YELLOW_FINGERS = int(input("Do You have Yellow Fingers ? 1/2 : "))
    ANXIETY = int(input("Do You have Anxiety ? 1/2 : "))
    PEER_PRESSURE = int(input("Do You have Peer Pressure ? 1/2 : "))
    CHRONIC_DISEASE = int(input("Do You have any Chronic Disease ? 1/2 : "))
    FATIGUE= int(input("Do You have Fatigue ? 1/2 : "))
    ALLERGY = int(input("Do You have Allergy ? 1/2 : "))
    WHEEZING = int(input("Do You suffer from Wheezing ? 1/2 : "))
    ALCOHOL_CONSUMING = int(input("Do You Consume Alcohol ? 1/2 : "))
    COUGHING = int(input("Do You have coughing issues ? 1/2 : "))
    SHORTNESS_OF_BREATH = int(input("Do You suffer from Shortness Of Breathing ? 1/2 : "))
    SWALLOWING_DIFFICULTY = int(input("Do You suffer from Swalloing Difficulty ? 1/2 : "))
    CHEST_PAIN = int(input("Do You suffer from Chest Pain ? 1/2 : "))
    if Lpredict(GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN)==1:
            print("You have Lung Cancer! Please take care of yourself!")
    else:
        print("Congratulations! You don't have Lung Cancer ❤️")
    
def Diabetespredict():
    print("❤️WELCOME TO DIABETES CHECKING CLINIC❤️".center(100))
    Pregnancies=float(input("Enter The Number of Pregnancies : "))
    Glucose=float(input("Enter Glucose level : "))
    BloodPressure=float(input("Enter the Blood Pressure : "))
    Insulin=float(input("Insulin ammount ? :"))
    BMI=float(input("BMI : "))
    DiabetesPedigreeFunction=float(input("DiabetesPedigreeFunction: " ))
    Age=float(input("AGE : "))
    if Dpredict(Pregnancies,Glucose,BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age)==1:
        print("You have Diabetes! Please take care of yourself!")
    else:
        print("Congratulations! You don't have Diabetes ❤️")
        

def Heartpredict():
    s1="USER INPUT"
    print(s1.center(50,'-'))
    age= int(input("Enter your Age : "))
    sex=int(input("PRESS '0' for 'FEMALE' and '1' for 'MALE' : "))    
    cp=int(input("PRESS '1' FOR HAVING CONSTRICTIVE PERICARDITIS AND '0' OTHERWISE : "))
    trestbps = int(input("ENTER YOUR RESTING BLOOD PRESSURE : "))
    chol= int(input("ENTER YOUR SERUM CHOLESTEROL : "))
    s2=" press '1' for 'YES' and press '0' for 'NO' "
    print(s2.center(60))
    fbs = int(input("DO YOU HAVE FASTING BLOOD SUGAR (> 120 mg/dl)? 0/1:"))
    restecg = int(input("DO YOU HAVE RESTING ELECTROCARDIOGRAPHIC RESULTS? (VALUES 0,1,2):"))
    thalach	= int(input("Enter maximum heart rate achieved : "))
    s2=" press '1' for 'YES' and press '0' for 'NO' "
    print(s2.center(60))
    exang = int(input("Do you have Exercise induced angina? 0/1 :"))
    oldpeak =float(input("Enter your ST depression induced by exercise relative to rest : "))
    slope = int(input("Enter the slope of the peak exercise ST segment (values 0,1,2) :"))
    ca = int(input("Enter number of major vessels colored by flourosopy (values 0,1,2,3) :"))
    s2=" PRESS '0' = normal  '1' = fixed defect  '2' = reversable defect "
    print(s2.center(60))
    thal= int(input("Enter your Thalassemia status: "))
    if Hpredict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)==1:
            print("You have Heart Disease! Please take care of yourself!")
    else:
        print("Congratulations! You don't have Heart Disease ❤️")

if __name__=='__main__':
    print("What Do You Want To Predict ? ")
    print("Press 'D' for DIABETES ")
    print("Press 'L' for LUNG CANCER ")
    print("Press 'H' for HEART DISEASE ")
    choice=input("ENTER YOUR CHOICE : ")
    if choice=='D':
           Diabetespredict()
    elif choice=='L':
           Lungpredict()
    elif choice=='H':
           Heartpredict()
    else:
           print("INVALID CHOICE...!!!")
          





























