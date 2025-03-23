import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🏋️‍♂️",
    layout="centered"
)

# Add custom CSS for responsiveness
st.markdown("""
    <style>
    .main {
        padding: 20px;
        max-width: 800px;
        margin: 0 auto;
    }
    .stTextInput, .stNumberInput {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("BMI Calculator 💪")
st.markdown("Calculate your Body Mass Index (BMI) to check if you're at a healthy weight.")

# Input fields
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=500.0, value=70.0)

with col2:
    height = st.number_input("Enter your height (cm)", min_value=1.0, max_value=300.0, value=170.0)

# Calculate button
if st.button("Calculate BMI"):
    # Add a loading spinner
    with st.spinner("Calculating..."):
        time.sleep(1)  # Simulate calculation time
        
        # Calculate BMI
        height_m = height / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        
        # Display result
        st.success(f"Your BMI is: {bmi:.1f}")
        
        # BMI Categories
        if bmi < 18.5:
            category = "Underweight"
            color = "🔵"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            color = "✅"
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "🟡"
        else:
            category = "Obese"
            color = "🔴"
        
        st.markdown(f"### Category: {color} {category}")
        
        # BMI Chart
        st.markdown("""
        ### BMI Categories:
        - Underweight: < 18.5 🔵
        - Normal weight: 18.5 - 24.9 ✅
        - Overweight: 25 - 29.9 🟡
        - Obese: ≥ 30 🔴
        """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 