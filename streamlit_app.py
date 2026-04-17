import streamlit as st
from st_supabase_connection import SupabaseConnection

st.title("OptionTradeLog Dashboard")

# Initialize Supabase connection (reads from secrets automatically)
conn = st.connection("supabase", type=SupabaseConnection)

# Fetch all data from your table
response = conn.query("*", table="OptionTradeLog", ttl="10m").execute()

if response.data:
    df = response.data   # This returns a list of dicts → Streamlit handles it well

    st.dataframe(df, use_container_width=True)

    # Example charts (change column names to match yours)
    col1, col2 = st.columns(2)
    with col1:
        if "Strike" in df[0] if df else False:
            st.subheader("Strike Distribution")
            st.bar_chart([row.get("Strike") for row in df if row.get("Strike")])

    with col2:
        if "DaysSince" in df[0] if df else False:
            st.subheader("Days Since")
            st.line_chart([row.get("DaysSince") for row in df if row.get("DaysSince")])

else:
    st.warning("No data found in the table.")