#!interpreter [optional-arg]
# -*- coding: utf-8 -*-
#
"""
user_routes.py

"""

#Built-in/Generic
import datetime

#Libs
from flask import Flask, g, redirect, render_template, request, url_for, session, flash
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
		Table, Column, Integer, String, MetaData, ForeignKey, Boolean
	)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo

from werkzeug.security import check_password_hash, generate_password_hash
from flask_bcrypt import check_password_hash, generate_password_hash

#Modules
from flask_app import db, app
from models import User, Subject, Bookmark, Crypto, Timer, Note



class Registration_form(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="New Password and Confirm Password do not match.")])
	submit = SubmitField('register')

class Login_form(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('login')

class Delete_Account_form(FlaskForm):
	#username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('delete_account')

class Change_Password_form(FlaskForm):
	#username = StringField('Username', validators=[DataRequired()])
	current_password = PasswordField('Current Password', validators=[DataRequired()])
	new_password = PasswordField('New Password', validators=[DataRequired()])
	new_password2 = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password', message="New Password and Confirm Password do not match.")])
	submit = SubmitField('change_password')

class User_Update_form(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	home_title = StringField('Home Title')
	latitude = DecimalField('Latitude')
	longitude = DecimalField('Longitude')
	country = StringField('Country')

	morning_greeting = StringField('Morning_greeting')
	afternoon_greeting = StringField('Afternoon_greeting')
	evening_greeting = StringField('Evening_greeting')
	night_greeting = StringField('Night_greeting')
	submit = SubmitField('Update_settings')



@app.route("/registration", methods=('GET', 'POST'))
def registration():

	#besser weg https://stackoverflow.com/questions/13585663/flask-wtfform-flash-does-not-display-errors

	form = Registration_form()#if "GET", create form to send to template
	if form.validate_on_submit():

		name = form.username.data
		password = form.password.data
		confirmation = form.password2.data
		error = None

		if User.query.filter_by(name = name).first():
			error = 'user name already registered.'
			flash(error)
			print(error)


		if len(password) < 8:
			error = 'password must be at least 8 characters long.'
			flash(error)
			print(error)

		if password != confirmation:
			error = 'password and confirmation password must match.'
			flash(error)
			print(error)

		if error:
			return render_template('auth/registration.html', form=form)

		result = user_create(name, generate_password_hash(password))

		if result:
			return redirect(url_for('login'))


	return render_template('auth/registration.html', form=form)


#Login_wtf
@app.route("/login", methods=('GET', 'POST'))
def login():

	form = Login_form()#if "GET", create form to send to template
	if form.validate_on_submit():

		name = form.username.data
		password = form.password.data
		error = None

		user = User.query.filter_by(name = name).first()#first or else you get an iterator

		if not user:
			error = 'User not found.'
			print(error)
			flash(error)

			#not check_password_hash(user.password, password)
		elif not check_password_hash(user.password, password):
			error = 'User name or password False.'
			print(error)
			flash(error)

		if not error:
			session.clear()
			session['user_id'] = user.id
			session.permanent = True
			#with just dashboard() I get an onscreen error Badrequest
			return redirect(url_for('index'))
			print(error)
	return render_template('auth/login.html', form=form)

@app.route("/logout")
def logout():
	if "user_id" not in session:
		return redirect(url_for('error_404'))
	session.clear()
	return redirect(url_for('index'))

#@app.route("/user_read")
def user_read(id):
	user = User.query.get(id)
	return user

#@app.route("/user_create")
#not a route, only a funciton, safe!
def user_create(name, password):
	user = User(name=name, password=password)
	db.session.add(user)
	db.session.commit()
	#user.ip_address = request.remote_addr
	#Init Getting Started List
	for i in range(6):

		subject = Subject(title="Subject "+str(i), parent_user=user.id)
		db.session.add(subject)
		print("Added Subject "+str(i))
		db.session.commit()

		bookmark = Bookmark(title="Leer "+str(i), hotkey="leer", link="google.ca", parent_subject=subject.id, parent_user=user.id)
		db.session.add(bookmark)
		print("Added Leer "+str(i))
		db.session.commit()

		crypto = Crypto(title="Leer "+str(i), link="google.ca", crypto_acronym="ETH", fiat_acronym="CAD", parent_user=user.id)
		db.session.add(crypto)
		print("Added crypto "+str(i))
		db.session.commit()

		timer = Timer(title="Leer "+str(i), hours=0, minutes=0, seconds=30, parent_user=user.id)
		db.session.add(timer)
		print("Added timer "+str(i))
		db.session.commit()

	note = Note(title="Blank Note...", text="Enter text here...", parent_user=user.id)
	db.session.add(note)
	print("Added note " + str(i))
	db.session.commit()

	return True

@app.route("/update_user", methods=('GET', 'POST'))
def update_user():
	if "user_id" not in session:
		return redirect(url_for('error_404'))
	form = User_Update_form()
	#if request.method == "POST":

	if form.validate_on_submit():
		error = None
		print('validated!')
		user = db.session.query(User).get(session["user_id"])
		form = User_Update_form()

		if user == None:
			error = "User not found."
			print(error)
			flash(error)


		if error == None:
			user.name = form.username.data
			user.home_title = form.home_title.data
			user.country = form.country.data
			user.latitude = form.latitude.data
			user.longitude = form.longitude.data
			user.morning_greeting = form.morning_greeting.data
			user.afternoon_greeting = form.afternoon_greeting.data
			user.evening_greeting = form.evening_greeting.data
			user.night_greeting = form.night_greeting.data

			db.session.commit()
			print('data commited')
			return redirect(url_for('index'))


	user = db.session.query(User).get(session["user_id"])
	if user.latitude == None:
		user.latitude = 0.
	if user.longitude == None:
		user.longitude = 0.

	return jsonify({'data': render_template('auth/update_user.html', \
	#return render_template('auth/update_user.html', form=form,\
	name=user.name, password=user.password,\
	country=user.country, latitude=user.latitude, longitude=user.longitude,\
	afternoon_greeting=user.afternoon_greeting, morning_greeting=user.morning_greeting,\
	evening_greeting=user.evening_greeting, night_greeting=user.night_greeting, home_title=user.home_title)})


#Login_wtf
@app.route("/change_password", methods=('GET', 'POST'))
def change_password():
	if "user_id" not in session:
		return redirect(url_for('error_404'))
	print("password change before")
	form = Change_Password_form()#if "GET", create form to send to template
	if form.validate_on_submit():
		print("password change")
		#name = form.username.data
		current_password = form.current_password.data
		new_password = form.new_password.data
		new_password2 = form.new_password2.data
		error = None

		user = User.query.filter_by(id=session["user_id"]).first()#first or else you get an iterator

		if not user:
			error = 'User not found.'
			print(error)
			flash(error)

		#not check_password_hash(user.password, password)
		elif not check_password_hash(user.password, current_password):
			error = 'User name or password False.'
			print(error)
			flash(error)

		elif new_password != new_password2:
			error = 'Password and confirmation do not match.'
			print(error)
			flash(error)

		if not error:
			user.password = generate_password_hash(new_password)
			db.session.commit()
			print('data commited')
			return redirect(url_for('index'))

	return render_template('auth/change_password.html', form=form)

@app.route("/delete_account", methods=('GET', 'POST'))
def delete_account():
	if "user_id" not in session:
		return redirect(url_for('error_404'))
	print(session["user_id"])
	form = Delete_Account_form()#if "GET", create form to send to template
	if form.validate_on_submit():

		#name = form.username.data
		password = form.password.data
		error = None

		user = User.query.filter_by(id=session["user_id"]).first()#first or else you get an iterator

		if not user:
			error = 'User not found.'
			print(error)
			flash(error)

			#not check_password_hash(user.password, password)
		elif not check_password_hash(user.password, password):
			error = 'User name or password False.'
			print(error)
			flash(error)

		if not error:
			delete_user(session["user_id"])
			return redirect(url_for('index'))

	return render_template('auth/delete_account.html', form=form)

#@app.route("/delete_user")
def delete_user(id):
	#pass user id in form?
	user = db.session.query(User).get(id)
	db.session.delete(user)
	db.session.commit()
	session.clear()
	return

#This is cool (if calls the following function
#before every request. and there is a bp version.

@app.before_request
def load_logged_in_user():
	#I think I needed "get()" instead of just session['key']
	#for the case that session doesn't have a user_id yet?
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = user_read(user_id)
