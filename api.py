import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for next days")
place = st.text_input("place: ")
days = st.slider("Forecast Days ", min_value= 1, max_value=5, help= "Select number of forecast days")
option = st.selectbox("Select data to view", ("temperature","Sky"))
st.subheader(f" {option} for the next {days} days in  {place} ")

if place :

    try:
        filtered_data=get_data(place, days)



        filter_data = get_data(place, days)

        if option == "temperature":
           temperatures =  [dict["main"]["temp"] /10 for dict in filter_data]
           dates= [dict["dt_txt"] for dict in filter_data]

           figure = px.line(x= dates, y= temperatures, labels={"x": "Date", "y": "Temperature (C)"})
           st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filter_data]
            image_paths = [images[condition] for condition in sky_conditions]

            st.image(image_paths, width =80)
    except KeyError:
        st.write("Entered place doesn't exist")


