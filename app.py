import streamlit as st

# Navigation Menu
st.sidebar.title("📽 Popcorn Pictures")
page = st.sidebar.radio("Go to", ["Home", "Actors", "Top Rated", "Request a Movie", "Login", "Register"])

# Home Page (Main Movie Listing)
if page == "Home":
    st.title("🎬 Recent Movies")
    
    movies = [
        {
            "title": "Daaku Maharaaj",
            "director": "Bobby Kolli",
            "starring": "Nandamuri Balakrishna, Bobby Deol, Pragya Jaiswal",
            "music": "Thaman S",
            "poster": "https://upload.wikimedia.org/wikipedia/en/e/e9/Daaku_Maharaaj_film_poster.jpg",
            "review_link": "Daaku Maharaj"
        },
        {
            "title": "Sankranthiki Vasthunam",
            "director": "Anil Ravipudi",
            "starring": "Venkatesh, Meenakshi Chaudhary",
            "music": "Bheems Ceciroleo",
            "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Sankranthiki_Vasthunnam_Release_Date%282%29.jpg/330px-Sankranthiki_Vasthunnam_Release_Date%282%29.jpg",
            "review_link": "Sankranthiki Vasthunam"
        },
        {
            "title": "Game Changer",
            "director": "S. Shankar",
            "starring": "Ram Charan, Kiara Advani, Anjali",
            "music": "Thaman S",
            "poster": "https://upload.wikimedia.org/wikipedia/en/6/6a/Game_Changer_Telugu.jpg",
            "review_link": "Game Changer"
        }
    ]
    
    for movie in movies:
        st.image(movie["poster"], width=250)
        st.subheader(movie["title"])
        st.write(f"**Director:** {movie['director']}")
        st.write(f"**Starring:** {movie['starring']}")
        st.write(f"**Music by:** {movie['music']}")
        st.markdown(f"[Read Reviews](#{movie['review_link'].replace(' ', '_')})")
        st.write("---")

# Actors Page
elif page == "Actors":
    st.title("🎭 Popular Actors")
    actors = [
        {"name": "Mahesh Babu", "films": "Srimanthudu, Bharat Ane Nenu", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Mahesh_Babu_in_Spyder_%28cropped%29.jpg/330px-Mahesh_Babu_in_Spyder_%28cropped%29.jpg"},
        {"name": "Pawan Kalyan", "films": "Vakeel Saab, Bheemla Nayak", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/The_noted_Telugu_film_actor_Shri_Pavan_Kalyan.jpg/306px-thumbnail.jpg"},
        {"name": "NTR Jr.", "films": "Janatha Garage, RRR", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/N._T._Rama_Rao_Jr._in_2021.jpg/330px-N._T._Rama_Rao_Jr._in_2021.jpg"}
    ]
    
    for actor in actors:
        st.image(actor["image"], width=200)
        st.subheader(actor["name"])
        st.write(f"**Notable Films:** {actor['films']}")
        st.write("---")

# Top Rated Movies
elif page == "Top Rated":
    st.title("⭐ Top Rated Telugu Movies")
    movies = [
        {"title": "RRR", "director": "S. S. Rajamouli", "poster": "https://upload.wikimedia.org/wikipedia/en/d/d7/RRR_Poster.jpg"},
        {"title": "Baahubali 2", "director": "S. S. Rajamouli", "poster": "https://upload.wikimedia.org/wikipedia/en/9/93/Baahubali_2_The_Conclusion_poster.jpg"},
        {"title": "Jersey", "director": "Gowtam Tinnanuri", "poster": "https://upload.wikimedia.org/wikipedia/en/1/10/Jersey_2019_poster.jpg"}
    ]
    
    for movie in movies:
        st.image(movie["poster"], width=250)
        st.subheader(movie["title"])
        st.write(f"**Directed by:** {movie['director']}")
        st.write("---")

# Movie Request Form
elif page == "Request a Movie":
    st.title("📩 Request a Movie")
    
    with st.form("movie_request"):
        email = st.text_input("Your Email")
        movie_name = st.text_input("Movie Name")
        year = st.number_input("Year", min_value=1900, max_value=2025, step=1)
        submitted = st.form_submit_button("Submit Request")
        
        if submitted:
            st.success(f"✅ Request for '{movie_name}' received! We will notify you at {email}.")

# Login Page
elif page == "Login":
    st.title("🔐 Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Login")
        
        if login:
            st.success("✅ Logged in successfully!")

# Register Page
elif page == "Register":
    st.title("📝 Register")

    with st.form("register_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        register = st.form_submit_button("Register")

        if register:
            if password == confirm_password:
                st.success("✅ Registration successful!")
            else:
                st.error("❌ Passwords do not match!")
