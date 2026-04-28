import streamlit as st
from src.helpers import streaming,buzz

st.set_page_config(page_title='Movie Recommender 6.0',layout='wide')
st.markdown('''
<style>
.stApp {background: linear-gradient(135deg,#050816,#0b1026,#111827); color:white;}
.block-container {padding-top:2rem;}
div[data-testid="stMetric"] {background:rgba(255,255,255,0.05);padding:15px;border-radius:16px;border:1px solid #1e40af;}
h1,h2,h3 {color:#60a5fa;}
.stButton>button {background:#2563eb;color:white;border-radius:12px;border:none;}
</style>
''', unsafe_allow_html=True)

movies=['Inception','Interstellar','John Wick','Dune Part Two','The Batman','Blade Runner 2049']
st.title('🎬 Movie Recommender 6.0')
st.caption('Futuristic AI Neon Edition')

tabs=st.tabs(['Home','Recommend','Streaming','Buzz','Watchlist'])

with tabs[0]:
    st.header('Hero Picks')
    cols=st.columns(3)
    for i,m in enumerate(movies[:3]):
        cols[i].metric(m, 'Trending')

with tabs[1]:
    mood=st.selectbox('Choose vibe',['Mind-bending','Action','Dark','Sci-Fi'])
    if st.button('Generate Recommendations'):
        st.success('AI selected:')
        for m in movies:
            st.write('•',m)

with tabs[2]:
    m=st.selectbox('Movie',movies,key='s')
    st.write(', '.join(streaming(m)))

with tabs[3]:
    m=st.selectbox('Buzz Movie',movies,key='b')
    data=buzz(m)
    c1,c2,c3=st.columns(3)
    c1.metric('X',data['X'])
    c2.metric('Reddit',data['Reddit'])
    c3.metric('Instagram',data['Instagram'])

with tabs[4]:
    st.info('Save favorites in next version with database login.')
    for m in movies[:4]:
        st.checkbox(m)
