import streamlit as st
##coloca um titulo

st. title("titulo da loja")

###escreve
st.write("testando...esquedar e direita")

###cria uma barra lateral
st.sidebar.title("barra lateral")

## criando  a lista
nomes =["uno", "chevette", "mclaren","bugatti"]

    ###cria uma caixa na barra lateral
st.sidebar.selectbox("selecione um nome: " , nomes)