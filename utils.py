import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
import os  # ✅ 이거 반드시 추가해줘야 함

def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'netflix_titles.csv')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일 없음: {file_path}")

    df = pd.read_csv(file_path)
    return df


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
