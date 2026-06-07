import streamlit as st

from gun_components.gun_layout import gun_back_home_button, gun_page_title


def gun_render_week_by_week():
    gun_page_title("WEEK-BY-WEEK")
    st.markdown('<div class="gun-message">THIS PAGE COMES NEXT.</div>', unsafe_allow_html=True)
    gun_back_home_button()
