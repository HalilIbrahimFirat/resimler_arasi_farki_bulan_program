import cv2
def find_difference(image1_path, image2_path, threshold=30):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray1, gray2)
    _, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    marked_img = img2.copy()
    for contour in contours:
        cv2.drawContours(marked_img, [contour], 0, (0, 0, 255), 2)
    cv2.imshow("Difference", marked_img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
image1_path = "C:/Users/halil/Desktop/otomataodevsoru1/ilk.png"
image2_path = "C:/Users/halil/Desktop/otomataodevsoru1/iki.png"
find_difference(image1_path, image2_path)
