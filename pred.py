import streamlit as st
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def prediction(cars_df, carswidth, enginesize, horsepower, drivingforward, carcompanybuick):
	x = cars_df.iloc[:,:-1]
	y = cars_df["price"]
	x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 42, test_size = 0.33)
	linear = LinearRegression()
	linear.fit(x_train, y_train)
	score = linear.score(x_train, y_train)
	pre = linear.predict([[carswidth, enginesize, horsepower, drivingforward, carcompanybuick]])
	y_test_pred = linear.predict(x_test)
	r2 = r2_score(y_test, y_test_pred)
	absolute = mean_absolute_error(y_test, y_test_pred)
	mean = mean_squared_error(y_test, y_test_pred)
	sqmean = np.sqrt(mean_squared_error(y_test, y_test_pred))
	log_mean = mean_squared_log_error(y_test, y_test_pred)
	return pre, score, r2, absolute, sqmean, log_mean

def app(cars_df):
	st.markdown("<p style='color:blue;font-size:25px'>This app uses <b>Linear regression</b> to predict the price of a car based on your inputs.", unsafe_allow_html = True)
	st.subheader("Select Values:")
	carswidth = st.slider("Car Width", float(cars_df["carwidth"].min()), float(cars_df["carwidth"].max()))     
	enginesize = st.slider("Engine Size", int(cars_df["enginesize"].min()), int(cars_df["enginesize"].max()))
	horsepower = st.slider("Horse Power", int(cars_df["horsepower"].min()), int(cars_df["horsepower"].max()))    
	drivingforward = st.radio("Is it a forward drive wheel car?", ("Yes", "No"))
	if drivingforward == 'No':
		drivingforward = 0
	else:
		drivingforward = 1
	carcompanybuick = st.radio("Is the car manufactured by Buick?", ("Yes", "No"))
	if carcompanybuick == 'No':
		carcompanybuick = 0
	else:
		carcompanybuick = 1
	# When 'Predict' button is clicked, the 'prediction()' function must be called 
	# and the value returned by it must be stored in a variable, say 'price'. 
	# Print the value of 'price' and 'score' variable using the 'st.success()' and 'st.info()' functions respectively.
	if st.button("Predict"):
		st.subheader("Prediction results:")
		price, score, car_r2, car_mae, car_msle, car_rmse = prediction(cars_df, carswidth, enginesize, horsepower, drivingforward, carcompanybuick)
		st.success("The predicted price of the car: ${:,}".format(int(price)))
		st.info("Accuracy score of this model is: {:2.2%}".format(score))
		st.info(f"R-squared score of this model is: {car_r2:.3f}")  
		st.info(f"Mean absolute error of this model is: {car_mae:.3f}")  
		st.info(f"Mean squared log error of this model is: {car_msle:.3f}")  
		st.info(f"Root mean squared error of this model is: {car_rmse:.3f}")
#b stands for bold
#p stands for paragraph
#html is for webpages