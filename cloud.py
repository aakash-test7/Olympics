import pandas as pd
import streamlit as st
import os
from google.cloud import storage
import io
from google.oauth2 import service_account
from google.cloud import storage
from datetime import timedelta
from google.oauth2 import service_account
import ast
import joblib
import plotly.express as px

secrets = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(secrets)

from google.cloud import storage
from datetime import timedelta

def generate_signed_url(blob_name):
    """Generates a signed URL to access a file in GCS."""
    try:
        bucket_name = "olympics-2025"
        client = storage.Client(credentials=credentials)
        # Use `client.bucket()` instead of `get_bucket()` to avoid needing storage.buckets.get
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        if not blob.exists():
            print(f"File {blob_name} does not exist in bucket {bucket_name}")  # Debugging
            return None
        url = blob.generate_signed_url(
            expiration=timedelta(hours=1),
            method='GET'
        )
        print(f"Generated signed URL for {blob_name}: {url}")  # Debugging
        return url
    except Exception as e:
        print(f"Error generating signed URL for {blob_name}: {e}")  # Debugging
        return None

# Initialize the Google Cloud Storage client
client = storage.Client(credentials=credentials)

bucket_name = "olympics-2025"

def read_excel_from_gcs(bucket_name, blob_name, header=0):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = blob.download_as_bytes()
    return pd.read_csv(io.BytesIO(data), header=header)

athlete_df = read_excel_from_gcs(bucket_name, "Data/athletes.csv")
medals_total_df = read_excel_from_gcs(bucket_name, "Data/medals_total.csv")
technical_officials_df = read_excel_from_gcs(bucket_name, "Data/technical_officials.csv")
events_df = read_excel_from_gcs(bucket_name, "Data/events.csv")
schedules_df = read_excel_from_gcs(bucket_name, "Data/schedules.csv")
torch_route_df = read_excel_from_gcs(bucket_name, "Data/torch_route.csv")
medallists_df = read_excel_from_gcs(bucket_name, "Data/medallists.csv")
teams_df = read_excel_from_gcs(bucket_name, "Data/teams.csv")
medals_df = read_excel_from_gcs(bucket_name, "Data/medals.csv")
venues_df = read_excel_from_gcs(bucket_name, "Data/venues.csv")
nocs_df = read_excel_from_gcs(bucket_name, "Data/nocs.csv")
coaches_df = read_excel_from_gcs(bucket_name, "Data/coaches.csv")
schedules_preliminary_df = read_excel_from_gcs(bucket_name, "Data/schedules_preliminary.csv")

golf_df = read_excel_from_gcs(bucket_name, "Data/results/Golf.csv")
beach_volleyball_df = read_excel_from_gcs(bucket_name, "Data/results/Beach Volleyball.csv")
judo_df = read_excel_from_gcs(bucket_name, "Data/results/Judo.csv")
equestrian_df = read_excel_from_gcs(bucket_name, "Data/results/Equestrian.csv")
taekwondo_df = read_excel_from_gcs(bucket_name, "Data/results/Taekwondo.csv")
artistic_gymnastics_df = read_excel_from_gcs(bucket_name, "Data/results/Artistic Gymnastics.csv")
cycling_bmx_racing_df = read_excel_from_gcs(bucket_name, "Data/results/Cycling BMX Racing.csv")
cycling_mountain_bike_df = read_excel_from_gcs(bucket_name, "Data/results/Cycling Mountain Bike.csv")
badminton_df = read_excel_from_gcs(bucket_name, "Data/results/Badminton.csv")
water_polo_df = read_excel_from_gcs(bucket_name, "Data/results/Water Polo.csv")
canoe_slalom_df = read_excel_from_gcs(bucket_name, "Data/results/Canoe Slalom.csv")
breaking_df = read_excel_from_gcs(bucket_name, "Data/results/Breaking.csv")
football_df = read_excel_from_gcs(bucket_name, "Data/results/Football.csv")
trampoline_gymnastics_df = read_excel_from_gcs(bucket_name, "Data/results/Trampoline Gymnastics.csv")
boxing_df = read_excel_from_gcs(bucket_name, "Data/results/Boxing.csv")
sport_climbing_df = read_excel_from_gcs(bucket_name, "Data/results/Sport Climbing.csv")
basketball_df = read_excel_from_gcs(bucket_name, "Data/results/Basketball.csv")
cycling_road_df = read_excel_from_gcs(bucket_name, "Data/results/Cycling Road.csv")
handball_df = read_excel_from_gcs(bucket_name, "Data/results/Handball.csv")
archery_df = read_excel_from_gcs(bucket_name, "Data/results/Archery.csv")
weightlifting_df = read_excel_from_gcs(bucket_name, "Data/results/Weightlifting.csv")
athletics_df = read_excel_from_gcs(bucket_name, "Data/results/Athletics.csv")
hockey_df = read_excel_from_gcs(bucket_name, "Data/results/Hockey.csv")
surfing_df = read_excel_from_gcs(bucket_name, "Data/results/Surfing.csv")
sailing_df = read_excel_from_gcs(bucket_name, "Data/results/Sailing.csv")
shooting_df = read_excel_from_gcs(bucket_name, "Data/results/Shooting.csv")
volleyball_df = read_excel_from_gcs(bucket_name, "Data/results/Volleyball.csv")
tennis_df = read_excel_from_gcs(bucket_name, "Data/results/Tennis.csv")
triathlon_df = read_excel_from_gcs(bucket_name, "Data/results/Triathlon.csv")
swimming_df = read_excel_from_gcs(bucket_name, "Data/results/Swimming.csv")
canoe_sprint_df = read_excel_from_gcs(bucket_name, "Data/results/Canoe Sprint.csv")
marathon_swimming_df = read_excel_from_gcs(bucket_name, "Data/results/Marathon Swimming.csv")
rugby_sevens_df = read_excel_from_gcs(bucket_name, "Data/results/Rugby Sevens.csv")
wrestling_df = read_excel_from_gcs(bucket_name, "Data/results/Wrestling.csv")
fencing_df = read_excel_from_gcs(bucket_name, "Data/results/Fencing.csv")
diving_df = read_excel_from_gcs(bucket_name, "Data/results/Diving.csv")
cycling_bmx_freestyle_df = read_excel_from_gcs(bucket_name, "Data/results/Cycling BMX Freestyle.csv")
modern_pentathlon_df = read_excel_from_gcs(bucket_name, "Data/results/Modern Pentathlon.csv")
table_tennis_df = read_excel_from_gcs(bucket_name, "Data/results/Table Tennis.csv")
skateboarding_df = read_excel_from_gcs(bucket_name, "Data/results/Skateboarding.csv")
rhythmic_gymnastics_df = read_excel_from_gcs(bucket_name, "Data/results/Rhythmic Gymnastics.csv")
basketball3x3_df = read_excel_from_gcs(bucket_name, "Data/results/Basketball3x3.csv")
artistic_swimming_df = read_excel_from_gcs(bucket_name, "Data/results/Artistic Swimming.csv")
cycling_track_df = read_excel_from_gcs(bucket_name, "Data/results/Cycling Track.csv")
rowing_df = read_excel_from_gcs(bucket_name, "Data/results/Rowing.csv")

import io
import joblib
from google.cloud import storage
from collections import defaultdict

def load_all_pickles_for_sport(sport, bucket_name, credentials=None):
    """
    Loads all .pkl files from Model/<sport>/ in GCS, organized by [type][gender].
    Example: "Model/Golf/golf_model_men.pkl" → result["model"]["men"]
    """
    client = storage.Client(credentials=credentials)
    bucket = client.bucket(bucket_name)
    prefix = f"Model/{sport}/"

    blobs = list(client.list_blobs(bucket, prefix=prefix))
    pickles = defaultdict(dict)
    for blob in blobs:
        if blob.name.endswith(".pkl"):
            try:
                # Example: Model/Golf/scaler_weight_men.pkl
                filename = blob.name.split("/")[-1].replace(".pkl", "")
                parts = filename.split("_")
                # Find the gender keyword
                if parts[-1] in ["men", "women", "mixed"]:
                    gender = parts[-1]
                    key = "_".join(parts[:-1])
                else:
                    gender = "general"
                    key = filename
                # Download and load
                data = blob.download_as_bytes()
                obj = joblib.load(io.BytesIO(data))
                pickles[key][gender] = obj
                print(f"✅ Loaded: {blob.name} as [{key}][{gender}]")
            except Exception as e:
                print(f"⚠️ Failed to load {blob.name}: {e}")
    return dict(pickles)

def nanDataframe(df):
    df_clean = df.copy()
    for col in df_clean.columns:
        if df_clean[col].isna().all() or (df_clean[col].astype(str).str.strip() == '').all():
            df_clean.drop(col, axis=1, inplace=True)
    
    return df_clean

def plots_data():
    athletes_df=athlete_df.copy()
    st.title("Olympics 2024: Data Visualizations")

    con=st.container(border=True)
    with con:
        col1,col2=st.columns([1,1])

        col1.subheader("Total Medals by Country")
        fig1 = px.bar(medals_total_df.sort_values("Total", ascending=False).head(15),
                    x="country_long", y="Total", color="country_long",
                    labels={"country_long": "Country", "Total": "Total Medals"},
                    title="Top 15 Countries by Total Medals")
        col1.plotly_chart(fig1,use_container_width=True)

        col2.subheader("Medal Breakdown by Country")
        fig2 = px.bar(medals_total_df.sort_values("Total", ascending=False).head(10),
                    x="country_long", y=["Gold Medal", "Silver Medal", "Bronze Medal"],
                    title="Gold, Silver, Bronze by Country")
        col2.plotly_chart(fig2,use_container_width=True)

        st.subheader("Number of Events by Sport")
        sport_event_count = events_df['sport'].value_counts().reset_index()
        sport_event_count.columns = ['Sport', 'Number of Events']
        fig3 = px.bar(sport_event_count.sort_values("Number of Events", ascending=False),
                    x="Sport", y="Number of Events",
                    title="Number of Events by Sport")
        st.plotly_chart(fig3,use_container_width=True)
    
    con=st.container(border=True)
    with con:
        col1,col2=st.columns([1,1])
        col1.subheader("Medallists by Gender")
        fig8 = px.histogram(medallists_df, x="gender", color="medal_type",
                            barmode="group", title="Medals by Gender and Type")
        col1.plotly_chart(fig8,use_container_width=True)

        col2.subheader("Gender Distribution of Coaches")
        fig13 = px.pie(coaches_df, names='gender', title='Coaches Gender Distribution')
        col2.plotly_chart(fig13,use_container_width=True)

    con=st.container(border=True)
    with con:
        st.subheader("Olympic Torch Route Timeline")
        torch_route_df["date_start"] = pd.to_datetime(torch_route_df["date_start"])
        fig4 = px.timeline(torch_route_df.sort_values("date_start"),
                        x_start="date_start", x_end="date_end",
                        y="city", color="title", title="Torch Relay Timeline")
        st.plotly_chart(fig4)

        st.subheader("Scheduled Events Overview")
        fig5 = px.treemap(schedules_df, path=["discipline"], values=None,
                        title="Event Schedule by Discipline (Treemap)")
        st.plotly_chart(fig5)

    con=st.container(border=True)
    with con:
        col1,col2=st.columns([1,1])
        col1.subheader("Number of Coaches by Country")
        coach_country_count = coaches_df['country_long'].value_counts().reset_index()
        coach_country_count.columns = ['Country', 'Coach Count']
        fig6 = px.bar(coach_country_count.head(10), x='Country', y='Coach Count',
                    title='Top 10 Countries by Number of Coaches')
        col1.plotly_chart(fig6,use_container_width=True)

        col2.subheader("Number of Sports per Venue")
        venue_df = venues_df.copy()
        venue_df['sport_count'] = venue_df['sports'].apply(lambda x: len(eval(x)) if pd.notnull(x) else 0)
        fig9 = px.bar(venue_df.sort_values("sport_count", ascending=False),
                    x="venue", y="sport_count", title="Number of Sports per Venue")
        col2.plotly_chart(fig9,use_container_width=True)

    con=st.container(border=True)
    with con:
        st.subheader("Number of Athletes per Country")
        athlete_country_count = athletes_df['country_long'].value_counts().reset_index()
        athlete_country_count.columns = ['Country', 'Athlete Count']
        fig10 = px.bar(athlete_country_count.head(10), x='Country', y='Athlete Count',
                    title="Top 10 Countries by Athlete Participation")
        st.plotly_chart(fig10)

        st.subheader("Events Scheduled Per Day")
        schedules_df["start_date"] = pd.to_datetime(schedules_df["start_date"])
        daily_event_count = schedules_df["start_date"].dt.date.value_counts().reset_index()
        daily_event_count.columns = ["Date", "Event Count"]
        fig11 = px.line(daily_event_count.sort_values("Date"), x="Date", y="Event Count",
                        markers=True, title="Number of Events Scheduled Per Day")
        st.plotly_chart(fig11)

        st.subheader("Medals Awarded by Discipline")
        medals_discipline_count = medals_df['discipline'].value_counts().reset_index()
        medals_discipline_count.columns = ['Discipline', 'Medal Count']
        fig12 = px.bar(medals_discipline_count.head(10), x='Discipline', y='Medal Count',
                    title="Top 10 Disciplines by Medals Awarded")
        st.plotly_chart(fig12)
    return
    
def show_data_main():
    with st.container(border=True):
        with st.expander("athletes.csv", expanded=False):
            st.dataframe(nanDataframe(athlete_df))

        with st.expander("medals_total.csv", expanded=False):
            st.dataframe(nanDataframe(medals_total_df))

        with st.expander("technical_officials.csv", expanded=False):
            st.dataframe(nanDataframe(technical_officials_df))

        with st.expander("events.csv", expanded=False):
            st.dataframe(nanDataframe(events_df))

        with st.expander("schedules.csv", expanded=False):
            st.dataframe(nanDataframe(schedules_df))

        with st.expander("torch_route.csv", expanded=False):
            st.dataframe(nanDataframe(torch_route_df))

        with st.expander("medallists.csv", expanded=False):
            st.dataframe(nanDataframe(medallists_df))

        with st.expander("teams.csv", expanded=False):
            st.dataframe(nanDataframe(teams_df))

        with st.expander("medals.csv", expanded=False):
            st.dataframe(nanDataframe(medals_df))

        with st.expander("venues.csv", expanded=False):
            st.dataframe(nanDataframe(venues_df))

        with st.expander("nocs.csv", expanded=False):
            st.dataframe(nanDataframe(nocs_df))

        with st.expander("coaches.csv", expanded=False):
            st.dataframe(nanDataframe(coaches_df))

        with st.expander("schedules_preliminary.csv", expanded=False):
            st.dataframe(nanDataframe(schedules_preliminary_df))
        return
    
st.markdown("---")

def show_data_result():
    with st.container(border=True):
        with st.expander("Golf.csv", expanded=False):
            st.dataframe(nanDataframe(golf_df))

        with st.expander("Beach Volleyball.csv", expanded=False):
            st.dataframe(nanDataframe(beach_volleyball_df))

        with st.expander("Judo.csv", expanded=False):
            st.dataframe(nanDataframe(judo_df))

        with st.expander("Equestrian.csv", expanded=False):
            st.dataframe(nanDataframe(equestrian_df))

        with st.expander("Taekwondo.csv", expanded=False):
            st.dataframe(nanDataframe(taekwondo_df))

        with st.expander("Artistic Gymnastics.csv", expanded=False):
            st.dataframe(nanDataframe(artistic_gymnastics_df))

        with st.expander("Cycling BMX Racing.csv", expanded=False):
            st.dataframe(nanDataframe(cycling_bmx_racing_df))

        with st.expander("Cycling Mountain Bike.csv", expanded=False):
            st.dataframe(nanDataframe(cycling_mountain_bike_df))

        with st.expander("Badminton.csv", expanded=False):
            st.dataframe(nanDataframe(badminton_df))

        with st.expander("Water Polo.csv", expanded=False):
            st.dataframe(nanDataframe(water_polo_df))

        with st.expander("Canoe Slalom.csv", expanded=False):
            st.dataframe(nanDataframe(canoe_slalom_df))

        with st.expander("Breaking.csv", expanded=False):
            st.dataframe(nanDataframe(breaking_df))

        with st.expander("Football.csv", expanded=False):
            st.dataframe(nanDataframe(football_df))

        with st.expander("Trampoline Gymnastics.csv", expanded=False):
            st.dataframe(nanDataframe(trampoline_gymnastics_df))

        with st.expander("Boxing.csv", expanded=False):
            st.dataframe(nanDataframe(boxing_df))

        with st.expander("Sport Climbing.csv", expanded=False):
            st.dataframe(nanDataframe(sport_climbing_df))

        with st.expander("Basketball.csv", expanded=False):
            st.dataframe(nanDataframe(basketball_df))

        with st.expander("Cycling Road.csv", expanded=False):
            st.dataframe(nanDataframe(cycling_road_df))

        with st.expander("Handball.csv", expanded=False):
            st.dataframe(nanDataframe(handball_df))

        with st.expander("Archery.csv", expanded=False):
            st.dataframe(nanDataframe(archery_df))

        with st.expander("Weightlifting.csv", expanded=False):
            st.dataframe(nanDataframe(weightlifting_df))

        with st.expander("Athletics.csv", expanded=False):
            st.dataframe(nanDataframe(athletics_df))

        with st.expander("Hockey.csv", expanded=False):
            st.dataframe(nanDataframe(hockey_df))

        with st.expander("Surfing.csv", expanded=False):
            st.dataframe(nanDataframe(surfing_df))

        with st.expander("Sailing.csv", expanded=False):
            st.dataframe(nanDataframe(sailing_df))

        with st.expander("Shooting.csv", expanded=False):
            st.dataframe(nanDataframe(shooting_df))

        with st.expander("Volleyball.csv", expanded=False):
            st.dataframe(nanDataframe(volleyball_df))

        with st.expander("Tennis.csv", expanded=False):
            st.dataframe(nanDataframe(tennis_df))

        with st.expander("Triathlon.csv", expanded=False):
            st.dataframe(nanDataframe(triathlon_df))

        with st.expander("Swimming.csv", expanded=False):
            st.dataframe(nanDataframe(swimming_df))

        with st.expander("Canoe Sprint.csv", expanded=False):
            st.dataframe(nanDataframe(canoe_sprint_df))

        with st.expander("Marathon Swimming.csv", expanded=False):
            st.dataframe(nanDataframe(marathon_swimming_df))

        with st.expander("Rugby Sevens.csv", expanded=False):
            st.dataframe(nanDataframe(rugby_sevens_df))

        with st.expander("Wrestling.csv", expanded=False):
            st.dataframe(nanDataframe(wrestling_df))

        with st.expander("Fencing.csv", expanded=False):
            st.dataframe(nanDataframe(fencing_df))

        with st.expander("Diving.csv", expanded=False):
            st.dataframe(nanDataframe(diving_df))

        with st.expander("Cycling BMX Freestyle.csv", expanded=False):
            st.dataframe(nanDataframe(cycling_bmx_freestyle_df))

        with st.expander("Modern Pentathlon.csv", expanded=False):
            st.dataframe(nanDataframe(modern_pentathlon_df))

        with st.expander("Table Tennis.csv", expanded=False):
            st.dataframe(nanDataframe(table_tennis_df))

        with st.expander("Skateboarding.csv", expanded=False):
            st.dataframe(nanDataframe(skateboarding_df))

        with st.expander("Rhythmic Gymnastics.csv", expanded=False):
            st.dataframe(nanDataframe(rhythmic_gymnastics_df))

        with st.expander("Basketball3x3.csv", expanded=False):
            st.dataframe(nanDataframe(basketball3x3_df))

        with st.expander("Artistic Swimming.csv", expanded=False):
            st.dataframe(nanDataframe(artistic_swimming_df))

        with st.expander("Cycling Track.csv", expanded=False):
            st.dataframe(nanDataframe(cycling_track_df))

        with st.expander("Rowing.csv", expanded=False):
            st.dataframe(nanDataframe(rowing_df))
        return
    
st.markdown("---")

def show_info_athlete():
    st.title('Athlete Code Lookup')
        
    # Dropdown for selecting either code or name
    con=st.container(border=True)
    selection_type = con.selectbox('Select by:', ['Code', 'Name'])

    # Handle based on selection type
    if selection_type == 'Code':
        selected_code = con.selectbox('Select Code', athlete_df['code'].tolist())
        # Display the corresponding name based on the selected code
        selected_name = athlete_df[athlete_df['code'] == selected_code]['name'].values[0]
        with con:
            col1,col2=st.columns(2)
            col1.subheader(f"Name: {selected_name}")
            col2.subheader(f"Code: {selected_code}")

    elif selection_type == 'Name':
        selected_name = con.selectbox('Select Name', athlete_df['name'].tolist())
        # Display the corresponding code based on the selected name
        selected_code = athlete_df[athlete_df['name'] == selected_name]['code'].values[0]
        with con:
            col1,col2=st.columns(2)
            col1.subheader(f"Name: {selected_name}")
            col2.subheader(f"Code: {selected_code}")
    
    if 'active_view' not in st.session_state:
            st.session_state.active_view = None
    # Button layout
    col1, col2, col3, col4 = st.columns(4)
    info_btn = col1.button("Athlete Info", icon=":material/contacts:", use_container_width=True)
    country_btn = col2.button("Country", icon=":material/flag_2:", use_container_width=True)
    discipline_btn=col3.button("Discipline",icon=":material/sprint:",use_container_width=True)
    venue_btn=col4.button("Venue",icon=":material/pin_drop:",use_container_width=True)
    # Update session state based on button clicks
    if info_btn:
        st.session_state.active_view = 'info_btn'
    if country_btn:
        st.session_state.active_view = 'country_btn'
    if discipline_btn:
        st.session_state.active_view = 'discipline_btn'
    if venue_btn:
        st.session_state.active_view = 'venue_btn'

    # Lookup athlete
    athlete = athlete_df[athlete_df["code"] == selected_code]
    if athlete.empty:
        st.error("Athlete not found.")
        st.stop()

    athlete = athlete.iloc[0]
    athlete_code = athlete["code"]
    country_code = athlete["country_code"]
    nationality_code = athlete["nationality_code"]
    disciplines = athlete["disciplines"]
    events = athlete["events"]

    # --- Tab Layout ---
    #tab1, tab2, tab3, tab4 = st.tabs(["Athlete Info", "Country/NOC", "Discipline", "Venues"])

    # Tab 1: Athlete Info
    #with tab1:
    if st.session_state.active_view == 'info_btn':
        st.subheader("🏃 Athlete Profile")
        st.dataframe(nanDataframe(pd.DataFrame([athlete])))

        st.subheader("🎖️ Medals")
        # Convert both to string to ensure reliable match
        athlete_code_str = str(athlete_code)
        medals_df["code"] = medals_df["code"].astype(str)

        # Now filter
        athlete_medals = medals_df[medals_df["code"] == athlete_code_str]
        if not athlete_medals.empty:
            st.dataframe(nanDataframe(athlete_medals))
        else:
            st.info("No medals found for this athlete.")

        st.subheader("🏅 Medallist Appearances")
        st.dataframe(nanDataframe(medallists_df[medallists_df["code_athlete"] == athlete_code]))

        st.subheader("👥 Teams")
        teams_df["athletes_codes"] = teams_df["athletes_codes"].astype(str)
        team_matches = teams_df[teams_df["athletes_codes"].str.contains(str(athlete_code))]
        st.dataframe(nanDataframe(team_matches))

    # Tab 2: Country/NOC
    #with tab2:
    if st.session_state.active_view == 'country_btn':
        st.subheader("🌍 Country (country_code)")
        st.dataframe(nanDataframe(nocs_df[nocs_df["code"] == country_code]))
        st.subheader("🥇 Country Medal Totals")
        st.dataframe(nanDataframe(medals_total_df[medals_total_df["country_code"] == country_code]))

        st.subheader("🌏 Nationality (nationality_code)")
        st.dataframe(nanDataframe(nocs_df[nocs_df["code"] == nationality_code]))
        st.subheader("🏅 Nationality Medal Totals")
        st.dataframe(nanDataframe(medals_total_df[medals_total_df["country_code"] == nationality_code]))

    #with tab3:
    if st.session_state.active_view == 'discipline_btn':
        st.subheader("📚 Athlete Disciplines")
        st.write(disciplines)
        
        # Filter schedule data to match disciplines (exact string match)
        if disciplines:
            discipline_schedule = schedules_df[schedules_df["discipline"] == disciplines]  # Exact match        
            
            # NEW FILTER: Only show events that exactly match athlete's events
            if events:
                exact_event_matches = discipline_schedule[discipline_schedule["event"] == events]  # Exact match
                st.subheader("🗓️ Discipline Schedule")
                st.dataframe(nanDataframe(exact_event_matches))

            if events:
                # Check if any event matches the athlete's events (exact string match)
                event_schedule = discipline_schedule[discipline_schedule["event"] == events]
                #st.subheader("🏅 Event Schedule")
                #st.dataframe(event_schedule)
            
                # Additional linked events and preliminary schedules
                discipline_codes = event_schedule["discipline_code"].unique().tolist()

                if discipline_codes:
                    st.subheader("🎯 Linked Events")
                    temp_events_df=events_df[events_df["event"]== events]
                    st.dataframe(nanDataframe(temp_events_df[temp_events_df["sport_code"].isin(discipline_codes)]))

                    st.subheader("⏱️ Preliminary Schedules")
                    st.dataframe(nanDataframe(schedules_preliminary_df[schedules_preliminary_df["sport_code"].isin(discipline_codes)]))
                else:
                    st.info("No linked discipline codes found for this athlete.")
    # Tab 4: Venues
    #with tab4:
    if st.session_state.active_view == 'venue_btn':
        # Clean venue columns to remove unwanted characters (like dashes, spaces)
        def clean_venue(val):
            return str(val).strip().replace("–", " ").replace("-", " ").lower()

        schedules_df["venue_clean"] = schedules_df["venue"].apply(clean_venue)
        venues_df["venue_clean"] = venues_df["venue"].apply(clean_venue)
        
        # Get athlete events (as string)
        athlete_events = str(athlete["events"]) if pd.notna(athlete["events"]) else ""
        
        # Filter schedules by event match (string comparison)
        schedule_event_match = schedules_df[
            (schedules_df["discipline"] == str(disciplines)) &  # Exact match for discipline
            (schedules_df["event"] == athlete_events)           # Exact match for event
        ]

        # Get cleaned venue names from filtered schedule
        used_clean_venues = schedule_event_match["venue_clean"].dropna().unique().tolist()

        # Match with venues_df
        matched_venues = venues_df[venues_df["venue_clean"].isin(used_clean_venues)]

        st.subheader("📍 Matched Venues for Athlete Events")
        if not matched_venues.empty:
            st.dataframe(nanDataframe(matched_venues))
        else:
            st.info("No matching venues found for the athlete's disciplines and events.")
    return

def show_info_coach():
    st.title('Coach Code Lookup')
        
    # Dropdown for selecting either code or name
    con = st.container(border=True)
    selection_type = con.selectbox('Select by:', ['Code', 'Name'],key="co6")

    # Handle based on selection type
    if selection_type == 'Code':
        selected_code = con.selectbox('Select Code', coaches_df['code'].tolist(),key="co5")
        # Display the corresponding name based on the selected code
        selected_name = coaches_df[coaches_df['code'] == selected_code]['name'].values[0]
        with con:
            col1, col2 = st.columns(2)
            col1.subheader(f"Name: {selected_name}")
            col2.subheader(f"Code: {selected_code}")

    elif selection_type == 'Name':
        selected_name = con.selectbox('Select Name', coaches_df['name'].tolist(),key="co4")
        # Display the corresponding code based on the selected name
        selected_code = coaches_df[coaches_df['name'] == selected_name]['code'].values[0]
        with con:
            col1, col2 = st.columns(2)
            col1.subheader(f"Name: {selected_name}")
            col2.subheader(f"Code: {selected_code}")
    
    if 'active_view' not in st.session_state:
        st.session_state.active_view = None
        
    # Button layout
    col1, col2, col3 = st.columns(3)
    info_btn = col1.button("Coach Info", icon=":material/contacts:", use_container_width=True,key="co1")
    country_btn = col2.button("Country", icon=":material/flag_2:", use_container_width=True,key="co2")
    discipline_btn = col3.button("Discipline", icon=":material/sprint:", use_container_width=True,key="co3")
    
    # Update session state based on button clicks
    if info_btn:
        st.session_state.active_view = 'info_btn'
    if country_btn:
        st.session_state.active_view = 'country_btn'
    if discipline_btn:
        st.session_state.active_view = 'discipline_btn'

    # Lookup coach
    coach = coaches_df[coaches_df["code"] == selected_code]
    if coach.empty:
        st.error("Coach not found.")
        st.stop()

    coach = coach.iloc[0]
    coach_code = coach["code"]
    country_code = coach["country_code"]
    disciplines = coach["disciplines"]
    category = coach["category"]
    function = coach["function"]

    # --- View Sections ---
    if st.session_state.active_view == 'info_btn':
        st.subheader("👔 Coach Profile")
        st.dataframe(nanDataframe(pd.DataFrame([coach])))

    elif st.session_state.active_view == 'country_btn':
        st.subheader("🌍 Country")
        st.dataframe(nanDataframe(nocs_df[nocs_df["code"] == country_code]))
        
    elif st.session_state.active_view == 'discipline_btn':
        st.subheader("📚 Coach Disciplines")
        st.write(disciplines)
        
        if disciplines:
            discipline_schedule = schedules_df[schedules_df["discipline"] == disciplines]
            
            if not discipline_schedule.empty:
                st.subheader("🗓️ Discipline Schedule")
                st.dataframe(nanDataframe(discipline_schedule))
    return

def show_info_technical_official():
    st.title('Technical Official Code Lookup')
        
    # Dropdown for selecting either code or name
    con = st.container(border=True)
    selection_type = con.selectbox('Select by:', ['Code', 'Name'],key="to7")

    # Handle based on selection type
    if selection_type == 'Code':
        selected_code = con.selectbox('Select Code', technical_officials_df['code'].tolist(),key="to6")
        # Display the corresponding name based on the selected code
        selected_name = technical_officials_df[technical_officials_df['code'] == selected_code]['name'].values[0]
        with con:
            col1, col2 = st.columns(2)
            col1.subheader(f"Name: {selected_name}")
            col2.subheader(f"Code: {selected_code}")

    elif selection_type == 'Name':
        selected_name = con.selectbox('Select Name', technical_officials_df['name'].tolist(),key="to5")
        # Display the corresponding code based on the selected name
        selected_code = technical_officials_df[technical_officials_df['name'] == selected_name]['code'].values[0]
        with con:
            col1, col2 = st.columns(2)
            col1.subheader(f"Name: {selected_name}")
            col2.subheader(f"Code: {selected_code}")
    
    if 'active_view' not in st.session_state:
        st.session_state.active_view = None
        
    # Button layout
    col1, col3, col4 = st.columns(3)
    info_btn = col1.button("Official Info", icon=":material/contacts:", use_container_width=True,key="to1")
    org_btn = col3.button("Organization", icon=":material/business:", use_container_width=True,key="to3")
    discipline_btn = col4.button("Discipline", icon=":material/sprint:", use_container_width=True,key="to4")
    
    # Update session state based on button clicks
    if info_btn:
        st.session_state.active_view = 'info_btn'
    if org_btn:
        st.session_state.active_view = 'org_btn'
    if discipline_btn:
        st.session_state.active_view = 'discipline_btn'

    # Lookup official
    official = technical_officials_df[technical_officials_df["code"] == selected_code]
    if official.empty:
        st.error("Technical official not found.")
        st.stop()

    official = official.iloc[0]
    organisation_code = official["organisation_code"]
    disciplines = official["disciplines"]

    # --- View Sections ---
    if st.session_state.active_view == 'info_btn':
        st.subheader("👨‍⚖️ Official Profile")
        st.dataframe(nanDataframe(pd.DataFrame([official])))

        
    elif st.session_state.active_view == 'org_btn':
        st.subheader("🏢 Organization")
        # You would need an organizations_df for this part
        # st.dataframe(nanDataframe(organizations_df[organizations_df["code"] == organisation_code]))
        st.info(f"Organization Code: {organisation_code}")
        
    elif st.session_state.active_view == 'discipline_btn':
        st.subheader("📚 Official Disciplines")
        st.write(disciplines)
        
        if disciplines:
            discipline_schedule = schedules_df[schedules_df["discipline"] == disciplines]
            
            if not discipline_schedule.empty:
                st.subheader("🗓️ Discipline Schedule")
                st.dataframe(nanDataframe(discipline_schedule))
    return
