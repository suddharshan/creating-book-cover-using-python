import csv
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
with open('books.csv',encoding='utf-8') as csv_file:
    data = [row for row in csv.reader(csv_file)]
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("              BOOK COVER MAKER                    ")
print("--------------------------------------------------")
x=range(10)
for i in x:
    bookname=(data[i][0])
    author=(data[i][1])
    print("booknumer=%d"%i)
    print("label=%s"%bookname)
    k=(i%9)
    j=str(k)
    a=len(bookname)
    d=len(author)
    b=bookname.split()
    e=author.split()
    c=len(b)
    f=len(e)
    print("No.of words in book name=%d"%(c))
    print("No.of characters in book name=%d"%a)
    print("No.of words in author=%d"%(f))
    print("No.of characters in author=%d"%(d))
    if(c==1):
        if(a<=8):
            img=Image.open(j+'.png')
            font=ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1=ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw=ImageDraw.Draw(img)
            draw.text((500,900),bookname,(255,255,255),font=font)
            draw.text((600,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        if(8<a<=17):
            img=Image.open(j+'.png')
            font=ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1=ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw=ImageDraw.Draw(img)
            draw.text((180,900),bookname,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
    if(c==2):
        if(a<=8):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            draw.text((500,900),bookname,(255,255,255),font=font)
            draw.text((600,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        if(8<a<=17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            draw.text((200,900),bookname,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
    if(c==3):
        if(8<a<=17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            draw.text((200,900),bookname,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        else:
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            ab=b[0]+" "+b[1]
            bc=b[2]
            draw.text((250,900),ab,(255,255,255),font=font)
            draw.text((350,1050),bc,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
    if(c==4):
        if(8<a<=17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            draw.text((200,900),bookname,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        else:
            img= Image.open("3.png")  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            ab=b[0]+" "+b[1]
            bc=b[2]+" "+b[3]
            draw.text((250,900),ab,(255,255,255),font=font)
            draw.text((250,1050),bc,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
    if(c==5):
        ab=b[0]+" "+b[1]+" "+b[2]
        bc=b[2]+" "+b[3]+" "+b[4]
        if(8<a<=17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            draw.text((250,900),bookname,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        elif(len(ab)<=17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            ab=b[0]+" "+b[1]+" "+b[2]
            bc=b[3]+" "+b[4]
            draw.text((180,900),ab,(255,255,255),font=font)
            draw.text((250,1050),bc,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        elif(len(ab)>17 and len(bc)<=17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            ab=b[0]+" "+b[1]
            bc=b[2]+" "+b[3]+" "+b[4]
            draw.text((250,900),ab,(255,255,255),font=font)
            draw.text((200,1050),bc,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        else:
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            ab=b[0]+" "+b[1]
            bc=b[2]+" "+b[3]
            cd=b[4]
            draw.text((250,900),ab,(255,255,255),font=font)
            draw.text((250,1050),bc,(255,255,255),font=font)
            draw.text((280,1200),cd,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
    if(c==6):
        ab=b[0]+" "+b[1]+" "+b[2]
        bc=b[3]+" "+b[4]+" "+b[5]
        if(8<a<=17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            draw.text((250,900),bookname,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        elif(len(ab)<17 and len(bc)<17):
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            ab=b[0]+" "+b[1]+" "+b[2]
            bc=b[3]+" "+b[4]+" "+b[5]
            draw.text((200,900),ab,(255,255,255),font=font)
            draw.text((200,1050),bc,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
        else:
            img= Image.open(j+'.png')  
            font = ImageFont.truetype('aleo-bold-webfont.ttf',150,encoding="utf-8")
            font1 = ImageFont.truetype('aleo-bold-webfont.ttf',110,encoding="utf-8")
            draw = ImageDraw.Draw(img)
            ab=b[0]+" "+b[1]
            bc=b[2]+" "+b[3]
            cd=b[4]+" "+b[5]
            draw.text((225,900),ab,(255,255,255),font=font)
            draw.text((225,1050),bc,(255,255,255),font=font)
            draw.text((225,1200),cd,(255,255,255),font=font)
            draw.text((400,2090),author,(255,255,255),font=font1)
            img.save(bookname+'.png')
    print("book cover saved as %s.png"%bookname)
    print("**************************************************************************")
    print("**************************************************************************")
        
        
