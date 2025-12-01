# IMPORTOK
import streamlit as st
import random
import json
from streamlit_js_eval import streamlit_js_eval

# FELHASZNÁLÓK
Users = ["Márk", "Mama", "Henrik", "Richard", "Gábor", "Susu"]



# ---- LOGIN ----
login = st.text_input("Felhasználónév:")
if login not in Users:
    st.text("Nem megfelelő felhasználónevet adott meg!")
else:
    if login == "Susu":
        st.text("Nagyonn szeretlek Kicsim ❤️")

    # ---- MENTETT JELSZAVAK ----
    if st.button("Jelszavak betöltése"):
        saved_pw = streamlit_js_eval(js_expressions="localStorage.getItem('passwords')", key="load_pw")
        if saved_pw and saved_pw != "null":
            saved_pw_list = json.loads(saved_pw)
        else:
            saved_pw_list = []
        for idx, entry in enumerate(saved_pw_list):
            st.write(f"{idx + 1}. {entry['usege']}: {entry['password']}")

    # ---- LISTÁK ----
    numbers = list(range(10))
    l_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    u_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    # ---- GENERÁLÁS ----
    st.title("🔐 Jelszó Generáló")
    usege = st.text_input("Mihez kell a jelszó?", key="usage")
    h = st.number_input("Jelszó hossza:", min_value=1, max_value=100, key="length")

    all_option = st.checkbox("Minden karaktertípus")
    use_numbers = use_lower = use_upper = all_option
    if not all_option:
        use_numbers = st.checkbox("Számok")
        use_lower   = st.checkbox("Kisbetűk")
        use_upper   = st.checkbox("Nagybetűk")

    all_lists = []
    if use_numbers: all_lists.append(numbers)
    if use_lower:   all_lists.append(l_letters)
    if use_upper:   all_lists.append(u_letters)

    # SESSION STATE
    if "password" not in st.session_state:
        st.session_state.password = ""

    def generate_password():
        if len(all_lists) == 0:
            return ""
        return "".join(str(random.choice(random.choice(all_lists))) for _ in range(h))

    # ---- GOMBOK ----
    if st.button("Jelszó generálása"):
        if len(all_lists) == 0:
            st.error("Válasszon ki legalább egy karaktertípust!")
        else:
            st.session_state.password = generate_password()

    if st.session_state.password:
        st.success(f"Generált jelszó: **{st.session_state.password}**")

    if st.button("Mentés"):
        new_entry = {"usege": usege, "password": st.session_state.password}
        st.success("☑️ Jelszó elmentve!")
