import pickle
import streamlit as st

model = pickle.load(open('estimasi_FishWeight.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Bobot Ikan Di Pasar')


Length1 = st.number_input('Input Length1')
Length2 = st.number_input('Input Length2')
Length3 = st.number_input('Input Length3')
Height = st.number_input('Input Height')
Width = st.number_input('Input Width')

predict = ''

if st.button('Cek bobot'):
    predict = model.predict(
        [[Length1,Length2,Length3,Height,Width]]
    )
    st.write ('Estimasi jumlah Bobot Ikan : ', predict)