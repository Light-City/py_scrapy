

from pylab import *
img1 = imread('./img/20180727123428244.jpg')
img2 = imread('./img/20180801035408514.jpg')
img3 = imread('./img/20180801053001405.jpg')
img4 = imread('./img/20180803015536407.jpg')



fig = plt.figure()
subplot(221)
imshow(img1)
title('img1')
axis('off')
subplot(222)
imshow(img2)
title('img2')
axis('off')
subplot(223)
imshow(img3)
title('img3')
axis('off')
subplot(224)
imshow(img4)
title('img4')
axis('off')
show()