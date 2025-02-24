import cv2

# Load images
faculty_img = cv2.imread('Plaksha_Faculty.jpg')
template_img = cv2.imread('Dr_Shashi_Tharoor.jpg')

if faculty_img is None or template_img is None:
    print("Error loading images")
else:
    print("Images loaded successfully")