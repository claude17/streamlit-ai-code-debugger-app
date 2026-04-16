import streamlit as st
from api_call import issue_generator,solution_generator

st.title("AI Code Debugger App",anchor=False)
st.markdown("Upload the image of your code")
st.divider()

with st.sidebar:
    st.header("Controls")
    has_error = False
    # image
    images = st.file_uploader(
        "Upload upto 3 images of your code",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )
    image_error = st.empty()
    if images:
        if(len(images)>3):
            image_error.error("Upload at max 3 images")
            has_error = True
        else:
            st.subheader("Uploaded images")

            col = st.columns(len(images))

            for i in range(len(images)):
                with col[i]:
                    st.image(images[i])

    # options
    option = st.selectbox(
        "How do you want to solve the problem?",
        ('Hints','Solution with code'),
        index=None
    )
    option_error = st.empty()
    if option:
        st.markdown(f"Selected Option: **{option}**")

    pressed = st.button("Submit",type="primary")
    

    if pressed:
        if not images:
            image_error.error("You must upload atleast 1 image")
            has_error = True
        if not option:
            option_error.error("You must select an option")
            has_error = True

if pressed and images and option and has_error != True:

    # The issue
    with st.container(border=True):
        st.subheader("The Issue:",anchor=False)
        
        with st.spinner("Generating response..."):
            generated_text = issue_generator(images)
            st.markdown(generated_text)

    # The Solution
    with st.container(border=True):
        st.subheader("The Solution",anchor=False)
        
        with st.spinner("Generating response..."):
            generated_text = solution_generator(images,option)
            st.markdown(generated_text)