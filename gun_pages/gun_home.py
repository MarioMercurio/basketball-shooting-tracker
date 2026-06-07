from pathlib import Path

import streamlit as st

from gun_components.gun_layout import gun_nav_button
from gun_utils.gun_constants import GUN_LOGO_PATH, GUN_QUOTE


def gun_render_home():
    logo = Path(GUN_LOGO_PATH)

    if logo.exists():
        st.image(str(logo), use_container_width=True)
    else:
        st.markdown("<h1>GUN CLUB</h1>", unsafe_allow_html=True)

    gun_nav_button("LOG WORKOUT", "log_workout")
    gun_nav_button("STATS", "stats")
    gun_nav_button("RECORD BOOK", "record_book")
    gun_nav_button("WEEK-BY-WEEK", "week_by_week")
    gun_nav_button("WORKOUT HISTORY", "workout_history")

    st.markdown(f'<div class="gun-quote">{GUN_QUOTE}</div>', unsafe_allow_html=True)
