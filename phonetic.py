import epitran
import eng_to_ipa
import streamlit as st


def idiomas():
    thisdict = {
        "Catalan": "cat-Latn",
        "Czech": "ces-Latn",
        "German": "deu-Latn",
        "Farsi": "fas-Arab",
        "French": "fra-Latn",
        "English": "en-Latn",
        "Italian": "ita-Latn",
        "Dutch": "nld-Latn",
        "Polish": "pol-Latn",
        "Portuguese": "por-Latn",
        "Romanian": "ron-Latn",
        "Russian": "rus-Cyrl",
        "Spanish": "spa-Latn",
        "Swedish": "swe-Latn",
        "Spanish": "spa-Latn",
        "Ukranian": "spa-Latn"}
    return thisdict.keys()

def english_ipa(frase):
    phonetica = eng_to_ipa.convert(frase)
    return phonetica 

def fonetica(lenguage,frase):
    thisdict = {
        "Catalan": "cat-Latn",
        "Czech": "ces-Latn",
        "German": "deu-Latn",
        "Farsi": "fas-Arab",
        "French": "fra-Latn",
        "Italian": "ita-Latn",
        "Dutch": "nld-Latn",
        "Polish": "pol-Latn",
        "Portuguese": "por-Latn",
        "Romanian": "ron-Latn",
        "Russian": "rus-Cyrl",
        "Spanish": "spa-Latn",
        "Swedish": "swe-Latn",
        "Spanish": "spa-Latn",
        "Ukranian": "spa-Latn"}
    
    if lenguage == "English":
        phonetics = english_ipa(frase)
    else:
        epi_instance = epitran.Epitran(thisdict[lenguage])
        phonetics = epi_instance.transliterate(frase)
    return phonetics


def main():
    
    lenguages = idiomas()
    
    # Titulo de la aplicación
    col1, col2 , col3 = st.columns([1,2,1])
    with col1:
        st.write('')
    with col2:
        st.header('FONETICA')
    with col3:
        st.write('')

    # Selección del idioma
    col1, col2 , col3 = st.columns([1,2,1])
    with col1:
        st.write('')
    with col2:
        idioma = st.selectbox('IDIOMA', lenguages)
    with col3:
        st.write('')

    # Entrada de texto y traduccion
    col1, col2 = st.columns(2)
    with col1:
        frase = st.text_area(label= '', value="", height=100,max_chars=300,key='f_origen')
    with col2:
        frase_traducida = fonetica(idioma,frase)
        ver_traduccion = st.text_area(label= '', value= frase_traducida, height=100,key='f_traducida')




if __name__ == "__main__":
    main()




