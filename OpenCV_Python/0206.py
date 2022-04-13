# 서브플롯에 영상 표시
import cv2
import matplotlib.pyplot as plt

path = './data/'
BGRimg1 = cv2.imread(path + 'lena.jpg')
BGRimg2 = cv2.imread(path + 'apple.jpg')
BGRimg3 = cv2.imread(path + 'baboon.jpg')
BGRimg4 = cv2.imread(path + 'orange.jpg')

RGBimg1 = cv2.cvtColor(BGRimg1, cv2.COLOR_BGR2RGB)
RGBimg2 = cv2.cvtColor(BGRimg2, cv2.COLOR_BGR2RGB)
RGBimg3 = cv2.cvtColor(BGRimg3, cv2.COLOR_BGR2RGB)
RGBimg4 = cv2.cvtColor(BGRimg4, cv2.COLOR_BGR2RGB)

fig = plt.figure(figsize=(10, 10))
fig.canvas.manager.set_window_title('Sample Pictures')

plt.subplot(221)
plt.imshow(RGBimg1, aspect = 'auto')
plt.axis('off')

plt.subplot(222)
plt.imshow(RGBimg2, aspect = 'auto')
plt.axis('off')

plt.subplot(223)
plt.imshow(RGBimg3, aspect = 'auto')
plt.axis('off')

plt.subplot(224)
plt.imshow(RGBimg4, aspect = 'auto')
plt.axis('off')

plt.subplots_adjust(left=0, right=1, bottom=0, top=1,
                    wspace=0.05, hspace=0.05)
plt.savefig('./data/0206_four_figures.jpg')
plt.show()