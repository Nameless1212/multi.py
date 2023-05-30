import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option("deprecation.showPyplotGlobalUse", False)
def app(cars_df):
	st.subheader("Visualise Data")
	select = st.multiselect("Select Graph", ("Histogram", "Boxplot", "Heatmap"))
	if "Histogram" in select:
		hsl = st.selectbox("Select Column", ["carwidth", "enginesize", "horsepower"])
		plt.figure(figsize =(10, 7))
		sns.histplot(cars_df[hsl], bins = "sturges")
		st.pyplot()
	if "Boxplot" in select:
		bsl = st.selectbox("Select Column", ["carwidth", "enginesize", "horsepower"])
		plt.figure(figsize =(10, 7))
		sns.boxplot(cars_df[bsl])
		st.pyplot()
	if "Heatmap" in select:
		plt.figure(figsize =(10, 7))
		sns.heatmap(cars_df.corr(), annot = True)
		st.pyplot()