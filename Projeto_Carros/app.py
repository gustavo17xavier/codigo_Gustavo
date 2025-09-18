import streamlit as st
st.sidebar.title("XAVIER EMPIRE")
st.sidebar.image("logo.png")

carros = ['Bugatti Chiron Super Sport','Pagani Huayra R','McLaren Speedtail','Aston Martin Valkyrie']

opçao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

st.title('XAVIER EMPIRE - Aluguel de Carros de Luxo✨🏎️')

st.image(f'{opçao}.png')
st.markdown(f'## Você alugou o modelo de luxo:  {opçao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opçao}foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opçao}?')
## diaria dos carros
if opçao == 'Bugatti Chiron Super Sport':
    diaria = 50000

elif opçao == 'Pagani Huayra R':
    diaria = 65000

elif opçao == 'McLaren Speedtail':
    diaria = 78000

elif opçao == 'Aston Martin Valkyrie':
    diaria = 89000

### calcular
if st.button('calcular'):
    dias = int(dias)
    km = float(km)


    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opçao} por {dias} dias e rodou {km}km. O valor total a pagar é R$:{aluguel_total:.2f}')