import streamlit as st
import pickle

# Load the trained model
with open('Water_Portability_Model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the Streamlit app
st.title('Water Portability Prediction')
# Create input fields for the features
ph = st.number_input('pH', min_value=0.0, max_value=14.0, step=0.1)
Hardness = st.number_input('Hardness', min_value=0.0, step=0.1)
Chloramines = st.number_input('Chloramines', min_value=0.0, step=0.1)
Organic_carbon = st.number_input('Organic Carbon', min_value=0.0, step=0.1)
Turbidity = st.number_input('Turbidity', min_value=0.0, step=0.1)

# Create a button to make the prediction
if st.button('Predict'):
    # Prepare the input data for prediction
    input_data = [[ph, Hardness, Chloramines, Organic_carbon, Turbidity]]
    
    # Make the prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Display the prediction result
    if prediction[0] == 1:
        st.success('The water quality is good.')
    else:
        st.error('The water quality is poor.')        