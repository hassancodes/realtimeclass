import cv2
import glob
def getcordlist(image):
    method = cv2.TM_SQDIFF_NORMED
    small = image
    large = cv2.imread('bg.png')
    result = cv2.matchTemplate(small, large, method)
    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    # Draw the rectangle:
    # Extract the coordinates of our best match
    xaxis,yaxis = mnLoc
    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small.shape[:2]
    # getting the mid point of the rectangle that we just create from the image matched area.
    point = (xaxis+int(tcols/2),yaxis+int(trows/2))
    return point

# function ends here


def getimages():
    path = glob.glob("assets/cordimages/*.png")
    # cv_image will store all the images
    cv_img = []
    for img in path:
        n = cv2.imread(img)
        cv_img.append(n)

    # cordinates for storing the points
    cordinates = []
    for i in cv_img:
        p = getcordlist(i)
        cordinates.append(p)
    large = cv2.imread('bg.png')
    print(cordinates)
    # [(718, 431), (839, 354), (298, 293), (447, 384), (547, 440)]
    for point in cordinates:
        cv2.circle(large,tuple(point),1,(255,0,0), thickness=10)
    cv2.imshow("output",large)
    cv2.waitKey(0)
getimages()
