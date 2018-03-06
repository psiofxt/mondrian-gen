# stdlib
from os import listdir, getcwd
from os.path import isfile, join

# third-party
from skimage.measure import compare_ssim as ssim
import cv2



def calculate_structural_sim():
    """
    Function responsible for calculating the structural similarity between
    the two images. Similarity is calculated with color then similarity is
    calculated with grayscale images.

    return: average_color, average_gray: averages of similarities of all base
                                         Mondrian images, float
    """
    test_image = cv2.imread('img/test.jpg')
    test_image = cv2.resize(test_image, (600, 1200))
    gray_test_image = cv2.imread('img/test.jpg')
    gray_test_image = cv2.resize(gray_test_image, (600, 1200))
    gray_test_image = cv2.cvtColor(gray_test_image, cv2.COLOR_BGR2GRAY)

    base_files = [f for f in listdir(getcwd() + '/img') \
                    if isfile(join(getcwd() + '/img', f)) and \
                    f[:4] == 'base']

    similarities_color = []
    similarities_gray = []
    for base in base_files:
        base_image = cv2.imread('img/' + base)
        base_image = cv2.resize(base_image, (600, 1200))
        similarity = ssim(test_image, base_image, multichannel=True)
        similarities_color.append(similarity)

        base_image_gray = cv2.imread('img/' + base)
        base_image_gray = cv2.resize(base_image_gray, (600, 1200))
        base_image_gray = cv2.cvtColor(base_image_gray, cv2.COLOR_BGR2GRAY)
        similarity = ssim(gray_test_image, base_image_gray)
        similarities_gray.append(similarity)

    average_color = sum(similarities_color) / len(similarities_color)
    average_gray = sum(similarities_gray) / len(similarities_gray)
    return (average_color, average_gray)
