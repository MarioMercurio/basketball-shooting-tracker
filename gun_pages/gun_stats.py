import streamlit as st

from gun_components.gun_layout import gun_back_home_button, gun_page_title


def gun_render_stats():
    gun_page_title("STATS")
    st.markdown('<div class="gun-message">THIS PAGE COMES NEXT.</div>', unsafe_allow_html=True)
    gun_back_home_button()
