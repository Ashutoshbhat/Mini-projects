import cv2

# Open the default camera (0 represents the default webcam)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    
    # Check if the frame was successfully captured
    if not ret:
        print("Error: Failed to capture frame.")
        break
    
    # Display the captured frame
    cv2.imshow('Camera Feed', frame)

    # Wait for a key press and exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()



