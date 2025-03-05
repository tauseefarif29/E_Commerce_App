import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title("Streamlit App for E-Commerce")
    st.sidebar.title("Upload Your File")

    uploaded_file = st.sidebar.file_uploader("Upload Your Own File", type = ['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)

            st.sidebar.success("File uploaded successfully")

            st.subheader("Data Overview")
            st.dataframe(data.head())

            st.subheader("Basic Information of the Data")
            st.write("Shape of the data", data.shape)
            st.write("Columns in the Data", data.columns)
            st.write("Missing Values", data.isnull().sum())

            st.subheader("I will show you the stats of the data")
            st.write(data.describe())

        except:
            print("It will handle if things go wrong")


if __name__ == "__main__":
    main() 