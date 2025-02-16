import streamlit as st
from textblob import TextBlob
import random
import emoji
import datetime
# Romantic Styling with Custom CSS
st.markdown("""
    <style>
            
    /* Background with Romantic Gradient */
    .stApp {
        background: linear-gradient(135deg, #ffe6eb, #ffd6e4, #fce1f3);
        color: #2c003e;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    /* Title Styling */
    h1 {
        color: #C71585;
        text-align: center;
        text-shadow: 3px 3px #ffe6eb;
        font-size: 3em;
        margin-bottom: 30px;
    }

    /* Subheaders and Questions */
    .stMarkdown h2 {
        color: #800080;
        text-decoration: underline;
    }

    /* Custom Button */
    div.stButton > button {
        background-color: #FF69B4;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 12px 25px;
        font-weight: bold;
        box-shadow: 0px 6px 10px rgba(0,0,0,0.4);
        transition: 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #FF1493;
        transform: scale(1.1);
    }

    /* Text Inputs and Areas */
    input[type="text"], textarea, select {
        border: 2px solid #FF69B4;
        border-radius: 15px;
        padding: 10px;
        margin-top: 5px;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
    }

    /* Progress Bar Color */
    .stProgress > div > div {
        background-color: #FF69B4 !important;
    }

    /* Love Score Display */
    .stAlert {
        background-color: #ffe6eb;
        color: #C71585;
        border-radius: 15px;
        border: 2px solid #FF69B4;
    }

    /* Song Link */
    a {
        color: #C71585;
        text-decoration: none;
    }

    a:hover {
        color: #FF69B4;
        text-decoration: underline;
    }

    /* Footer */
    .stFooter {
        color: #FF69B4;
        font-style: italic;
    }

    </style>
    """, unsafe_allow_html=True)

def analyze_love_score(answers):
    total_sentiment = sum(TextBlob(answer).sentiment.polarity for answer in answers)
    avg_sentiment = (total_sentiment / len(answers)) * 100
    love_score = round(avg_sentiment + random.randint(5, 40)) 
    return max(0, min(love_score, 100))

def generate_love_message(score):
    if score > 85:
        return f"💖 True Soulmates! Your Love Score is {score}% {emoji.emojize(':sparkling_heart:')}"
    elif score > 70:
        return f"❤️ A Strong and Beautiful Bond! Score: {score}%"
    elif score > 50:
        return f"💛 A Good Match! Keep growing together! Score: {score}%"
    else:
        return f"💔 Love Needs Some Work! But don't worry, true love takes time! Score: {score}%"

def suggest_couple_name(name1, name2):
    return name1[:3].capitalize() + name2[-3:].capitalize()

def suggest_couple_story(name1, name2):
    stories = [
        f"{name1} and {name2} met by chance but stayed by choice, growing stronger with each shared laugh and adventure.",
        f"{name1} and {name2} were once strangers who became inseparable, discovering magic in everyday moments.",
        f"{name1} and {name2} started with a simple 'hello' that turned into a lifetime of 'I love you's.",
        f"{name1} and {name2} found love in the most unexpected place, turning an ordinary day into an extraordinary life.",
        f"{name1} and {name2} built their relationship on trust and laughter, creating a bond that's unbreakable."
    ]
    return random.choice(stories)

def suggest_song_and_link():
    songs = [
        ("Dilshad - Yawar Abdal", "https://youtu.be/rPOn6B6zcGU?si=XWOwAhXfpPByLeRC"),
        ("Maanu - Jhol", "https://youtu.be/qg89z5xMyTU?si=HlTiKYxkBy2mnU7n"),
        ("Ishq Official", "https://youtu.be/hHuG7FIKgtc?si=MdnK5hf7YPrqqGKq"),
        ("Wedding Nasheed ", "https://youtu.be/ivrumxRUz_Y?si=QAppP0j74qSo0E1K"),
        ("Ed Sheeran - Perfect ", "https://youtu.be/2Vv-BfVoq4g?si=og7I7mkatsz_g6XO")
    ]
    return random.choice(songs)

st.title("💖 AI Love Compatibility Test 💖")

name1 = st.text_input("Your Name")
dob1 = st.date_input("Your Birthday", min_value=datetime.date(1950, 1, 1))
name2 = st.text_input("Partner's Name")
dob2 = st.date_input("Partner's Birthday", min_value=datetime.date(1950, 1, 1))

st.write("💑 Answer these fun questions to check your love compatibility!")

q1 = st.text_area("1️⃣ How do you feel when you think about your partner?")
q2 = st.text_area("2️⃣ What's the best thing about your relationship?")
q3 = st.text_area("3️⃣ Describe your partner in one sentence.")
q4 = st.text_area("4️⃣ How do you handle fights or disagreements?")
q5 = st.text_area("5️⃣ What would you do for a romantic date?")

st.write("✨ What qualities do you value most in a partner?")
qualities = st.multiselect("Select qualities", ["Respect","Support","Honesty","Trust","Humor", "Kindness", "Intelligence", "Loyalty", "Patience"])

st.write("🎶 What kind of music do you like?")
music_preferences = st.multiselect("Select music genres", ["Country","Pop", "Rock", "Classical", "Jazz", "EDM", "Hip-Hop","K-Pop","R&B (Rhythm & Blues)"])

if st.button("💘 Calculate Love Score"):
    if not (name1 and name2 and q1 and q2 and q3 and q4 and q5):
        st.error("⚠️ Please answer all questions!")
    else:
        answers = [q1, q2, q3, q4, q5]
        love_score = analyze_love_score(answers)
        result_message = generate_love_message(love_score)
        st.success(result_message)
        st.progress(love_score / 100)

        st.write(f"💎 Selected Qualities: {', '.join(qualities) if qualities else 'None'}")
        st.write(f"🎼 Music Preferences: {', '.join(music_preferences) if music_preferences else 'None'}")

        couple_name = suggest_couple_name(name1, name2)
        story = suggest_couple_story(name1, name2)
        song, link = suggest_song_and_link()

        st.write(f"💞 Suggested Couple Name: {couple_name}")
        st.write(f"📖 Couple Story: {story}")
        st.markdown(f"🎶 Suggested Song: [{song}]({link})")

        if love_score > 50:
          st.balloons()
