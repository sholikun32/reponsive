import streamlit as st
import streamlit.components.v1 as components
import streamlit.components.v1 as stc

import streamlit as st

def main():
    # Mengatur latar belakang gambar
    page_bg_img = '''
        <style>
        body {
            background-image: url("https://www.freepik.com/free-photos-vectors/white-background");
            background-size: cover;
        }
        </style>
        '''

    # Menambahkan kode HTML ke halaman Streamlit
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title("Login Page")

    with st.sidebar:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

    if login_button:
        if username == "admin" and password == "password":
            st.success("Logged in as {}".format(username))
            # Tampilkan halaman utama setelah berhasil login
        else:
            st.error("Invalid username or password")

if _name_ == "_main_":
    main()
