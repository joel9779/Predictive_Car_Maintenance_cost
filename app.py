
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("vehicles_us.csv")

# Load the data
vehicles_df = pd.read_csv('vehicles_us.csv')


# Filter data for cars with over 200,000 miles
high_mileage_cars = vehicles_df[vehicles_df['odometer'] > 200000]
# Create a histogram of manufacturers for cars with over 200,000 miles
fig = px.histogram(
    high_mileage_cars,
    x="model",
    title="Number of Cars from Manufacturers with Over 200,000 Miles",
    labels={"manufacturer": "Manufacturer"},
    color_discrete_sequence=["blue"]
)
# Update layout for better readability
fig.update_layout(
    xaxis_title="  ",
    yaxis_title="Count of Cars",
    xaxis={'categoryorder': 'total descending'} ) # Sort by count

st.header('Vehicle types by model')
st.write(px.histogram(df, x='model', color='type'))

st.header('Histogram of `High mileage cars`')

# Show the plot
fig.show()

# Filter data for cars with over 200,000 miles
high_mileage_cars = vehicles_df[vehicles_df['odometer'] > 200000]

# Identify the top 5 car models with the most cars over 200,000 miles
top_5_models = (
    high_mileage_cars['model']
    .value_counts()
    .head(5)
    .index.tolist()
)

# Streamlit App
st.title("High Mileage Cars Analysis 2")

# Checkbox to toggle between all models and top 5 models
if st.checkbox("Show Only Top 5 Models"):
    st.write("### Histogram of Vehicle Types for Top 5 Models")
    # Filter data for the top 5 models
    filtered_cars = high_mileage_cars[high_mileage_cars['model'].isin(top_5_models)]
else:
    st.write("### Histogram of Vehicle Types for All Models")
    # Use all high mileage cars
    filtered_cars = high_mileage_cars

# Create the histogram
fig = px.histogram(
    filtered_cars,
    x="model",
    color="type",  # Optionally group by vehicle type
    title="Number of Vehicles by Model and Type",
    labels={"model": "Car Model", "type": "Vehicle Type"},
    barmode="stack",  # Stack bars for clarity
)

# Display the histogram
st.write(fig)


# Filter data for cars with over 200,000 miles
high_mileage_cars = vehicles_df[vehicles_df['odometer'] > 200000]

# Streamlit App
st.title("High Mileage Cars Analysis")

# Scatter plot with Streamlit interaction
if st.checkbox("Show Scatter Plot"):
    st.write("### Scatter Plot of High Mileage Cars")
    
    # Scatter plot: price vs. odometer
    fig = px.scatter(
        high_mileage_cars,
        x="odometer", 
        y="price",
        color="model",  # Optional grouping by manufacturer
        title="Price vs Odometer for High Mileage Cars",
        labels={"odometer": "Odometer (miles)", "price": "Price ($)"}
    )
    
    # Display the plot
    st.write(fig)

