import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Student Performance")
df = pd.read_csv('StudentsPerformance.csv')

# DATA CLEANING IS DONE HERE

# st.write(df.isna().sum())
# st.write(df.duplicated().sum())

# VISUALIZATION FUNCTIONS
# st.write(df.columns)
def plot_math_score_distribution():
    plt.figure(figsize=[10,6])
    plt.hist(df['math score'], bins=15, color='blue', edgecolor='black')
    plt.title('Distribution of Math Score')
    plt.xlabel('Math Score')
    plt.ylabel('Frequency')
    st.pyplot(plt)

def plot_scores_by_Gender():
    plt.figure(figsize=(12,8))
    df.boxplot(column=['math score','reading score','writing score'], by='gender')
    plt.title('Score by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Scores')
    st.pyplot(plt)

def math_vs_reading():
    plt.figure(figsize=(10,6))
    plt.scatter(df['math score'],df['reading score'],alpha=0.5,color='green')
    plt.title('Math Score vs Reading Score')
    plt.xlabel('Math Score')
    plt.ylabel('Reading Score')
    st.pyplot(plt)

st.title('Student Performance Analysis')
st.write('This web application allows you to explore and visualize the "Students Performance Dataset". You can view various plots to analyze how different factors affect student performance.')

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(df)

st.sidebar.header('Choose Visualization')
visualization = st.sidebar.selectbox('Select a plot Type:',['Math Score Distribution','Scores by Gender','Math vs Reading Score'])

if visualization == 'Math Score Distribution':
    st.subheader('Distribution of Math Scores:') 
    plot_math_score_distribution()
elif visualization == 'Scores by Gender':
    st.subheader('Scores by Gender:')
    plot_scores_by_Gender()
elif visualization == 'Math vs Reading Score':
    st.subheader('Math Score vs. Reading Score')
    math_vs_reading()