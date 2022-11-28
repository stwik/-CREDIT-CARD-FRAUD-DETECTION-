import streamlit as st
import pandas as pd
import pickle
import random
st.title("CREDIT CARD FRAUD DETECTION")
x_test=pd.read_csv("x_test1.csv")
pickle_in= open('lr_class.pkl', 'rb')
model = pickle.load(pickle_in)
def log_reg_predict_fake(credit_card):
    X_test_prediction = model.predict(credit_card)
    ret=X_test_prediction.astype(int)
    return (ret)  
pickle_in1= open('knn_class.pkl', 'rb')
model1 = pickle.load(pickle_in1)
def knn_predict_fake(credit_card):
    X_test_prediction = model1.predict(credit_card)
    ret=X_test_prediction.astype(int)
    return(ret)
pickle_in2= open('dt_class.pkl', 'rb')
model2= pickle.load(pickle_in2)
def dt_for_predict_fake(credit_card):
    X_test_prediction = model2.predict(credit_card)
    ret=X_test_prediction.astype(int)
    return(ret)
pickle_in3= open('rf_class.pkl', 'rb')
model3 = pickle.load(pickle_in3)
def rf_predict_fake(credit_card):
    X_test_prediction = model3.predict(credit_card)
    ret=X_test_prediction.astype(int)
    return(ret)
pickle_in4= open('svm_class.pkl', 'rb')
model4 = pickle.load(pickle_in4)
def svm_predict_fake(credit_card):
    X_test_prediction = model4.predict(credit_card)
    ret=X_test_prediction.astype(int)
    return(ret)   
pickle_in5=open('mlp_class.pkl','rb') 
model5=pickle.load(pickle_in5)   
def mlp_predict_fake(credit_card):
    X_test_prediction = model5.predict(credit_card)
    ret=X_test_prediction.astype(int)
    return(ret)
if 'random' not in st.session_state:
    st.session_state['random'] = random.randint(0,199)
def gapproach(s):
    if len(s):
        s = s.replace(' ','')
        print('Input is ',s)
        l=list(map(int, list(s)))
        print('Input is ',l)
        checkBit=int(s[-1])
        for i in range(len(s)):
            if(s[i]!=" "):
                l.append(int(s[i]))
        sum=0
        for i in range(0,len(l)):
            if(i%2==0):
                temp=2*l[i]
                if(temp>=10):
                    temp=temp%10+temp//10
                    sum+=temp
                else:
                    sum+=temp  
            else:
                sum+=l[i]
        if((sum+checkBit)%10==0):
            return("original")
        else:
            return("fake")

print('test', gapproach('1234 4321 1234 4321'))

credit_card = x_test.sample(n=1, random_state=st.session_state['random'] )
con = st.container()
st.image('/Users/tarunkumar/Desktop/Credit-Cards_Merithew.jpg',use_column_width=True)
st.title("Generic approach")
ga=st.button("click here to predict by using generic approach")
if ga:
    s=st.text_input("Enter the credit card number:")
    if s:
        result = gapproach(s)
        st.success("The predicted result is: {}".format(result))
st.title("Machine learning approach")    

col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
op1 = col1.button("Logistic Regression")
op2 = col2.button("K-Means Clustering")
op3 = col3.button("Decision Tree")
op4 = col4.button("RANDOM FOREST")
op5=  col4.button("SUPPORT VECTOR MACHINE")
op6=  col4.button("MULTI LAYER PERCEPTRON")
if op1 :
    result=log_reg_predict_fake(credit_card)
    if result==1:
        st.success("The credit card is fake")
    else:
        st.success("The credit card is original")    
    st.info("Logistic Regression")
    st.write(credit_card)
elif op2 :
    result=knn_predict_fake(credit_card)
    if result==1:
        st.success("The credit card is fake")
    else:
        st.success("The credit card is original")
    st.info("K-Means Clustering")
    st.write(credit_card)
    
elif op3 :
    result=dt_for_predict_fake(credit_card)
    if result==1:
        st.success("The credit card is fake")
    else:
        st.success("The credit card is original")
    st.info("Decision Tree")
    st.write(credit_card)
elif op4 :
    result=rf_predict_fake(credit_card)
    if result==1:
        st.success("The credit card is fake")
    else:
        st.success("The credit card is original")
    st.info("Random Forest")
    st.write(credit_card)
elif op5 :
    result=svm_predict_fake(credit_card)
    if result==1:
        st.success("The credit card is fake")
    else:
        st.success("The credit card is original")
    st.info("Support vector machine")
    st.write(credit_card)
elif op6 :
    result=mlp_predict_fake(credit_card)
    if result==1:
        st.success("The credit card is fake")
    else:
        st.success("The credit card is original")
    st.info("Multi Layer Perceptron")
    st.write(credit_card)
else:
    st.write("Select an option")
b1=st.button("click here to see the result of logistic regression")
if b1:
    st.image("/Users/tarunkumar/Desktop/mini_project/lr.png",use_column_width=True)
b2=st.button("click here to see the result of KNN")
if b2:
    st.image("/Users/tarunkumar/Desktop/mini_project/knn.png",use_column_width=True)     
b3=st.button("click here to see the result of Decision Tree")
if b3:
    st.image("/Users/tarunkumar/Desktop/mini_project/dt.png",use_column_width=True)
b4=st.button("click here to see the result of Random Forest")
if b4:
     st.image("/Users/tarunkumar/Desktop/mini_project/rf.png",use_column_width=True)
b5=st.button("click here to see the result of Support Vector Machine")
if b5:
    st.image("/Users/tarunkumar/Desktop/mini_project/svm.png",use_column_width=True)
b6=st.button("click here to see the result of Multi Layer Perceptron")
if b6:
    st.image("/Users/tarunkumar/Desktop/mini_project/mlp.png",use_column_width=True)
 