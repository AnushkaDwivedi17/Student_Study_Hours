# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pickle
import sklearn
# loading the trained model
reg = pickle.load(open('LR','rb')) 
@st.cache()
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Hours):   

# Making predictions 
    prediction = reg.predict([[Hours]])

    return prediction
# this is the main function in which we define our webpage  
def main():       
# front end elements of the web page 
    html_temp = """ 
        <div style ="background-color:slateblue;padding:13px"> 
        <h1 style ="color:black;text-align:center;">Percentage Prediction ML App</h1> 
        </div> 
        """
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    # following lines create boxes in which user can enter data required to make prediction 
    Hours = st.number_input("How many hours student has studied") 
    result =""
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Hours)
    st.success('Your score is {}'.format(result))
if __name__=='__main__': 
    main()
