import cv2

# Create a VideoCapture object and open the camera (try index 0 if 4 doesn't work)
cap = cv2.VideoCapture(4)  # Index 0 for default camera
print('is working')

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

i = 0  # Counter for image naming

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press 'q' on the keyboard to exit the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # Press 'm' to capture and save the current frame
        if cv2.waitKey(25) & 0xFF == ord('m'):
            # Save the captured frame as an image
            filename = f'/home/hackathon/Desktop/wojtek/Data_img1/board3_{i}.png'
            cv2.imwrite(filename, frame)
            print(f"Photo taken and saved: {filename}")
            i += 1

    else:
        break

# When everything is done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
