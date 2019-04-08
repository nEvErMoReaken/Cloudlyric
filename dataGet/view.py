from wordcloud import WordCloud
import json
from scipy.misc import imread
import  matplotlib.pyplot as plt
with open(r'C:\Users\admin\PycharmProjects\Cloudlyric\data\dirtydata.json', 'r',encoding='utf-8') as f:
    read_dict = json.load(f)
alice_mask = imread('oook.png')

# 生成一个词云图像
wordcloud = WordCloud(background_color='white',mask=alice_mask,max_words =1000,font_path=r"C:\\Windows\\Fonts\\STFANGSO.ttf",).fit_words(read_dict)
#生成词云（通常字体路径均设置在C:\\Windows\\Fonts\\也可自行下载）
#不加这一句显示口字形乱码  ""报错
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
