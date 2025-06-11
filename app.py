import streamlit as st
from utils import load_data, filter_data_by_genre_year, plot_genre_trend, plot_rating_distribution

st.set_page_config(page_title="넷플릭스 영화 장르 분석", layout="wide")

st.title("넷플릭스 영화 장르 및 평점 분석")

st.markdown("""
넷플릭스 영화 및 TV 프로그램 데이터를 기반으로  
장르별 작품 분포와 평점 분석을 제공합니다.
""")

# 데이터 로드 (캐시됨)
df = load_data()

# 장르 리스트 뽑기
all_genres = sorted({genre for sublist in df['genres'] for genre in sublist if sublist})

# 사용자 입력 위젯
selected_genre = st.selectbox("장르 선택", all_genres)

min_year = int(df['year'].min())
max_year = int(df['year'].max())
selected_year = st.slider("출시 연도 범위 선택", min_year, max_year, (min_year, max_year))

# 데이터 필터링
filtered_df = filter_data_by_genre_year(df, selected_genre, selected_year)

st.subheader(f"{selected_genre} 장르 작품 연도별 분포")
fig1 = plot_genre_trend(filtered_df, selected_genre)
st.plotly_chart(fig1, use_container_width=True)

st.subheader(f"{selected_genre} 장르 작품 평점 분포")
fig2 = plot_rating_distribution(filtered_df)
st.plotly_chart(fig2, use_container_width=True)

st.subheader(f"{selected_genre} 장르 작품 리스트 ({len(filtered_df)}개)")
st.dataframe(filtered_df[['title', 'year', 'rating', 'duration', 'description']].reset_index(drop=True))
