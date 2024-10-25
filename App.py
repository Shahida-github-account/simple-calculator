import streamlit as st

# Simple Calculator using Streamlit

# Set up title and description
st.title("Simple Calculator")
st.write("Select an operation and enter two numbers to calculate.")

# Select operation
operation = st.selectbox("Choose an operation:", ['Addition', 'Subtraction', 'Multiplication', 'Division'])

# Input numbers
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Perform calculation based on user input
if st.button("Calculate"):
    if operation == 'Addition':
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == 'Subtraction':
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == 'Multiplication':
        result = num1 * num2
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {num1} / {num2} = {result}")
        else:
            st.write("Error! Division by zero.")

# Footer
st.write("Thank you for using the Simple Calculator!")
