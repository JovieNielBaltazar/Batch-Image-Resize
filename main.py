import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    img_resized = cv2.resize(img, (100, 100))
    cv2.imshow("hey", img_resized)
    cv2.imwrite(f"resized_{image}", img_resized)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


