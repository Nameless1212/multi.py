import streamlit as st
def app(cars_df):
	st.subheader("View Data")
	with st.beta_expander("View Full Data Set"):
		st.table(cars_df)
	beta1, beta2, beta3 = st.beta_columns(3)
	with beta1:
		if st.checkbox("Show all column names"):
			st.table(cars_df.columns)
	with beta2:
		if st.checkbox("View Column Data types"):
			st.table(cars_df.dtypes)
	with beta3:
		if st.checkbox("View Column Data"):
			final_selection = st.selectbox("Select feature", ['carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price'])
			st.table(cars_df[final_selection])