import streamlit as st
from src.social_media import get_social_mentions,get_hype_score
from src.streaming import get_streaming_platforms
from src.youtube_reviews import get_youtube_review_url
st.set_page_config(page_title="Movie Recommender 5.0",layout="wide")
movies=["Inception","Interstellar","John Wick","Dune Part Two","The Batman"]
st.title("🎬 Movie Recommender 5.0")
tab1,tab2,tab3=st.tabs(["Home","Buzz","Streaming"])
with tab1:
    m=st.selectbox("Movie",movies)
    st.write("Hype Score:",get_hype_score(m))
    st.video(get_youtube_review_url(m))
with tab2:
    m=st.selectbox("Buzz Movie",movies,key="b")
    st.json(get_social_mentions(m))
with tab3:
    m=st.selectbox("Streaming Movie",movies,key="s")
    st.write(", ".join(get_streaming_platforms(m)))
