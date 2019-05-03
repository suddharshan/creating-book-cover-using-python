#!/usr/bin/env python
# coding: utf-8

# In[31]:


import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
font = ImageFont.truetype('aleo-bold-webfont.ttf',40)
font1 = ImageFont.truetype('aleo-bold-webfont.ttf',30)
img=Image.new("RGBA", (800,600),(120,20,20))
draw = ImageDraw.Draw(img)
draw.text((300,250),"Book label",(255,255,0),font=font)
draw.text((300,320),"Author name",(255,255,0),font=font1)
draw = ImageDraw.Draw(img)
img.save("test.png")


# In[22]:


from PIL import Image, ImageDraw, ImageFont
 
img = Image.new('RGB', (1000, 500), color = (73, 109, 137))
 
d = ImageDraw.Draw(img)
d.text((500,250), "Hello world", fill=(255, 255, 255))
 
img.save('pil_text_font.png')


# In[44]:


import csv
with open('books.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    row = list(csv_reader)
print (row[9])
print(row[1:10])


# In[67]:


import csv

def read_cell(x, y):
    with open('books.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

print (read_cell(0,1)) 


# In[3]:


import csv
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
with open('books.csv',encoding='utf-8') as csv_file:
    data = [row for row in csv.reader(csv_file)]
x=range(2)
for i in x:
    bookname=(data[i][0])
    author=(data[i][1])
    a=len(bookname)
    img= Image.open("1.png")  
    font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
    font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
    draw = ImageDraw.Draw(img)
    draw.text((250,1000),a,(255,255,255),font=font)
    draw.text((400,2090),b,(255,255,255),font=font1)
    img.save(bookname+'.png')
    img


# In[24]:


import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
img= Image.open("1.png")
img


# In[13]:


import csv
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
with open('books.csv',encoding='utf-8') as csv_file:
    data = [row for row in csv.reader(csv_file)]
bookname=(data[1][0])
author=(data[1][1])
a=len(bookname)
b=bookname.split()
c=len(b)
c


# In[ ]:





# In[ ]:




