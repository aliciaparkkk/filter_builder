#this doc applies 3 filters on an image
import cv2
from filters import apply_warm_filter, apply_pastel_filter, apply_bw_with_grain


# load my image
img = cv2.imread("images/horse.JPG")
if img is None:
    print("Image not found!")
    exit()

# resize for display
img = cv2.resize(img, (600, 600))

# apply warm filter
warm_img = apply_warm_filter(img)
cv2.imshow("Warm Filter", warm_img)
cv2.waitKey(0)

# Apply pastel filter
pastel_img = apply_pastel_filter(img)
cv2.imshow("Pastel Filter", pastel_img)
cv2.waitKey(0)

# Apply BW + grain filter
bw_img = apply_bw_with_grain(img)
cv2.imshow("BW with Grain", bw_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
