import cv2

try:
    # Load the images used in the notebook
    faculty_img = cv2.imread('plaksha_Faculty.jpg')
    template_img = cv2.imread('Dr_Shashi_Tharoor.jpg')
    
    if faculty_img is None or template_img is None:
        raise ValueError("Failed to load images")
    
    print("All images and files loaded successfully")
except Exception as e:
    print(f"Error: {e}")