import streamlit as st
import streamlit.components.v1 as components

st.title("Contact")
# Contact
with st.container():
    st.write("---")
    st.header("Let's get in touch !")
    st.write("##")
    # https://formsubmit.co if we need fully functional contact format

    contact_form = """
    <form action="https://formsubmit.co/kiran1.paudel2@gmail.com" method="POST" style="display: flex; flex-direction: column; gap: 10px;">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
        <input type="email" name="email" placeholder="Your Email" required style="padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
        <textarea name="message" placeholder="Your Message Here" required style="padding: 10px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
        <button type="submit" style="padding: 10px; border-radius: 5px; border: none; background-color: #4CAF50; color: white; cursor: pointer;">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    st.write("##")
    st.header("Book an Appointment")
    st.write("##")
    # Embed a live calendar for booking an appointment
    calendar_embed_code = """
    <iframe src="https://calendar.google.com/calendar/embed?src=kiran1.paudel2%40gmail.com&ctz=America%2FToronto" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
    """
    components.html(calendar_embed_code, height=600)