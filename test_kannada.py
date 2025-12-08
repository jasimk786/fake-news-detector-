#!/usr/bin/env python3
"""Test script for Kannada fake news detection"""

import requests
import json

# Test data
kannada_text = "ಇದು ಒಂದು ಪರೀಕ್ಷಾ ಸುದ್ದಿ ಲೇಖನವಾಗಿದೆ. ಸರ್ಕಾರವು ಹೊಸ ನೀತಿಯನ್ನು ಘೋಷಿಸಿದೆ."
english_text = "This is a test news article. The government has announced a new policy."

def test_kannada_detection():
    """Test Kannada language detection and analysis"""
    url = "http://localhost:5000/analyzeText"
    
    # You'll need to get a valid JWT token first by logging in
    token = "YOUR_JWT_TOKEN_HERE"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Test Kannada text
    print("Testing Kannada text...")
    response = requests.post(url, 
                           headers=headers, 
                           json={"text": kannada_text})
    
    if response.status_code == 200:
        result = response.json()
        print(f"Language: {result.get('language')}")
        print(f"Prediction: {result.get('prediction')}")
        print(f"Confidence: {result.get('confidence'):.2f}%")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    
    print("\n" + "="*50 + "\n")
    
    # Test English text
    print("Testing English text...")
    response = requests.post(url, 
                           headers=headers, 
                           json={"text": english_text})
    
    if response.status_code == 200:
        result = response.json()
        print(f"Language: {result.get('language')}")
        print(f"Prediction: {result.get('prediction')}")
        print(f"Confidence: {result.get('confidence'):.2f}%")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("Kannada Fake News Detection Test")
    print("="*50)
    test_kannada_detection()