import streamlit as st


st.title('TITULO H1')


n1  = st.number_input('numero:', )
n2  = st.number_input('numero:', value = 0.0)


if st.button('Soma'):
    calcular   =  n1  + n2 
    st.success(calcular)
elif st.button('subtração'):    
    calcular   =  n1  - n2 
    st.success(calcular)    
elif st.button('Divisão'):    
    calcular   =  n1  / n2 
    st.success(calcular)       
elif st.button('Multiplicação'):    
    calcular   =  n1  * n2 
    st.success(calcular)     



#

st.title('O Cartão de Visitas Digital')

st.header('Cartão de visitas')

st.text('Isso é um texto de streamlit')

st.markdown('Isso é um paragrafo de um comentário')

#

st.title('Formulário de Cadastro de Usuário')

st.text_input('nome')

st.number_input('idade')

st.checkbox('termos de uso')

st.button('enviar')

#

import streamlit as st

opition = st.selectbox(
    "Como você gostaria de ser contatado?",
    ("Email", "Telefone fixo", "Telefone móvel"),
)

st.write("você selecionou:", opition)

import streamlit as st

options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options))

#

st.title('Visualizador de Planilhas Interativo')

st.dataframe('')

st.table('')