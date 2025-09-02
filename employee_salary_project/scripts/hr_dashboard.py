import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import plotly.express as px
# ==============================
# Authentication Setup
# ==============================
names = ["Admin"]
usernames = ["likhi"]
passwords = ["123"]

credentials = {
    "usernames": {
        usernames[i]: {"name": names[i], "password": passwords[i]}
        for i in range(len(usernames))
    }
}
authenticator = stauth.Authenticate(
    credentials,
    "employee_dashboard",
    "abcdef",
    1
)
# ================
# Login Page 
# ================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    authenticator.login(location="main")
# ================
# Dashboard 
# ================
if st.session_state.get("authentication_status"):
    name = st.session_state["name"]
    st.sidebar.write(f"👋 Welcome {name}")
    authenticator.logout("Logout", "sidebar")
    st.title("📊 HR Employee Salary Dashboard")
    # ---------------------
    # Upload CSV
    # ---------------------
    uploaded_file = st.file_uploader("Upload Employee Data CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # Standardize Column Names
        df.columns = df.columns.str.strip().str.replace(" ", "").str.capitalize()
        # Check required columns
        required_cols = ["Salary", "Department", "Jobtitle"]
        for col in required_cols:
            if col not in df.columns:
                st.error(f"❌ CSV is missing required column: {col}")
                st.stop()
        # Data Cleaning
        df.drop_duplicates(inplace=True)
        df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
        df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
        # ==============================
        # Sidebar Page Navigation
        # ==============================
        page = st.sidebar.radio("Navigation", ["Cleaned Data", "Charts & KPIs"])
        filtered_df = df.copy()

        # Department filter
        departments = df["Department"].unique()
        selected_departments = st.sidebar.multiselect(
            "Select Department(s)", options=departments, default=departments
        )
        filtered_df = filtered_df[filtered_df["Department"].isin(selected_departments)]

        # Job Title filter
        job_titles = df["Jobtitle"].unique()
        selected_jobs = st.sidebar.multiselect(
            "Select Job Title(s)", options=job_titles, default=job_titles
        )
        filtered_df = filtered_df[filtered_df["Jobtitle"].isin(selected_jobs)]

        # Salary range filter
        min_salary = int(df["Salary"].min())
        max_salary = int(df["Salary"].max())
        salary_range = st.sidebar.slider(
            "Select Salary Range",
            min_value=min_salary,
            max_value=max_salary,
            value=(min_salary, max_salary)
        )
        filtered_df = filtered_df[
            (filtered_df["Salary"] >= salary_range[0]) &
            (filtered_df["Salary"] <= salary_range[1])
        ]
        #  Cleaned Data
        if page == "Cleaned Data":
            st.subheader("🧹 Cleaned Employee Data")
            st.dataframe(filtered_df)
            # Download Cleaned Data
            if not filtered_df.empty:
                csv = filtered_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Cleaned Data as CSV",
                    data=csv,
                    file_name="cleaned_employee_data.csv",
                    mime="text/csv"
                )
        #  Charts & KPIs
        elif page == "Charts & KPIs":
            st.subheader("📈 HR Key Performance Indicators (KPIs)")

            avg_salary = filtered_df["Salary"].mean() if not filtered_df.empty else 0
            st.metric("Average Salary", f"{avg_salary:,.2f}")
            total_emp = filtered_df.shape[0]
            st.metric("Total Employees", total_emp)

            # Average Salary by Department
            st.subheader("Average Salary by Department")
            if not filtered_df.empty:
                dept_salary = filtered_df.groupby("Department")["Salary"].mean().reset_index()
                fig_dept = px.bar(
                    dept_salary,
                    x="Department",
                    y="Salary",
                    color="Salary",
                    color_continuous_scale="Blues",
                    text="Salary"
                )
                fig_dept.update_layout(yaxis_title="Average Salary")
                st.plotly_chart(fig_dept, use_container_width=True)

            # Average Salary by Job Title
            st.subheader("Average Salary by Job Title")
            if not filtered_df.empty:
                job_salary = filtered_df.groupby("Jobtitle")["Salary"].mean().reset_index()
                fig_job = px.bar(
                    job_salary,
                    x="Jobtitle",
                    y="Salary",
                    color="Salary",
                    color_continuous_scale="Greens",
                    text="Salary"
                )
                fig_job.update_layout(yaxis_title="Average Salary")
                st.plotly_chart(fig_job, use_container_width=True)

            # Employees per Department
            st.subheader("Employees per Department")
            if not filtered_df.empty:
                dept_count = filtered_df["Department"].value_counts().reset_index()
                dept_count.columns = ["Department", "Count"]
                fig_dept_count = px.bar(
                    dept_count,
                    x="Department",
                    y="Count",
                    color="Count",
                    color_continuous_scale="Oranges",
                    text="Count"
                )
                st.plotly_chart(fig_dept_count, use_container_width=True)

            # Top 5 Earners
            st.subheader("💰 Top 5 Earners")
            if not filtered_df.empty:
                if "Name" in filtered_df.columns:
                    top5 = filtered_df.nlargest(5, "Salary")[["Name", "Jobtitle", "Department", "Salary"]]
                else:
                    top5 = filtered_df.nlargest(5, "Salary")[["Jobtitle", "Department", "Salary"]]
                st.dataframe(top5)

            # Top 5 Least Earners
            st.subheader("💸 Top 5 Least Earners")
            if not filtered_df.empty:
                if "Name" in filtered_df.columns:
                    least5 = filtered_df.nsmallest(5, "Salary")[["Name", "Jobtitle", "Department", "Salary"]]
                else:
                    least5 = filtered_df.nsmallest(5, "Salary")[["Jobtitle", "Department", "Salary"]]
                st.dataframe(least5)

    else:
        st.info("👆 Please upload your employee_data.csv file to see the dashboard")
# ---------------------
# Handle login errors
# ---------------------
elif st.session_state.get("authentication_status") is False:
    st.error("❌ Username/password is incorrect")
