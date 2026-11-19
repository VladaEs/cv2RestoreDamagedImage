import cv2
import matplotlib.pyplot as plt
#image


def createMask(image):
    mask = image.copy()
    height, width = mask.shape[0], mask.shape[1]
    for i in range(height):
        for k in range(width):
            if mask[i, k].all() > 0:
                mask[i, k] = 0
            else:
                mask[i, k] = [255, 255, 255]

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.dilate(mask, kernel)
    return mask



    
images_path = ['images/damaged_image1.jpg', 'images/damaged_image2.jpg']
images = []
masks = []
for path in images_path:
    img = cv2.imread(path)
    mask = createMask(img)
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    masks.append(mask)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img)


for i in range(len(images)):
    outputs = []
    output1 = cv2.inpaint(images[i], masks[i], 5, cv2.INPAINT_TELEA)
    output2 = cv2.inpaint(images[i], masks[i], 5, cv2.INPAINT_NS)
    outputs.append(output1)
    outputs.append(output2)

    titles = ['Damaged Image', 'Mask', 'TELEA', 'NS']
    results = [images[i], masks[i], *outputs]
    plt.figure()
    for index in range(4):
        plt.subplot(2, 2, index + 1)
        plt.imshow(results[index], cmap='gray' if index == 1 else None)
        plt.title(titles[index])
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout()

plt.show()

