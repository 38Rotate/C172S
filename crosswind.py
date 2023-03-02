import math
import streamlit as st

# Define the main function to calculate crosswind component


def crosswind_component(wind_speed, wind_direction, runway_heading):
    # Convert wind direction and runway heading to radians
    wind_direction = math.radians(wind_direction)
    runway_heading = math.radians(runway_heading)

    # Calculate the crosswind angle in radians
    crosswind_angle = wind_direction - runway_heading

    # Calculate the crosswind component in knots
    crosswind_component_kts = abs(wind_speed * math.sin(crosswind_angle))

    # Return the crosswind component in knots
    return crosswind_component_kts

# Define the Streamlit app


def app():
    # Set the app title
    st.title("Crosswind Component Calculator")

    # Create input fields for wind speed, wind direction, and runway heading
    wind_speed = st.number_input(
        "Wind Speed (knots)", min_value=0, max_value=100, step=1)
    wind_direction = st.number_input(
        "Wind Direction (degrees)", min_value=0, max_value=360, step=1)
    runway_heading = st.number_input(
        "Runway Heading (degrees)", min_value=0, max_value=360, step=1)

    # Calculate the crosswind component
    crosswind_kts = crosswind_component(
        wind_speed, wind_direction, runway_heading)

    # Display the crosswind component
    st.write(f"Crosswind Component: {crosswind_kts:.1f} knots")


# Run the Streamlit app
if __name__ == '__main__':
    app()
