import re 
import streamlit as st 
import string
import random

def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

def genrate_password(password):
  score = 0

  feedback = []

  if len(password)  >= 8:
     score += 1
  else:
      feedback.append("❌ Password should be at least 8 characters long.")

    #  check uppercase and lowercase
  if re.search(r"[A-Z]",password)  and re.search(r"[a-z]",password):
     score += 1
  else:
     feedback.append("Include both uppercase and lowercase charactors")   

  # Digit check

  if re.search(r"\d",password):
     score+=1
  else:
     feedback.append("❌ Add at least one number (0-9)")   

# speacal charectors check

  if re.search(r"[!@#$%^&*]",password):
     score += 1
  else:
     feedback.append("❌ Include at least one special character (!@#$%^&*).")

    #  check strength

  if score == 4:
      return "✅ Strong Password!", "Strong"
  elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "Moderate"
  else:
      return "\n".join(feedback), "Weak"



st.set_page_config(page_title="Password strength meter", page_icon="🔐",layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .stTextInput, .stSlider, .stButton {
            border-radius: 10px;
        }
        .stTextInput>div>div>input {
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #007BFF;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 8px 15px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("📝 Previous typed passwords")

if 'password_history' not in st.session_state:
    st.session_state.password_history = []


for i, past_password in enumerate(st.session_state.password_history[-5:], 1):  # Show last 5 passwords
    st.sidebar.write(f"{i}. {past_password}")


st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength:")

password = st.text_input("Enter your password",type="password")

if st.button("check strength"):
   if password:
      st.session_state.password_history.append(password)
      result , strength = genrate_password(password)

      if strength == "Strong":
         st.success(result)
         st.balloons()

      elif strength == "Moderate":
         st.warning(result)  

      else:
        st.error("Weak Password - Improve it using these tips:")
        for tip in result.split("\n"):
         st.write(tip)
   else:
        st.warning("⚠️ Please enter a password to check.")

st.write("---")
st.write("🔑 **Need a strong password? Generate one below!**")


password_length = st.slider("Select password length",min_value=8 , max_value=20,value=12)
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password(password_length)
    st.text_input("Suggested Strong Password:", strong_password)        