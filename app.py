
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("vehicles_us.csv")

# Load the data
vehicles_df = pd.read_csv('vehicles_us.csv')

# Check for missing values
st.write("### Missing Values")
missing_values = vehicles_df.isnull().sum()
st.write(missing_values[missing_values > 0])

display(missing_values)

# Check for duplicates
st.write("### Duplicate Rows")
duplicate_count = vehicles_df.duplicated().sum()
st.write(f"Number of duplicate rows: {duplicate_count}")

display(duplicate_count)

# Detect outliers in numerical columns using IQR
st.write("### Outliers Detection")
numerical_columns = vehicles_df.select_dtypes(include=['int64', 'float64']).columns

outliers_info = {}
for col in numerical_columns:
    Q1 = vehicles_df[col].quantile(0.25)
    Q3 = vehicles_df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = vehicles_df[(vehicles_df[col] < lower_bound) | (vehicles_df[col] > upper_bound)]
    outliers_info[col] = len(outliers)

# Display outlier counts per column
outliers_info = pd.DataFrame.from_dict(outliers_info, orient='index', columns=['Outlier Count'])
st.write(outliers_info.sort_values(by='Outlier Count', ascending=False))

# Fill missing values with the mean for numerical columns
numerical_columns = vehicles_df.select_dtypes(include=['int64', 'float64']).columns
vehicles_df[numerical_columns] = vehicles_df[numerical_columns].fillna(vehicles_df[numerical_columns].mean())

# Fill missing values with mode for non-numerical columns (optional)
categorical_columns = vehicles_df.select_dtypes(include=['object']).columns
vehicles_df[categorical_columns] = vehicles_df[categorical_columns].fillna(vehicles_df[categorical_columns].mode().iloc[0])

# Check for missing values after filling
st.write("### Missing Values After Filling")
st.write(vehicles_df.isnull().sum()[vehicles_df.isnull().sum() > 0])

# Display the cleaned DataFrame
st.write("### Cleaned Data")
st.write(vehicles_df.head())



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

