import streamlit as st
from agent.planner import generate_itinerary
from agent.email_sender import send_email
from agent.pdf_generator import generate_pdf
from agent.map_embedder import generate_map_embed_url

st.set_page_config(page_title="Agentic AI Travel Planner", layout="centered")

st.title("🌍 Agentic AI Travel Itinerary Planner")

with st.form("trip_form"):
    destination = st.text_input("Where do you want to go?")
    days = st.number_input("For how many days?", min_value=1, max_value=30, step=1)
    user_email = st.text_input("Enter your email to receive the itinerary (optional)")
    submitted = st.form_submit_button("Plan My Trip")

if submitted:
    if destination and days:
        with st.spinner("Planning your adventure..."):
            itinerary = generate_itinerary(destination, days)

            st.success("Here is your itinerary:")
            st.text_area("Travel Itinerary", itinerary, height=400)

            # Show Map
            st.subheader("🗺️ Destination Map")
            map_url = generate_map_embed_url(destination)
            st.components.v1.iframe(map_url, height=300)

            # Generate PDF
            pdf_file = generate_pdf(itinerary, destination)
            with open(pdf_file, "rb") as f:
                st.download_button("📄 Download Itinerary PDF", f, file_name=pdf_file, mime="application/pdf")

            # Send Email
            if user_email:
                try:
                    send_email(user_email, f"{destination} Travel Plan", itinerary)
                    st.success(f"📧 Itinerary sent to {user_email}")
                except Exception as e:
                    st.error(f"Error sending email: {e}")
    else:
        st.error("Please fill in all fields.")
