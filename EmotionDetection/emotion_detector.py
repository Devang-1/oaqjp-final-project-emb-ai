# emotion_detector.py

def emotion_detector(statement):
    # Check for blank input
    if not statement.strip():  # This checks if the statement is empty or contains only whitespace
        # Return a dictionary with all values as None for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Your existing emotion detection code goes here
    # For now, let's simulate a successful output:
    return {
        'anger': 0.004234234, 
        'disgust': 0.000567123, 
        'fear': 0.005678234, 
        'joy': 0.980123456, 
        'sadness': 0.009987654, 
        'dominant_emotion': 'joy'
    }
