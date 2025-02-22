import streamlit as st
from datetime import datetime, date
import pandas as pd
import time

# Set page config
st.set_page_config(
    page_title="Birthday & Age Calculator",
    page_icon="🎂",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
    }
    .success-message {
        padding: 1rem;
        border-radius: 10px;
        background-color: #d4edda;
        color: #155724;
        margin: 1rem 0;
    }
    .developer-credits {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #f8f9fa;
        padding: 10px;
        text-align: center;
        border-top: 1px solid #dee2e6;
    }
    </style>
    """, unsafe_allow_html=True)

def calculate_age(birthdate):
    try:
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        next_birthday = date(today.year, birthdate.month, birthdate.day)
        if today > next_birthday:
            next_birthday = date(today.year + 1, birthdate.month, birthdate.day)
        days_until_birthday = (next_birthday - today).days
        
        return age, days_until_birthday
    except Exception as e:
        st.error(f"Error calculating age: {str(e)}")
        return None, None

def validate_input(name, birthdate):
    if not name.strip():
        st.error("Please enter your name!")
        return False
    if birthdate > date.today():
        st.error("Birth date cannot be in the future!")
        return False
    if birthdate.year < 1900:
        st.error("Please enter a valid birth date after 1900!")
        return False
    return True

def get_age_message(age):
    if age < 13:
        return "👶 You're just a child! Enjoy your wonderful childhood years! 🎈"
    elif age < 20:
        return "🌟 You're in your teenage years - an exciting time of discovery! 🎓"
    elif age < 30:
        return "✨ You're in your twenties - the perfect time to chase your dreams! 🎯"
    elif age < 50:
        return "🌈 You're in your prime years - make the most of your experience! 💪"
    else:
        return "🎊 You're wise and experienced - your wisdom is valuable! 👑"

def show_developer_credits():
    st.markdown("""
        <div class='developer-credits'>
            <p>Developed by: <b>Riaz Hussain</b> | Senior Student - Quarter 2 | 
            <a href="mailto:infosaifideveloper@gmail.com">📧 Contact Developer</a></p>
            <p>© 2025 All Rights Reserved</p>
        </div>
    """, unsafe_allow_html=True)

def main():
    st.title("🎉 Birthday Calculator & Wishes 🎂")
    st.write("Enter your details below to get personalized birthday wishes!")

    # Add developer info at the top
    st.markdown("""
        <div style='background-color:#f0f8ff;padding:10px;border-radius:5px;margin-bottom:20px;'>
            <h4>👨‍💻 Developer Information</h4>
            <p>Created by: <b>Riaz Hussain</b><br>
            Senior Student - Quarter 2<br>
            Specializing in HTML, CSS, Tailwind CSS, Node.js, React.js, Next.js, and Python.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Your Name")
        gender = st.selectbox("⚧ Gender", ["Male", "Female", "Other"])
        birthdate = st.date_input("📅 Your Birth Date", min_value=date(1900, 1, 1))
        marital_status = st.selectbox("💑 Marital Status", 
            ["Single", "Engaged", "Married", "Divorced", "Widowed"])

    if st.button("Calculate & Show Wishes 🎈"):
        if validate_input(name, birthdate):
            with st.spinner("Calculating..."):
                time.sleep(1)

            age, days_until_birthday = calculate_age(birthdate)
            if age is not None:
                # Display results with animation
                st.balloons()

                # Create result container
                result = st.container()
                with result:
                    st.markdown(f"### Hello {name}! 👋")
                    st.markdown(f"#### You are {age} years old! 🎉")
                    
                    # Age-specific message
                    st.info(get_age_message(age))

                    # Birthday check
                    today = date.today()
                    if today.month == birthdate.month and today.day == birthdate.day:
                        st.markdown("""
                            <div style='padding:20px;background-color:#ffebee;border-radius:10px;'>
                            <h2>🎉 Happy Birthday! 🎂</h2>
                            <p>Wishing you a fantastic day filled with joy and happiness!</p>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.write(f"🗓 {days_until_birthday} days until your next birthday!")

                    # Marital status message
                    status_messages = {
                        "Single": "🌟 Enjoying the freedom of single life!",
                        "Engaged": "💍 Congratulations on your engagement! Wishing you a beautiful journey ahead!",
                        "Married": "💑 Blessed with the joy of marriage! May your love grow stronger each day!",
                        "Divorced": "🌈 Starting a new chapter in life. Stay strong and positive!",
                        "Widowed": "🕊️ Carrying beautiful memories in your heart. Stay strong!"
                    }
                    
                    st.markdown(f"#### {status_messages[marital_status]}")

                    # Additional personalized message based on gender and age
                    if gender == "Male":
                        title = "Mr."
                    elif gender == "Female":
                        title = "Ms." if marital_status in ["Single", "Divorced"] else "Mrs."
                    else:
                        title = "Mx."

                    st.markdown(f"""
                        <div style='padding:20px;background-color:#e3f2fd;border-radius:10px;margin-top:20px;'>
                        <p>Dear {title} {name},</p>
                        <p>Thank you for using our Birthday Calculator! We hope you enjoyed learning about your age metrics.</p>
                        <p>Have a wonderful day! ✨</p>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Please fill in all the required fields! 🚨")

    # Show developer credits at the bottom
    show_developer_credits()

if __name__ == "__main__":
    main()