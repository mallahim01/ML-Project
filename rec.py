import streamlit as st
import pickle
import requests

movies=pickle.load(open("moviess.pkl",'rb'))
cs=pickle.load(open("similarityy.pkl",'rb'))
movlst=movies['title'].values




st.markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>", unsafe_allow_html=True)

m=st.selectbox("select movie from dropdown",movlst)

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=39a9bf4f0aff3b43955bb365f4ecbd61".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    dist=sorted(list(enumerate(cs[index])),reverse=True,key=lambda cv:cv[1])
    rec=[]
    pos=[]
    for i in dist[1:6]:
        movies_id=movies.iloc[i[0]].id
        rec.append(movies.iloc[i[0]].title)
        pos.append(fetch_poster(movies_id))
    return rec,pos

if st.button("recommend"):
    m_rec,m_pos=recommend(m)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(m_rec[0])
        st.image(m_pos[0])
    with col2:
        st.text(m_rec[1])
        st.image(m_pos[1])
    with col3:
        st.text(m_rec[2])
        st.image(m_pos[2])
    with col4:
        st.text(m_rec[3])
        st.image(m_pos[3])
    with col5:
        st.text(m_rec[4])
        st.image(m_pos[4])
