import streamlit as st
from PIL import Image
from PIL import ImageFilter

st.set_page_config(page_title='SteamLit Image Editor')

st.markdown("<h1 style='text-align:center;'>StreamLit Image Editor</h1>", unsafe_allow_html=True)
st.markdown('---')
userimage = st.file_uploader('Upload your Image', type=['jpg', 'png', 'jpeg', 'webp'])
if userimage is not None:
    img = Image.open(userimage)
    imageholder = st.image(img)
    colx, coly = st.columns(2)
    colx.markdown(f'Image Mode: {img.mode} {img.format}')
    coly.markdown(f'Image Size: {img.size}')

    st.markdown("<h2 style='text-align:center'>Resizing</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    height = col1.number_input('Enter Height', value=img.width)
    width = col2.number_input('Enter Width', value=img.height)

    st.markdown("<h2 style='text-align:center'>Rotation</h2>", unsafe_allow_html=True)
    degree = st.number_input('Enter degree')

    st.markdown("<h2 style='text-align:center'>Filters</h2>", unsafe_allow_html=True)
    filters = st.selectbox("Filter", options=("None", "Blur", "Detail", "Emboss", "Smooth"))

    submitbtn = st.button('Submit')

    if submitbtn:
        edited = img.resize((width, height)).rotate(degree)
        st.image(edited)  

    if filters != 'None':
        edited = None  # Define edited variable
        if filters == 'Blur':
            edited = img.filter(ImageFilter.BLUR)
        elif filters == 'Detail':
            edited = img.filter(ImageFilter.DETAIL)
        elif filters == 'Emboss':
            edited = img.filter(ImageFilter.EMBOSS)
        else:
            edited = img.filter(ImageFilter.SMOOTH)

        if edited is not None:
            st.image(edited)