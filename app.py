# Imports
import streamlit as st

# Creating Functions
def Distance_Converter(from_unit, to_unit, value):
    units = {
        "Metres": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34, 
    }
    
    result = value * units[from_unit]/units[to_unit]
    return result

def Temperature_Converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

def Weight_Converter(from_unit, to_unit, value):
    units = {
        "Kilogram": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    
    result = value * units[from_unit] / units[to_unit]
    return result

def Pressure_Converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000, 
    }
    
    result = value * units[from_unit]/units[to_unit]
    return result 




# Title
st.title("Unit Converter")

# Category
category = st.selectbox("Select Category", ["Distance", "Temperature", "Pressure", "Weight"])

if category == "Distance":
    from_unit = st.selectbox("From", ["Kilometers", "Miles", "Feet", "Metres"])
    to_unit = st.selectbox("To", ["Kilometers", "Miles", "Feet", "Metres"])
    final_value = st.number_input("Enter Input")
    if st.button("Convert"):
        result = Distance_Converter(from_unit, to_unit, final_value)
        st.success(f"{final_value} {from_unit} = {result: .2f} {to_unit}")
        
elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    final_value = st.number_input("Enter Input")
    if st.button("Convert"):
        result = Temperature_Converter(from_unit, to_unit, final_value)
        st.success(f"{final_value} {from_unit} = {result: .1f} {to_unit}")
        
elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilogram", "Pounds", "Grams", "Ounces"])
    to_unit = st.selectbox("To", ["Kilogram", "Pounds", "Grams", "Ounces"])
    final_value = st.number_input("Enter Input")
    result = Weight_Converter(from_unit, to_unit, final_value)
    if st.button("Convert"):
        result = Weight_Converter(from_unit, to_unit, final_value)
        st.success(f"{final_value} {from_unit} = {result: .1f} {to_unit}")
        
elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    final_value = st.number_input("Enter Input")
    result = Pressure_Converter(from_unit, to_unit, final_value)
    if st.button("Convert"):
        result = Pressure_Converter(from_unit, to_unit, final_value)
        st.success(f"{final_value} {from_unit} = {result: .2f} {to_unit}")