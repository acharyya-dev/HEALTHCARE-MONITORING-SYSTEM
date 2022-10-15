import streamlit as st
from streamlit_option_menu import option_menu
import time
import pickle

ch=['YES','NO']
def negativeprogressbar():
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div 
        {
            background-image: linear-gradient(to right, #00ccff,#99ff99);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress=st.progress(0)
    for i in range(100):
        time.sleep(0.001)
        progress.progress(i)
def positiveprogressbar():
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div 
        {
            background-image: linear-gradient(to right, #00ccff,#ff0000);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress=st.progress(0)
    for i in range(100):
        time.sleep(0.001)
        progress.progress(i)
             
def choicevar01(var,yes,no):
    if var==yes:
        return 1
    else:
        return 0    

def choicevar12(var,yes,no):
    if var==yes:
        return 2
    else:
        return 1

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
    st.markdown("""
    ### :heart: **WELCOME TO LUNG CANCER CHECKING CLINIC** :heart: """,True)
    gender=st.radio("GENDER",['MALE','FEMALE'])
    GENDER=choicevar01(gender,'MALE','FEMALE')

    AGE = st.number_input("ENTER YOUR AGE")

    smoking=st.radio("DO YOU SMOKE",ch)
    SMOKING=choicevar12(smoking,'YES','NO')

    YF = st.radio("DO YOU HAVE YELLOW FINGERS",ch)
    YELLOW_FINGERS=choicevar12(YF,'YES','NO')

    A = st.radio("DO YOU HAVE ANXIETY",ch)
    ANXIETY=choicevar12(A,'YES','NO')

    peer= st.radio("DO YOU HAVE PEER PRESSURE",ch)
    PEER_PRESSURE=choicevar12(peer,'YES','NO')

    CD = st.radio("DO YOU HAVE ANY CHRONIC DISEASE",ch)
    CHRONIC_DISEASE=choicevar12(CD,'YES','NO')

    f= st.radio("DO YOU HAVE FATIGUE",ch)
    FATIGUE=choicevar12(f,'YES','NO')

    aller = st.radio("DO YOU HAVE ALLERGY",ch)
    ALLERGY=choicevar12(aller,'YES','NO')

    W = st.radio("DO YOU SUFFER FROM WHEEZING",ch)
    WHEEZING=choicevar12(W,'YES','NO')

    ac = st.radio("DO YOU CONSUME ALCOHOL",ch)
    ALCOHOL_CONSUMING=choicevar12(ac,'YES','NO')

    cough = st.radio("DO YOU HAVE COUGHING ISSUES",ch)
    COUGHING=choicevar12(cough,'YES','NO')
    
    sob = st.radio("DO YOU SUFFER FROM SHORTNESS OF BREARHING",ch)
    SHORTNESS_OF_BREATH=choicevar12(sob,'YES','NO')

    sd = st.radio("DO YOU SUFFER FROM SWALLOWING DIFFICULTIES",ch)
    SWALLOWING_DIFFICULTY=choicevar12(sd,'YES','NO')

    cp = st.radio("DO YOU SUFFER FROM CHEST PAIN",ch)
    CHEST_PAIN=choicevar12(cp,'YES','NO')

    predic=Lpredict(GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN)
    if st.button("PREDICT"):    
        if predic==1:
            positiveprogressbar()
            st.error("YOU HAVE LUNG CANCER! PLEASE TAKE CARE OF YOURSELF!")
            st.snow()
        else:
            negativeprogressbar()
            st.success("CONGRATULATIONS ! YOU DON'T HAVE LUNG CANCER ❤️")
            st.balloons()
def Diabetespredict():
    st.markdown("""
    ### :heart: **WELCOME TO DIABETES CHECKING CLINIC** :heart: """,True)
    Pregnancies=st.number_input("ENTER THE NUMBER OF PREGNANCIES",step=1)
    Glucose=st.number_input("ENTER GLUCOSE LEVEL",step=10)
    BloodPressure=st.number_input("ENTER BLOOD PRESSURE",step=10)
    Insulin=st.number_input("ENTER INSULIN AMMOUNT")
    BMI=st.number_input("ENTER BMI",step=10.00,format="%.2f")
    DiabetesPedigreeFunction=st.slider("DIABETES PEDIGREE FUNCTION",min_value=0.000,max_value=1.000,step=0.001)
    Age=st.number_input("ENTER AGE",step=10)
    predic=Dpredict(Pregnancies,Glucose,BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age)
    if st.button("PREDICT"):
        if predic==1:
            positiveprogressbar()
            st.error("YOU HAVE DIABETES! PLEASE TAKE CARE OF YOURSELF!")  
        else:
            negativeprogressbar()
            st.success("CONGRATULATIONS! YOU DON'T HAVE DIABETES ❤️")
            st.balloons()
        
        

def Heartpredict():
    st.markdown("""
    ### :heart: **WELCOME TO HEART DISEASE CHECKING CLINIC** :heart: """,True)
    age= st.number_input("ENTER YOUR AGE",step=00)

    gender=st.radio("GENDER",['MALE','FEMALE'])
    sex=choicevar01(gender,'MALE','FEMALE')   

    CP=st.radio("CHEST PAIN TYPE",['TYPICAL ANGINA','ATYPICAL ANGINA','NON-ANGIAL PAIN','ASYMPTOMATIC'])
    if CP=='TYPICAL ANGINA':
        cp=0
    elif CP=="ATYPICAL ANGINA":
        cp=1
    elif CP=="NON-ANGIAL PAIN":
        cp=2        
    else:
        cp=3

    trestbps = st.number_input("ENTER YOUR RESTING BLOOD PRESSURE",step=10)

    chol= st.number_input("ENTER YOUR SERUM CHOLESTEROL",step=10)

    fb = st.radio("DO YOU HAVE FASTING BLOOD SUGAR > 120 mg/dl",['YES','NO'])
    fbs=choicevar01(fb,'YES','NO')

    rg = st.radio("RESTING ELECTROCARDIOGRAPHIC RESULTS",[0,1,2])
    restecg=rg
    
    thalach	= st.number_input("ENTER HEARTRATE ACHIEVED")

    ex = st.radio("EXERCISE INDUCED ANGINA",['YES','NO'])
    exang=choicevar01(ex,'YES','NO')

    oldpeak =st.number_input("ENTER YOUR ST DEPRESSION INDUCED BY EXERCISE RELATIVE TO REST",format="%.2f",step=0.01)
    
    slope = st.radio("ENTER THE SLOPE OF THE PEAK EXERCISE ST SEGMENT ",[0,1,2])
    
    ca = st.radio("ENTER THE NUMBER OF MAJOR VESSELS COLORED BY FLOUROSCOPY",[0,1,2,3])
 
    s2=" PRESS '0' = normal  '1' = fixed defect  '2' = reversable defect "
    print(s2.center(60))
    
    th = st.radio("ENTER YOUR THALASSEMIA STATUS",['NORMAL','FIXED DEFECT','REVERSABLE DEFECT'])
    if th=='NORMAL':
        thal=0
    elif th=='FIXED DEFECT':
        thal=1
    else:
        thal=2

    predic = Hpredict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)            
    if st.button("PREDICT"):
        if predic==1:
            positiveprogressbar()
            st.error("YOU HAVE HEART DISEASE! PLEASE TAKE CARE OF YOURSELF!")
        else:
            negativeprogressbar()
            st.success("CONGRATUALTIONS! YOU DON'T HAVE HEART DISEASE ❤️")
            st.balloons()

if __name__=='__main__':
    with st.sidebar:
        selected= option_menu(
            menu_title="Main Menu",
            options=["Home","Predictions","Contacts"],
            icons=["house","book","envelope"],
            menu_icon="cast",
            default_index=0,
    )
    st.image('WALLPAPER.jpg',)
    if selected=="Predictions":
        
        choice=st.selectbox("CHOOSE A DISEASE TO PREDICT",['CHOOSE A OPTION','DIABETES','LUNG CANCER','HEART DISEASE'],index=0)
                
        if choice=='DIABETES':
            Diabetespredict()            
        elif choice=='LUNG CANCER':
            Lungpredict()
        elif choice=='HEART DISEASE':
            Heartpredict()
        else:
            print("INVALID CHOICE...!!!")
    elif selected=="Contacts":
        i1,bl,i2=st.columns(3)
        i1.markdown(" ✉️ **ayanacharyya7@gmail.com** ",True)     
        i2.markdown(" 📞 **8910146203** ",True)     
          





























