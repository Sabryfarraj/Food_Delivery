import streamlit as st
import joblib
import pandas as pd

# Load the pipeline and feature configurations
pipeline = joblib.load("final_pipeline.pkl")
min_max_values = joblib.load('min_max_values.pkl')
unique_values = joblib.load('unique_values.pkl')

def get_part_of_day(hour):
    # Define time ranges
    night_start = pd.to_datetime('00:00:00', format='%H:%M:%S').time()
    night_end = pd.to_datetime('06:00:00', format='%H:%M:%S').time()
    
    morning_start = pd.to_datetime('06:00:00', format='%H:%M:%S').time()
    morning_end = pd.to_datetime('12:00:00', format='%H:%M:%S').time()
    
    afternoon_start = pd.to_datetime('12:00:00', format='%H:%M:%S').time()
    afternoon_end = pd.to_datetime('18:00:00', format='%H:%M:%S').time()
    
    evening_start = pd.to_datetime('18:00:00', format='%H:%M:%S').time()
    evening_end = pd.to_datetime('23:59:59', format='%H:%M:%S').time()
    
    # Convert hour to a time object
    time = pd.to_datetime(f'{hour:02}:00:00', format='%H:%M:%S').time()
    
    # Categorize based on time ranges
    if night_start <= time < night_end:
        return 'Night'
    elif morning_start <= time < morning_end:
        return 'Morning'
    elif afternoon_start <= time < afternoon_end:
        return 'Afternoon'
    elif evening_start <= time <= evening_end:
        return 'Evening'
    else:
        return 'Unknown'  # Handle unexpected cases

def prediction(Delivery_person_Age, Delivery_person_Ratings, Vehicle_condition, multiple_deliveries, distance_km, Hour_Placed, Weatherconditions, Road_traffic_density, Type_of_vehicle, Festival, City):
    Part_Of_Day = get_part_of_day(Hour_Placed)  # Automatically determine Part of Day
    
    # Create a DataFrame for the input features
    df = pd.DataFrame({
        'Delivery_person_Age': [Delivery_person_Age],
        'Delivery_person_Ratings': [Delivery_person_Ratings],
        'Vehicle_condition': [Vehicle_condition],
        'multiple_deliveries': [multiple_deliveries],
        'distance_km': [distance_km],
        'Hour_Placed': [Hour_Placed],
        'Weatherconditions': [Weatherconditions],
        'Road_traffic_density': [Road_traffic_density],
        'Type_of_vehicle': [Type_of_vehicle],
        'Festival': [Festival],
        'City': [City],
        'Part_Of_Day': [Part_Of_Day]
    })
    
    # Use the pipeline to make a prediction
    result = pipeline.predict(df)
    
    return result[0]

def main():
    # Set the title and description of the app
    st.title("Food Delivery ETA Prediction")
    st.markdown("""
    Welcome to the Food Delivery ETA Prediction app! 🚚
    
    This application estimates the time taken for food delivery based on various input features. 
    Use the controls below to provide the input data and click the "Get Prediction" button to get the estimate.
    """)

    # Split the page into two columns
    col1, col2 = st.columns(2)
    
    # Column 1: Numeric inputs
    with col1:
        
        Delivery_person_Age = st.slider(
            "Delivery Person Age",
            min_value=int(min_max_values['Delivery_person_Age'][0]),
            max_value=int(min_max_values['Delivery_person_Age'][1]),
            step=1,
            value=int((min_max_values['Delivery_person_Age'][0] + min_max_values['Delivery_person_Age'][1]) / 2)
        )
        
        Delivery_person_Ratings = st.slider(
            "Delivery Person Ratings",
            min_value=float(min_max_values['Delivery_person_Ratings'][0]),
            max_value=float(min_max_values['Delivery_person_Ratings'][1]),
            step=0.1,
            value=float((min_max_values['Delivery_person_Ratings'][0] + min_max_values['Delivery_person_Ratings'][1]) / 2)
        )
        
        Vehicle_condition = st.slider(
            "Vehicle Condition",
            min_value=int(min_max_values['Vehicle_condition'][0]),
            max_value=int(min_max_values['Vehicle_condition'][1]),
            step=1,
            value=int((min_max_values['Vehicle_condition'][0] + min_max_values['Vehicle_condition'][1]) / 2)
        )
        
        multiple_deliveries = st.slider(
            "Multiple Deliveries",
            min_value=int(min_max_values['multiple_deliveries'][0]),
            max_value=int(min_max_values['multiple_deliveries'][1]),
            step=1,
            value=int((min_max_values['multiple_deliveries'][0] + min_max_values['multiple_deliveries'][1]) / 2)
        )
        
        distance_km = st.slider(
            "Distance (km)",
            min_value=float(min_max_values['distance_km'][0]),
            max_value=float(min_max_values['distance_km'][1]),
            step=0.1,
            value=float((min_max_values['distance_km'][0] + min_max_values['distance_km'][1]) / 2)
        )
        
        Festival = st.radio(
            "Festival",
            unique_values['Festival']
        )
        
    # Column 2: Categorical inputs
    with col2:
        
        Weatherconditions = st.selectbox(
            "Weather Conditions",
            unique_values['Weatherconditions']
        )
        
        Road_traffic_density = st.radio(
            "Road Traffic Density",
            unique_values['Road_traffic_density']
        )
        
        Type_of_vehicle = st.radio(
            "Type of Vehicle",
            unique_values['Type_of_vehicle']
        )
        
        City = st.radio(
            "City",
            unique_values['City']
        )
        
        Hour_Placed = st.slider(
            "Hour Placed",
            min_value=int(min_max_values['Hour_Placed'][0]),
            max_value=int(min_max_values['Hour_Placed'][1]),
            step=1,
            value=int((min_max_values['Hour_Placed'][0] + min_max_values['Hour_Placed'][1]) / 2)
        )
      
         # Display Part of Day directly below Hour Placed
        part_of_day = get_part_of_day(Hour_Placed)
        st.write(f"**Part of Day:** {part_of_day}")
    
    if st.button("Predict"):
        result = prediction(
            Delivery_person_Age, Delivery_person_Ratings, Vehicle_condition, multiple_deliveries,
            distance_km, Hour_Placed, Weatherconditions, Road_traffic_density, Type_of_vehicle,
            Festival, City
        )
        st.text(f"The Estimated Time of Arrival is:\n {round(result , 1)} minutes")

# Run the Streamlit app
main()
