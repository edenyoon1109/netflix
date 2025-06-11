import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv('data/netflix_titles.csv')
    df['year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
    df['genres'] = df['listed_in'].str.split(', ')
    df['rating'] = df['rating'].fillna('Unknown')
    return df.dropna(subset=['year'])

def filter_data_by_genre_year(df, genre, year_range):
    return df[
        (df['genres'].apply(lambda g: genre in g)) &
        (df['year'].between(year_range[0], year_range[1]))
    ]

def plot_genre_trend(df, genre):
    yearly_counts = df['year'].value_counts().sort_index()
    fig = px.bar(
        x=yearly_counts.index,
        y=yearly_counts.values,
        labels={'x': '출시 연도', 'y': '작품 수'},
        title=f'{genre} 장르 연도별 작품 수'
    )
    return fig

def plot_rating_distribution(df):
    rating_counts = df['rating'].value_counts()
    fig = px.bar(
        x=rating_counts.index,
        y=rating_counts.values,
        labels={'x': '평점', 'y': '작품 수'},
        title='평점 분포'
    )
    return fig
