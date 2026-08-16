password = "user123"
#password = "p@ssword123"
correct_password = "p@ssword123"
correct = "Login successful!"
incorrect = "Incorrect password, try again."
login_message = correct if password == correct_password else incorrect

# Testing
print("Login Status:", login_message)