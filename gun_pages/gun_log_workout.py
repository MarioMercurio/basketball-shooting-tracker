from datetime import date, datetime
import uuid

import streamlit as st

from gun_components.gun_layout import gun_back_home_button, gun_page_title, gun_section_title
from gun_utils.gun_storage import gun_add_workout


def _gun_number_input(label, key):
    st.markdown(f'<div class="gun-label">{label}</div>', unsafe_allow_html=True)
    return st.number_input(
        label,
        min_value=0,
        max_value=10000,
        value=0,
        step=1,
        key=key,
        label_visibility="collapsed",
    )


def _gun_validate(made, attempted, label):
    if made > attempted:
        return f"{label} MAKES CANNOT BE GREATER THAN ATTEMPTS."
    return ""


def gun_render_log_workout():
    gun_page_title("LOG WORKOUT")

    workout_date = st.date_input("DATE", value=date.today())

    gun_section_title("3PT FG")
    three_made = _gun_number_input("MAKES", "gun_three_made")
    three_attempted = _gun_number_input("ATTEMPTS", "gun_three_attempted")

    gun_section_title("2PT FG")
    two_made = _gun_number_input("MAKES", "gun_two_made")
    two_attempted = _gun_number_input("ATTEMPTS", "gun_two_attempted")

    gun_section_title("FREE THROWS")
    free_throw_made = _gun_number_input("MAKES", "gun_free_throw_made")
    free_throw_attempted = _gun_number_input("ATTEMPTS", "gun_free_throw_attempted")

    errors = []
    for message in [
        _gun_validate(three_made, three_attempted, "3PT FG"),
        _gun_validate(two_made, two_attempted, "2PT FG"),
        _gun_validate(free_throw_made, free_throw_attempted, "FREE THROW"),
    ]:
        if message:
            errors.append(message)

    if st.button("SAVE WORKOUT"):
        if errors:
            for error in errors:
                st.error(error)
        else:
            workout = {
                "workout_id": str(uuid.uuid4()),
                "date": workout_date.isoformat(),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "three_made": int(three_made),
                "three_attempted": int(three_attempted),
                "two_made": int(two_made),
                "two_attempted": int(two_attempted),
                "free_throw_made": int(free_throw_made),
                "free_throw_attempted": int(free_throw_attempted),
                "notes": "",
            }
            gun_add_workout(workout)
            st.success("WORKOUT SAVED.")

    gun_back_home_button()
