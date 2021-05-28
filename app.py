import streamlit as st
import datetime
import requests


''' # TaxiFareModel front '''

date = st.date_input("On what day would you like to get picked up?")
time = st.time_input('At what time would you like to get picked up?')
pickup_time = date.strftime("%Y-%m-%d") + ' ' + time.strftime("%H:%M:%S")

pickup_longitude = st.number_input('Insert the Pickup Longitude', 40.7614327)
pickup_latitude = st.number_input('Insert the Pickup Latitude', -73.9798156)
dropoff_longitude = st.number_input('Insert the Dropoff Longitude', 40.6513111)
dropoff_latitude = st.number_input('Insert Dropoff Latitude', -73.8803331)

passenger_count = st.number_input('How many people are you travelling with?', 2)

# url = 'https://taxifare.lewagon.ai/predict'
url = "https://taxifare-api-n3bfhtw63q-ew.a.run.app/predict"

data = dict(
    pickup_datetime = pickup_time, 
    pickup_longitude = pickup_longitude, 
    pickup_latitude = pickup_latitude, 
    dropoff_longitude = dropoff_longitude,
    dropoff_latitude = dropoff_latitude,  
    passenger_count = passenger_count
)

response = requests.get(
    url, 
    params=data
)

if response.status_code == 200: 
    print("Success")
else: 
    print("Error")
    
# response.status_code, response.json().get("prediction", "no prediction"), response.json()

json_response = response.json()
prediction = round(json_response["prediction"], 2)

st.markdown(f"### Your Fare will cost approximately {prediction} dollars")





"___"

show_instructions = st.checkbox('Show Instructions')

markdown_instructions = st.empty()
controller_instructions = st.empty()
api_instructions = st.empty()

if show_instructions: 
    markdown_instructions.markdown('''
        Remember that there are several ways to output content into your web page...

        Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
        ''')
    
    controller_instructions.markdown('''
        ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

        1. Let's ask for:
        - date and time
        - pickup longitude
        - pickup latitude
        - dropoff longitude
        - dropoff latitude
        - passenger count
        ''')
    
    api_instructions.markdown('''
        ## Once we have these, let's call our API in order to retrieve a prediction

        See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

        🤔 How could we call our API ? Off course... The `requests` package 💡

        2. Let's build a dictionary containing the parameters for our API...

        3. Let's call our API using the `requests` package...

        4. Let's retrieve the prediction from the **JSON** returned by the API...

        ## Finally, we can display the prediction to the user
        ''')
    
    
