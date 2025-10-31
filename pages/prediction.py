import streamlit as st
from Scripts.golf import golf_model
from Scripts.archery import archery_model
from Scripts.wrestling import wrestling_model

def predict_page():
    
    sports = [
        "Golf", "Archery", "Wrestling",
        "Beach Volleyball", "Judo", "Equestrian", "Taekwondo", "Artistic Gymnastics",
        "Cycling BMX Racing", "Cycling Mountain Bike", "Badminton", "Water Polo", "Canoe Slalom",
        "Breaking", "Football", "Trampoline Gymnastics", "Boxing", "Sport Climbing", "Basketball",
        "Cycling Road", "Handball", "Weightlifting", "Athletics", "Hockey", "Surfing",
        "Sailing", "Shooting", "Volleyball", "Tennis", "Triathlon", "Swimming", "Canoe Sprint",
        "Marathon Swimming", "Rugby Sevens", "Fencing", "Diving", "Cycling BMX Freestyle",
        "Modern Pentathlon", "Table Tennis", "Skateboarding", "Rhythmic Gymnastics", "3x3 Basketball",
        "Artistic Swimming", "Cycling Track", "Rowing"
    ]

    icon_map = {
        "Golf": "golf_course", "Beach Volleyball": "sports_volleyball", "Judo": "self_improvement",
        "Equestrian": "pets", "Taekwondo": "sports_mma", "Artistic Gymnastics": "accessibility_new",
        "Cycling BMX Racing": "pedal_bike", "Cycling Mountain Bike": "pedal_bike",
        "Badminton": "sports_tennis", "Water Polo": "pool", "Canoe Slalom": "kayaking",
        "Breaking": "emoji_people", "Football": "sports_soccer", "Trampoline Gymnastics": "airline_seat_flat",
        "Boxing": "sports_mma", "Sport Climbing": "terrain", "Basketball": "sports_basketball",
        "Cycling Road": "pedal_bike", "Handball": "sports_handball", "Archery": "sports",
        "Weightlifting": "fitness_center", "Athletics": "directions_run", "Hockey": "sports_hockey",
        "Surfing": "surfing", "Sailing": "sailing", "Shooting": "target", "Volleyball": "sports_volleyball",
        "Tennis": "sports_tennis", "Triathlon": "directions_run", "Swimming": "pool",
        "Canoe Sprint": "kayaking", "Marathon Swimming": "waves", "Rugby Sevens": "sports_rugby",
        "Wrestling": "sports_kabaddi", "Fencing": "sports_martial_arts", "Diving": "pool",
        "Cycling BMX Freestyle": "pedal_bike", "Modern Pentathlon": "military_tech",
        "Table Tennis": "sports_tennis", "Skateboarding": "skateboarding",
        "Rhythmic Gymnastics": "accessibility_new", "3x3 Basketball": "sports_basketball",
        "Artistic Swimming": "waves", "Cycling Track": "pedal_bike", "Rowing": "rowing"
    }

    # ✅ Initialize session state
    if "sport" not in st.session_state:
        st.session_state.sport = None

    # ✅ Dummy model loader function (replace with actual model logic)
    def load_model(sport):
        with st.spinner(f"Loading model for {sport}..."):
            st.success(f"{sport} model loaded!")

    # ✅ Dummy model functions for sports not yet implemented
    def dummy_model():
        st.warning("This model is currently in development")
        st.info("Olympic Prediction Model for this sport will arrive with future updates!")
        st.markdown("""
        Apologies for inconvenience, working hard to bring you the best predictive models for all Olympic sports.
        Please check back later for updates!
        """)

    # ✅ Render logic
    st.title("🏅 Olympic Sports Model Selector")

    # Load Material Icons
    st.markdown("""
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    """, unsafe_allow_html=True)

    # When no sport selected → Show all buttons
    if st.session_state.sport is None:
        st.subheader("Choose a sport to load its model:")

        cols = st.columns(3)
        for idx, sport in enumerate(sports):
            icon = icon_map.get(sport, "sports")
            with cols[idx % 3]:
                if st.button(f"{sport}", key=sport, use_container_width=True, icon=f":material/{icon}:"):
                    st.session_state.sport = sport
                    st.rerun()

    # If sport selected, show model + cancel button
    else:
        selected_sport = st.session_state.sport
        st.success(f"✅ Selected Sport: {selected_sport}")
        icon = icon_map.get(selected_sport, "sports")

        st.markdown(f"### :material/{icon}: {selected_sport}")
        load_model(selected_sport)
        
        # Model mapping - only real models for Golf, Archery, Wrestling
        model_map = {
            "Golf": golf_model,
            "Archery": archery_model,
            "Wrestling": wrestling_model
        }
        
        # Get the model function or use dummy if not available
        model_func = model_map.get(selected_sport, dummy_model)
        model_func()

        st.markdown("---")
        if st.button("❌ Cancel", use_container_width=True):
            st.session_state.sport = None
            st.rerun()

if __name__ == "__main__":
    predict_page()
