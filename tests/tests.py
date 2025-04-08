"""
Tests for ../app.py

Run from the project directory (not the tests directory) with the invocation `pytest tests/tests.py`
"""
import streamlit as st
from streamlit.testing.v1 import AppTest

def test_button_increments_counter():
    """Test that the counter increments when the button is clicked."""
    at = AppTest.from_file("app.py").run()

    # Initialize the session state.
    # Note that we use at.session_state, not st.session_state. This is the testing session_state object.
    at.session_state.count = 1

    # Click the button
    at.button(key="increment").click().run()

    # Assert that the counter has been incremented
    assert at.session_state.count == 2

def test_button_decrements_counter():
    # TODO test that the decrement button works
    at = AppTest.from_file("app.py").run()
    
    # Initialize the session state
    at.session_state.count = 5
    
    # Click the decrement button
    at.button(key="decrement").click().run()
    
    # Assert that the counter has been decremented
    assert at.session_state.count == 4

def test_button_increments_counter_ten_x():
    # TODO test that the increment button works in ten_x mode
    at = AppTest.from_file("app.py").run()

    # Initialize the session state
    at.session_state.count = 1
    
    # Enable ten_x mode
    at.checkbox(key="ten_x").check().run()
    
    # Click the button
    at.button(key="increment").click().run()

    # Assert that the counter has been incremented
    assert at.session_state.count == 11



def test_button_decrements_counter_ten_x():
    # TODO test that the decrement button works in ten_x mode
    at = AppTest.from_file("app.py").run()
    
    # Initialize the session state
    at.session_state.count = 24
    
    # Enable ten_x mode
    at.checkbox(key="ten_x").check().run()
    
    # Click the decrement button
    at.button(key="decrement").click().run()
    
    # Assert that the counter has been decremented by 10
    assert at.session_state.count == 14
    
def test_decrement_stops_at_zero():
    """Test that the counter does not go below zero when decremented."""
    at = AppTest.from_file("app.py").run()
    
    # Initialize the session state to 0
    at.session_state.count = 0
    
    # Click the decrement button
    at.button(key="decrement").click().run()
    
    # Assert that the counter remains at 0
    assert at.session_state.count == 0
    
def test_decrement_stops_at_zero_ten_x():
    """Test that the counter does not go below zero when decremented in ten_x mode."""
    at = AppTest.from_file("app.py").run()
    
    # Initialize the session state to 5
    at.session_state.count = 5
    
    # Enable ten_x mode
    at.checkbox(key="ten_x").check().run()
    
    # Click the decrement button (would normally subtract 10, but should stop at 0)
    at.button(key="decrement").click().run()
    
    # Assert that the counter is 0, not -5
    assert at.session_state.count == 0

def test_output_text_correct():
    """Test that the text shows the correct value."""
    at = AppTest.from_file("app.py").run()

    # Initialize session state
    at.session_state.count = 0
    at.session_state.ten_x = False

    # Increment once at 1x, once at 10x.
    at.button(key="increment").click().run()
    at.checkbox(key="ten_x").check().run()
    at.button(key="increment").click().run()

    # Check text value
    assert at.markdown[0].value == "Total count is 11"