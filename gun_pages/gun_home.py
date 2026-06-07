from pathlib import Path

import streamlit as st

from gun_utils.gun_constants import GUN_LOGO_PATH, GUN_QUOTE


def gun_render_home():
    logo = Path(GUN_LOGO_PATH)

    if logo.exists():
        st.image(str(logo), use_container_width=True)
    else:
        st.markdown("<h1>GUN CLUB</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="gun-home-buttons">
            <a class="gun-home-button" href="?gun_page=log_workout">LOG WORKOUT</a>
            <a class="gun-home-button" href="?gun_page=stats">STATS</a>
            <a class="gun-home-button" href="?gun_page=record_book">RECORD BOOK</a>
            <a class="gun-home-button" href="?gun_page=week_by_week">WEEK-BY-WEEK</a>
            <a class="gun-home-button" href="?gun_page=workout_history">WORKOUT HISTORY</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f'<div class="gun-quote">{GUN_QUOTE}</div>', unsafe_allow_html=True)
