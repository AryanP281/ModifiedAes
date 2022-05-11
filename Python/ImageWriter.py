
import cv2
import numpy as np

def generatePixelFile(imgName) :
    img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    pixels = np.array(img)
    cv2.imshow("Input Image",pixels)
    cv2.waitKey(0)

    print(pixels.size)

    np.savetxt("../pixelVals.txt", pixels, fmt="%d", newline=" ")



def displayOutput(imgName) :
    img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
    pixels = np.array(img)
    cv2.imshow("Input Image",pixels)
    cv2.waitKey(0)

    encryptedPixels = np.loadtxt("../encrypted.txt", dtype=np.int8)
    encryptedPixels = encryptedPixels.reshape((256,256))
    cv2.imshow("Encrypted Image",encryptedPixels)
    cv2.waitKey(0)

    decryptedPixels = np.loadtxt("../decrypted.txt", dtype=np.uint8)
    decryptedPixels = decryptedPixels.reshape((256,256))
    cv2.imshow("Decrypted Image",decryptedPixels)
    cv2.waitKey(0)

#generatePixelFile("img.png")
displayOutput("img.png")