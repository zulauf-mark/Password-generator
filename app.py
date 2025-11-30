import streamlit as st
import random
print("A")

numbers = list(range(10))
l_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
u_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

st.title("🔐 Jelszó Generáló")

usege = st.text_input("Mihez kell a jelszó?")
h = st.number_input("Jelszó hossza:", min_value=1, max_value=100)

all_option = st.checkbox("Minden")
use_numbers = use_lower = use_upper = all_option

if not all_option:
    use_numbers = st.checkbox("Számok")
    use_lower   = st.checkbox("Kisbetűk")
    use_upper   = st.checkbox("Nagybetűk")


# ---- CREATE CHARACTER POOL ----
all_lists = []
if use_numbers: all_lists.append(numbers)
if use_lower:   all_lists.append(l_letters)
if use_upper:   all_lists.append(u_letters)


# ---- PASSWORD GENERATION FUNCTION ----
def generate_password():
    passw = ""
    for i in range(h):
        chosen_list = random.choice(all_lists)
        character = random.choice(chosen_list)
        passw += str(character)
    return passw


# ---- BUTTONS ----
generate_clicked = st.button("Jelszó generálása")
ok_clicked=st.button("Mentés")

# Keep password in session_state
if "password" not in st.session_state:
    st.session_state.password = ""

if generate_clicked:
    if len(all_lists) == 0:
        st.error("Válasszon ki legalább egy karaktertípust!")
    else:
        st.session_state.password = generate_password()

if ok_clicked:
    with open("jelszavak.txt", "a", encoding="UTF-8") as f:
        f.write(str("\n") + usege + str(":\n\t") + st.session_state.password)
    ok_text=st.text("☑️ Jelszó elmentve!")



# ---- DISPLAY PASSWORD ----
if st.session_state.password:
    st.success(f"Generált jelszó: **{st.session_state.password}**")
