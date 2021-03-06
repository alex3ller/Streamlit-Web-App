import streamlit as st 
import pandas


data = {
  'Series_1':[1, 3, 4, 5, 7],
  'Series 2':[10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our first Web App.
Enjoy it!
''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)


with open("report.pdf", "rb") as file:
     btn = st.download_button(
             label="Download Report",
             data=file,
             file_name="report.pdf",
             mime="application/pdf"
           )

username = st.text_input('Username', '')
password = st.text_input('Password', '')
st.write('Username is ', username)
st.write('Password is ', password)