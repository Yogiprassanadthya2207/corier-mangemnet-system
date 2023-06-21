# Courier-Mangemnet-System


This code is a basic implementation of a Courier Management System using the Tkinter library in Python. Here's a breakdown of the code:

The code begins by importing the necessary modules: tkinter and PIL.
It defines several global lists and functions for different operations in the courier management system.
The call() function is called when the "Get started" button is clicked. It opens a new window (Toplevel) where users can choose to sign up, login, or track their order.
The track() function is called when the "Track order" button is clicked. It opens a new window where users can enter their order details and check the status of their order.
The status() function displays a message box with the status of the order. In this case, it always shows a fixed message "Your order will be delivered on Friday."
The signup() function is called when the "Sign-Up" button is clicked. It opens a new window where users can enter their details to register.
The register() function retrieves the entered details from the sign-up form and appends them to the respective lists.
The login() function is called when the "Login" button is clicked. It opens a new window where users can enter their username and password to log in.
The submit() function retrieves the entered username and password from the login form and checks if they match the stored values. If the credentials are correct, a message box is displayed with a success message; otherwise, an error message is shown.
Finally, the main Tkinter window is created (root), with a title and a "Get started" button. The window size and appearance are set, and the main event loop (root.mainloop()) is started to handle user interactions.
Overall, this code provides a basic interface for users to sign up, log in, and track their courier orders in a Courier Management System.




