
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

    # Show the plot
fig.show()