import pandas as pd
import plotly.express as px
import streamlit as st
import os

@st.cache_data
def load_data():
    # Streamlit에서는 현재 실행 경로 기준으로 상대경로 사용이 더 안전합니다.
    csv_path = os.path.join("netflix_titles.csv")
    
    # 파일 존재 여부 확인
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"'{csv_path}' 파일을 찾을 수 없습니다. Streamlit에 올렸는지 확인하세요.")
    
    df = pd.read_csv(csv_path)
    df.dropna(subset=['title', 'type', 'release_year', 'rating'], inplace=True)
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
