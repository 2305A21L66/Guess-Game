import streamlit as st
import random

# Title of the app
st.title("🎮 Number Guessing Game")

# Generate or retrieve a random number
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Instructions
st.write("I have picked a random number between 1 and 100. Can you guess what it is?")
st.write("Enter your guess below:")

# User input
guess = st.number_input("Your Guess:", min_value=1, max_value=100, step=1, key="user_guess")

# Check button
if st.button("Check"):
    st.session_state.attempts += 1
    if guess < st.session_state.random_number:
        st.warning("🔼 Too low! Try again.")
    elif guess > st.session_state.random_number:
        st.warning("🔽 Too high! Try again.")
    else:
        st.success(f"🎉 Correct! The number was {st.session_state.random_number}.")
        st.success(f"You guessed it in {st.session_state.attempts} attempts.")
        # Reset the game
        if st.button("Play Again"):
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0

# Display the number of attempts
st.write(f"Attempts: {st.session_state.attempts}")