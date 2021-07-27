# Movie-Management-System
A GUI based Movie Management System made with the help of Tkinter, SQLite3 and Python.

<!-- PROJECT LOGO -->
<p align="center">
  <a href="">
    <img src="https://sqliteviewer.com/blog/wp-content/uploads/2015/06/sqlite-database.png" alt="Logo" width="160" height="80"><img src="https://static.javatpoint.com/python/images/tkinter-tutorial.png" alt="Logo" width="160" height="200">
  </a>

  <h2 align="center">Movie Management System</h2>

  <center>
    <a href="https://github.com/Jeel13/Movie-Management-System"><strong>Explore the docs »</strong></a>
</center>
<br>


<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-The-Project">About The Project</a></li>
    <li><a href="#Prerequisites">Prerequisites</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Contacts">Contacts</a></li>
  </ol>
</details>

## About-The-Project

This GUI based project is aimed for the use of admins of the theater to manage the information related to the movies. It is built with Python, SQLite3 and Tkinter.

### ScreenShots
![](https://raw.githubusercontent.com/Jeel13/Movie-Management-System/main/Screenshots/SS1.jpeg)

![](https://raw.githubusercontent.com/Jeel13/Movie-Management-System/main/Screenshots/SS2.jpg)

![](https://raw.githubusercontent.com/Jeel13/Movie-Management-System/main/Screenshots/SS3.jpg)

![](https://raw.githubusercontent.com/Jeel13/Movie-Management-System/main/Screenshots/SS4.jpg)


## Prerequisites

* Python3
* PyQT5
* SQLite

## Features

- Sign up/Login feature
-  Multiple Admins can edit the data
-  Admins can,
	-  Add new Movies
	-  Remove Movies
	-  Search Movies
	-  Display the Movie list
	-  Update the Movie information
- Storing the Movie details in a file for later uses

## Usage

- Signup / Login
	- You can sign up with a new account by clicking on the signup button or login directly if you have already made the account.

- Main Window
	- On this window you will be able to add, display, delete, search and update the movie details like
		1. Movie ID 
		2. Name
		3. Genre
		4. Release date
		5. Budget
		6. Duration 
		7. Rating

	- We can switch to Cast and Director windows using their buttons.

- Director and Cast window
	-  In these windows you can add details of director and cast.

- **The concept of Refrential Integrity is used.**
	- After deleting a specific movies's details, its respective cast and director data will also be deleted on the basis of Movie ID (foregin key).

-Finally you can Log out and can Login again.


## Contacts

Krupal Patel - [@iamkp1010](https://github.com/iamkp1010) - krupalpatel150@gmail.com

Jeel Patel - [@Jeel13](https://github.com/Jeel13) - jeel0patel31052002@gmail.com

Jeel Patel - [@jeelpatel1812](https://github.com/jeelpatel1812) - jeelp9216@gmail.com
