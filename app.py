import streamlit as st


def piadina(num):
    pesototale = 90 * num
    acqua = pesototale / 3
    farina = pesototale - acqua
    return pesototale, farina, acqua


def pizza(tot):
    teglia_1 = (14 / 100) * tot
    teglia_2 = (25 / 100) * tot
    teglia_3 = (28 / 100) * tot
    teglia_4 = (33 / 100) * tot
    return teglia_1, teglia_2, teglia_3, teglia_4


st.title("Piadina/Pizza Calculator")

option = st.radio("Select", ["Piadina", "Pizza"])

if option == 'Piadina':
    with st.form("piadina_form"):
        num_piadine = st.number_input('Quante piadine vuoi fare?', min_value=1)
        submitted = st.form_submit_button("Calculate")

        if submitted:
            peso, farina, acqua = piadina(num_piadine)
            st.write(f'Peso totale: {peso} g')
            st.write(f'Farina: {farina} g')
            st.write(f'Acqua: {acqua} g')

elif option == 'Pizza':
    with st.form("pizza_form"):
        tot_grammi = st.number_input('Grammi totali?', min_value=1)
        submitted = st.form_submit_button("Calculate")

        if submitted:
            t1, t2, t3, t4 = pizza(tot_grammi)
            st.write(f'Quadrata piccola: {t1} g')
            st.write(f'Quadrata media: {t2} g')
            st.write(f'Rettangolare media: {t3} g')
            st.write(f'Rettangolare grande: {t4} g')
