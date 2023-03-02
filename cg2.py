import streamlit as st


def calculate_cg(front_seat_weight, rear_seat_weight, fuel_weight, baggage_weight_a, baggage_weight_b):
    # preprogrammed C172S CG values
    front_seats_cg = 37  # 36-46
    rear_seats_cg = 73  # 73
    fuel_cg = 48.0  # 48
    bag_a = 95.0  # 82-108
    bag_b = 123  # 108-142
    empty_cg = 46.0  # 46

    # calculate weight moments and total weight
    front_seat_moment = front_seat_weight * front_seats_cg
    rear_seat_moment = rear_seat_weight * rear_seats_cg
    fuel_moment = fuel_weight * fuel_cg
    baggage_moment_a = baggage_weight_a * bag_a
    baggage_moment_b = baggage_weight_b * bag_b

    total_weight = front_seat_weight + rear_seat_weight + \
        fuel_weight + baggage_weight_a + baggage_weight_b
    total_moment = front_seat_moment + rear_seat_moment + \
        fuel_moment + baggage_moment_a + baggage_moment_b

    # calculate center of gravity (CG)
    cg = total_moment / total_weight

    # print CG result
    st.write(
        "The center of gravity for your Cessna 172 is {:.2f} inches from the reference datum.".format(cg))

    if cg > 35 and cg < 47.33:
        st.write("CG requirement is satisfied")
    else:
        st.write("CG requirement is not satisfied")


# Streamlit app UI
st.title("Cessna 172 Center of Gravity Calculator")
st.write("Enter the weight of the passengers, fuel, and baggage to calculate the center of gravity.")

front_seat_weight = st.number_input("Front seat passengers (lbs): ", value=0.0)
rear_seat_weight = st.number_input(
    "Rear seat passengers or bags (lbs): ", value=0.0)
fuel_weight = st.number_input("Fuel (lbs): ", value=0.0)
baggage_weight_a = st.number_input(
    "Enter front baggage weight (lbs): ", value=0.0)
baggage_weight_b = st.number_input(
    "Enter rear baggage weight (lbs): ", value=0.0)

if st.button("Calculate CG"):
    calculate_cg(front_seat_weight, rear_seat_weight,
                 fuel_weight, baggage_weight_a, baggage_weight_b)
