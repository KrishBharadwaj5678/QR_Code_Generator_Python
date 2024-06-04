import streamlit as st
import qrcode as qr

# Defining Page Title,Icon
st.set_page_config(
    page_title="QR Code Generator - Create Custom QR Codes Online",
    page_icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAY1BMVEX///8AAADCwsKWlpb09PR0dHSlpaVLS0vc3NxhYWEwMDDo6OjPz8+Ghoa0tLT7+/uOjo47Ozvh4eF4eHifn58iIiJvb29CQkI1NTWvr69aWlrU1NTExMRNTU3m5uYWFhYoKCgUtj3zAAADrklEQVR4nO3d23KqMBiG4VYtblBRcVPU2t7/VXY6PSCfY/4JWQGh631PwdCnPTENgZcXIiIiIiKi5L0maSRjjo0zx3LmKM3lESYIYR3CqBAmCGEdwqgQJghhHcKoeiXcPFmYTwIrjsHCfSEfNITHwne5+/Jo4cQ81+0tWJgZo6jwLfjqE4ROCH0hRPgbQl8I3RD6Qojwt78hrIxRni08Tp22u0jh4sMZ5aR/UUu427qXP7YinMqxWaRQs2bAKpzJsSlChAgRIkSIECHC/1a4jRRuWhBuWxHuZm664mAJc/djO/WGCwu5us5snj0/1LJIoRVCN4S+ENYhRPgohG4IfSGsQ9itsDDPdSuDhVWwsAy+ehEtPL4FVr4bwrU7TKmzTEv4XoZeXu/I6td9bX//zj2EUSFMEMI6hFEhTBDCOoRRIUxQn/dbjJKUG8Ly6p6p6zt5msubwjYKv3NvqCEcfgiHH8Lhh3D4IRx+f1+46ZVw7LbRlZls7G1zM8a8VGsnHeUqZ842/ktYO1EK/ZwplF/33era6dXf0hzVLXx1TTsbY7Zzb2LXwjlChAgRIkSIECFCj1C/eVvfSy+RwvB1C0vY5J6oLLRKvavgD2r6t9/t3WMrQziRM/cNhNpBPqjrLXPj920VPj+8GMLcM3pT4eKpwiVChAgRIkSIECHCoKzvpeeOhfo/71TCvaxN6Gyx8i8x3KW/CxXu3DWNSmcaN1mN0HULFR7kB7XXLdrIWl3THTSr4DFVuEj9IzfMEq4RekLYbQgRPgphtyFE+CiE3dYvYZoNDzrPGq3cMne/xTWTY/urd0jtWkULX5MU+8SBa+T1hiOM3RWEEGHzENYhDAshwuYhrEMY1nCEsd9Lv6KFaZ4TdVu6Ze6gx/3FPbb2X7DUta6DPEOqlFHse+xUmOZZX9aemfD54U7O/JBj8c/6av89M+HCLp4FjRAhQoQIESJEiDCtUL+XPvv9FircyDDVeV53Hssx3R+uwtPNPfPijjK39p60846S8KeZ6fxQ3wA484zw06dpChf26T0zWvwcHyFChAgRIkSIEGF3wq9Ewvbfy7103719WuVuy9PU23kip0YLrdK8W13TvdzWc6L6vG5hZe170vo8x7dCWIfQDaEvhAgfhbAOoRtCX0MV5pPACn17nQr3h0XdIStCB9X/8d8J5cz8c+HWQBhb+H1t4anwJsfi1y1ia18Yvyvo33U/IYwJIUKEzUIYE0KECJuFMKZUQiIiIiIioqi+Aed8jEj3hse7AAAAAElFTkSuQmCC",
    menu_items={
        "About":"Our QR Code Generator offers a convenient solution for generating personalized QR codes tailored to your needs. Whether you're a business owner looking to promote your website, a marketer seeking to engage customers, or an individual wanting to share contact details, our user-friendly tool makes it easy to create QR codes in seconds."
    }
)

st.write("<h3>Welcome to our <span style='color:orange;'>QR Code Generator!</span></h3>",unsafe_allow_html=True)

st.write("<h5>Start generating QR codes effortlessly and enhance your digital presence today!</h5>",unsafe_allow_html=True)

text=st.text_input("Enter URL or Text",placeholder="e.g  https://www.google.com")

generate_btn=st.button("Generate")

if generate_btn:
    if(len(text)>=1):
        img=qr.make(text)
        img.save("qr-code.jpg")
        st.image("qr-code.jpg",caption="QR Code")
    else:
        st.error("Please Fill Out The Above Field")
    
