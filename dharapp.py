import streamlit as st  # Import Streamlit library for creating web apps
import pandas as pd  # Import Pandas library for data manipulation
import plotly.express as px  # Importing Plotly Express for interactive plotting

# Load data from CSV file into a Pandas DataFrame
df = pd.read_csv("Hazardous waste per capita-Global Analysis.csv")


# Set page title and icon for the Streamlit app
st.set_page_config(page_title='Hazardous Waste Global Analysis', page_icon=':chart_with_upwards_trend:')

# Welcome message
st.write("""
# Welcome to Streamlit!
## Global Analysis for Hazardous Waste Generation per Capita
""")

# Sidebar filters setup section
st.sidebar.title('Filters')  # Title for the sidebar section

# Filter by country using a multi-select dropdown
countries = st.sidebar.multiselect('Select countries', df['Countries'].unique())

# Filter by year range using a slider
year_min = int(df['Year'].min())  # Minimum year from the dataset
year_max = int(df['Year'].max())  # Maximum year from the dataset
year_range = st.sidebar.slider('Select year range', year_min, year_max, (year_min, year_max))  # Year range slider

# Apply filters to the main DataFrame
filtered_df = df[(df['Countries'].isin(countries)) & (df['Year'].between(year_range[0], year_range[1]))]

# Main content section
# Display filtered data with a red-colored subheader on a black background
st.markdown('<h2 style="color: red; background-color: black;">Filtered Data</h2>', unsafe_allow_html=True)
st.write(filtered_df)

# Visualization section
# Display visualization subheader with red-colored text on a black background
st.markdown('<h2 style="color: red; background-color: black;">Visualization</h2>', unsafe_allow_html=True)

# Choose chart type via a dropdown selector
chart_type = st.selectbox('Select chart type', ['Line Chart', 'Bar Chart'])

# Plot based on selected chart type
if chart_type == 'Line Chart':
    fig = px.line(filtered_df, x='Year', y='Hazardous waste generated, per capita (Kg)', color='Countries',
                  title='Hazardous Waste Generation per Capita Over Years')  # Line chart plotting hazardous waste per capita over years
elif chart_type == 'Bar Chart':
    fig = px.bar(filtered_df, x='Year', y='Hazardous waste generated, per capita (Kg)', color='Countries',
                 title='Hazardous Waste Generation per Capita Over Years')  # Bar chart plotting hazardous waste per capita over years

# Display the selected chart
st.plotly_chart(fig)

# Additional insights section
# Checkbox is created to toggle display of additional insights if wanted
if st.checkbox('Show Additional Insights'):
    # Display average hazardous waste per capita with a red-colored subheader on a black background
    st.markdown('<h2 style="color: red; background-color: black;">Average Hazardous Waste per Capita</h2>', unsafe_allow_html=True)
    avg_per_country = filtered_df.groupby('Countries')['Hazardous waste generated, per capita (Kg)'].mean().reset_index()
    st.write(avg_per_country)

    # Display top countries by hazardous waste with a red-colored subheader on a black background
    st.markdown('<h2 style="color: red; background-color: black;">Top Countries by Hazardous Waste</h2>', unsafe_allow_html=True)
    top_countries = avg_per_country.sort_values(by='Hazardous waste generated, per capita (Kg)', ascending=False).head(5)
    st.write(top_countries)

# Footer section
st.sidebar.markdown("---")  # Divider line in the sidebar
st.sidebar.markdown("This dashboard is created by Dharsheeni Kanthiah")  # Footer text in the sidebar
