import streamlit as st
import qrcode as qr

st.title(":violet[QR Code Generator]")

text=st.text_input("Enter URL or Text",placeholder="e.g  https://www.google.com")

generate_btn=st.button("Generate")

if generate_btn:
    if(len(text)>=1):
        img=qr.make(text)
        img.save("qr-code.jpg")
        st.image("qr-code.jpg",caption="QR Code",width=350)
    else:
        st.error("Please Fill Out The Above Field")
    