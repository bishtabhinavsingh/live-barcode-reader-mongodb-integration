from pyzbar import pyzbar
import cv2
import time, datetime
from mongo_access import get_database


def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        # update entries to database
        update_db(str(obj.type), str(obj.data))

    return image

def update_db(type,data):
    # gets database
    collection = get_database()
    # inserts the new entry
    collection.insert_one({
        "Type": type,
        "Data": data,
        "Time": datetime.datetime.now()
    })
    print("Update Success!")


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    start = time.time()
    while True:
        # read the frame from the camera
        _, frame = cap.read()
        # decode detected barcodes & get the image
        # that is drawn
        decoded_objects = decode(frame)
        # show the image in the window
        cv2.imshow("frame", frame)
        end = time.time()
        if cv2.waitKey(1) == ord("q"):
            break
        elif (end - start) > 10: # ten second timeout
            break

