import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header('Interagindo com Gráficos')
st.sidebar.header('Barra de selação')




x= np.linspace(0,2*np.pi,300)

fig,ax = plt.subplots(figsize=(8,6))

def plotFunc():
    ax.plot(x,st.session_state.amp*np.sin(st.session_state.freq*x + st.session_state.fase),st.session_state.color_pick) 

    ax.plot(x,st.session_state.amp*np.cos(st.session_state.freq*x + st.session_state.fase),'red') 

if st.sidebar.checkbox('Mostra Gráfico'):
    plotFunc()
    st.pyplot(fig)
st.write('---')
st.slider('Mudar angulo de fase',min_value=-5.,max_value=5.,step=0.1,on_change=plotFunc,key='fase')
st.slider('Mudar amplitude',min_value=1,max_value=5,step=1,on_change=plotFunc,key='amp')
st.slider('Mudar frequência',min_value=1.,max_value=10.,step=1.,on_change=plotFunc,key='freq')

#st.sidebar.selectbox('Selecione a cor da linha',['red','green','blue'],on_change=plotFunc,key='cor')
st.sidebar.color_picker('Seleção de cores',on_change=plotFunc,key='color_pick')