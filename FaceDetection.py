import cv2
import face_recognition

 #Load known face encodings and names
 known_face_encodings = [] 
 known_face_names = []


 # Load known faces and their names here
 known_person1_image = face_recognition.load_image_file("C:\Users\Admin\Downloads\person 1.jpegperson1.jpg")
 known_person2_image = face_recognition.load_image_file("C:\Users\Admin\Downloads\person 2.jpegperson2.jpg")
 known_person3_image = face_recognition.load_image_file("C:\Users\Admin\Downloads\person 3.jpegperson3.jpg")

 known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
 known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
 known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encoding) 
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_names.append("Salman Khan")
known_face_names.append("Madhuri Dixit")
known_face_names.append("Sharukh Khan")

# Initialize Webcam
Video_Capture = cv2.VideoCapture(0)

while True:
    #Capture frame-by-frame
    ret, frame = Video_Capture.read()

    #Find all face locations in the current frames
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_locations(frame,face_locations)

    #Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name ="Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 225),2)  
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 225), 2)

     # Display the resulting frame
    cv2.imshow("Videos", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.WaitKey(1) & 0xff == ord('q'):
        break

 # Release the webcam and close OpenCV windows
 Video_Capture.release()
 cv2.destroyAIIWindows()
