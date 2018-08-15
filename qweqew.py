
import matplotlib.pyplot as plt
import matplotlib.image as mping
img1 = mping.imread('./img/20180727123428244.jpg')
img2 = mping.imread('./img/20180801035408514.jpg')
img3 = mping.imread('./img/20180801053001405.jpg')
img4 = mping.imread('./img/20180803015536407.jpg')



fig = plt.figure()
plt.subplot(221)
plt.imshow(img1)
plt.title('img1')
plt.axis('off')
plt.subplot(222)
plt.imshow(img2)
plt.title('img2')
plt.axis('off')
plt.subplot(223)
plt.imshow(img3)
plt.title('img3')
plt.axis('off')
plt.subplot(224)
plt.imshow(img4)
plt.title('img4')
plt.axis('off')
plt.show()