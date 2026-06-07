import base64
from pathlib import Path

import streamlit as st

from gun_utils.gun_constants import (
    GUN_BODY_FONT_PATH,
    GUN_GREY,
    GUN_HEADER_FONT_PATH,
    GUN_LIGHT_GREY,
    GUN_NAVY,
    GUN_WHITE,
)


def _gun_font_face(font_name, font_path):
    path = Path(font_path)
    if not path.exists():
        return ""

    encoded = base64.b64encode(path.read_bytes()).decode()
    suffix = path.suffix.lower()
    font_format = "truetype" if suffix == ".ttf" else "opentype"

    return f"""
    @font-face {{
        font-family: '{font_name}';
        src: url(data:font/{font_format};base64,{encoded}) format('{font_format}');
        font-weight: normal;
        font-style: normal;
    }}
    """


def gun_apply_styles():
    header_font = _gun_font_face("GunHeader", GUN_HEADER_FONT_PATH)
    body_font = _gun_font_face("GunBody", GUN_BODY_FONT_PATH)

    st.markdown(
        f"""
        <style>
        {header_font}
        {body_font}

        html, body, [data-testid="stAppViewContainer"] {{
            background-color: {GUN_WHITE};
        }}

        [data-testid="stHeader"] {{
            background-color: {GUN_WHITE};
        }}

        [data-testid="stToolbar"] {{
            display: none;
        }}

        .block-container {{
            max-width: 520px;
            padding-top: 1.1rem;
            padding-left: 1rem;
            padding-right: 1rem;
            padding-bottom: 2rem;
        }}

        h1, h2, h3, .gun-title {{
            font-family: 'GunHeader', Arial, sans-serif;
            color: {GUN_NAVY};
            text-transform: uppercase;
            text-align: center;
            letter-spacing: 1px;
        }}

        p, div, span, label, input, textarea {{
            font-family: 'GunBody', Arial, sans-serif;
            text-transform: uppercase;
        }}

        .gun-section-title {{
            font-family: 'GunHeader', Arial, sans-serif;
            color: {GUN_NAVY};
            text-align: center;
            font-size: 1.35rem;
            letter-spacing: 1px;
            margin-top: 1.5rem;
            margin-bottom: 0.65rem;
        }}

        .gun-label {{
            color: {GUN_GREY};
            font-size: 0.82rem;
            letter-spacing: 1px;
            margin-bottom: 0.25rem;
        }}

        .stButton {
            display:flex;
            justify-content:center;
        }

        .stButton > button {
            width: 450px !important;
            max-width: 95%;
            min-height: 90px;
            background-color: {GUN_NAVY};
            color: {GUN_GREY} !important;
            border: 2px solid {GUN_NAVY};
            border-radius: 12px;
            padding: 1.4rem 1rem;
            font-family: 'GunHeader', Arial, sans-serif !important;
            font-size: 28px !important;
            font-weight: 700 !important;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .stButton > button:hover {{
            background-color: {GUN_WHITE};
            color: {GUN_NAVY};
            border: 2px solid {GUN_NAVY};
        }}

        input {{
            text-align: center;
            font-size: 2rem !important;
            min-height: 74px;
            border-radius: 10px !important;
        }}

        [data-testid="stDateInput"] input {{
            font-size: 1.1rem !important;
            min-height: 52px;
        }}

        .gun-quote {{
            color: {GUN_GREY};
            text-align: center;
            font-size: 0.82rem;
            line-height: 1.45;
            margin-top: 2.25rem;
        }}

        .gun-message {{
            background-color: {GUN_LIGHT_GREY};
            border: 1px solid {GUN_GREY};
            border-radius: 12px;
            padding: 1rem;
            color: {GUN_NAVY};
            text-align: center;
            margin-top: 1rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def gun_nav_button(label, page):
    if st.button(label):
        st.session_state.gun_page = page
        st.rerun()


def gun_back_home_button():
    if st.button("HOME"):
        st.session_state.gun_page = "home"
        st.rerun()


def gun_page_title(title):
    st.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)


def gun_section_title(title):
    st.markdown(f'<div class="gun-section-title">{title}</div>', unsafe_allow_html=True)
