import streamlit as st

from gun_components.gun_layout import gun_apply_styles
from gun_pages.gun_home import gun_render_home
from gun_pages.gun_log_workout import gun_render_log_workout
from gun_pages.gun_record_book import gun_render_record_book
from gun_pages.gun_stats import gun_render_stats
from gun_pages.gun_week_by_week import gun_render_week_by_week
from gun_pages.gun_workout_history import gun_render_workout_history
from gun_utils.gun_constants import GUN_APP_NAME

st.set_page_config(
    page_title=GUN_APP_NAME,
    page_icon="🏀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

gun_apply_styles()

if "gun_page" not in st.session_state:
    st.session_state.gun_page = "home"

if st.session_state.gun_page == "home":
    gun_render_home()
elif st.session_state.gun_page == "log_workout":
    gun_render_log_workout()
elif st.session_state.gun_page == "stats":
    gun_render_stats()
elif st.session_state.gun_page == "record_book":
    gun_render_record_book()
elif st.session_state.gun_page == "week_by_week":
    gun_render_week_by_week()
elif st.session_state.gun_page == "workout_history":
    gun_render_workout_history()
else:
    st.session_state.gun_page = "home"
    st.rerun()
