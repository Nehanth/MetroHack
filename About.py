
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(
    page_title="Find your Disease",
    page_icon="🤔",
    layout="wide"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_health = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_x1gjdldd.json")
lottie_welcome = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_puciaact.json")
img_biometrix = Image.open("images/img1.jpg")
img_lottie_animation = Image.open("images/img2.jpg")


# st.title("Main Page")
st.subheader("Welcome!")
st_lottie(lottie_welcome, height=300, key="welcome")
st.title("Find your disease just by uploading image of your hand or writing.")
st.write("A single platform that will help you to find your disease and based on your location and your condition will recommend you the nearby hospital.")
st.write("[Learn More >](https://google.com)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How it works?")
        st.write("##")
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
            qui officia deserunt mollit anim id est laborum.

            """
        )
        st.write("[Learn More>](https://youtube.com)")
    with right_column:
        st_lottie(lottie_health, height=300, key="health")

with st.container():
    st.write("---")
    st.header("What it does?")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Read More...](https://youtu.be)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_biometrix)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Read More...](https://youtu.be)")





st.sidebar.success("Select the page above.")