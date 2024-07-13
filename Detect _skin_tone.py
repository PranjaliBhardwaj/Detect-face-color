import cv2
import numpy as np

def get_skin_mask(hsv_frame):
    # Define the skin color range in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask for the skin color
    skin_mask = cv2.inRange(hsv_frame, lower_skin, upper_skin)
    return skin_mask

def get_average_skin_color(frame, skin_mask):
    # Calculate the average color of the detected skin region
    skin_region = cv2.bitwise_and(frame, frame, mask=skin_mask)
    mean_color = cv2.mean(skin_region, mask=skin_mask)
    return mean_color

def main():
    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Start capturing video
    cap = cv2.VideoCapture(0)

    # Variable to store the extracted hex color code
    extracted_hex_color = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Extract the face region
            face_region = frame[y:y+h, x:x+w]

            # Convert the face region to HSV color space
            hsv_face = cv2.cvtColor(face_region, cv2.COLOR_BGR2HSV)

            # Get the skin mask
            skin_mask = get_skin_mask(hsv_face)

            # Get the average skin color
            mean_color = get_average_skin_color(face_region, skin_mask)

            # Convert the average color to BGR and Hex formats
            bgr_color = (int(mean_color[0]), int(mean_color[1]), int(mean_color[2]))
            hex_color = "#{:02x}{:02x}{:02x}".format(bgr_color[2], bgr_color[1], bgr_color[0])

            # Store the hex color code and break out of the loop
            extracted_hex_color = hex_color
            break  # Exit the loop after processing the first face

        if extracted_hex_color:
            break  # Exit the main loop once color is extracted

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Print the extracted hex color code for JavaScript to read
    print(extracted_hex_color)

if __name__ == "__main__":
    main()
