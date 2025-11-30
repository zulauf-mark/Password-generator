import streamlit as st
import random
from streamlit_js_eval import streamlit_js_eval
import json



#reading existing value from browser
saved_pw = streamlit_js_eval(js_expressions="localStorage.getItem('passwords')")

#st.login()
Users=["Márk","Mama","Henrik","Richard","Gábor","Susu"]


# If nothing saved yet, use an empty list
if saved_pw is None or saved_pw == "null":
    saved_pw_list = []
else:
    import json
    saved_pw_list = json.loads(saved_pw)

#Mentett jelszavak kiírása
st.write("Mentett jelszavak:", saved_pw_list)


#Listák felvétele
numbers = list(range(10))
l_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
u_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


#Login
login=st.text_input("Felhasználónév:")
if(login not in Users):
    st.text("Nem megfelelő felhasználónevet adott meg!")
else:
    if (login == "Susu"):
        st.text("Nagyonn szeretlek Kicsim ❤️")

    #A belépett felület
    st.title("🔐 Jelszó Generáló")

    usege = st.text_input("Mihez kell a jelszó?")
    h = st.number_input("Jelszó hossza:", min_value=1, max_value=100)

    all_option = st.checkbox("Minden")
    use_numbers = use_lower = use_upper = all_option

    #Választás a karakterekből
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


    #Jelszó generálás
    if generate_clicked:
        if len(all_lists) == 0:
            st.error("Válasszon ki legalább egy karaktertípust!")
        else:
            st.session_state.password = generate_password()


    #Jelszó mentés
    if ok_clicked:
        with open("jelszavak.txt", "a", encoding="UTF-8") as f:
            f.write(str("\n") + usege + str(":\n\t") + st.session_state.password)
        saved_pw_list.append(st.session_state.password)
        json_str=json.dump(saved_pw_list,ensure_ascii=False)
        streamlit_js_eval(
            js_expressions=f"localStorage.setItem('passwords', '{json_str}')")
        st.success("☑️ Jelszó elmentve!")



    # ---- DISPLAY PASSWORD ----
    if st.session_state.password:
        st.success(f"Generált jelszó: **{st.session_state.password}**")
