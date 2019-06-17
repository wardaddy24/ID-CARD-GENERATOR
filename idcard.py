from PIL import Image,ImageDraw,ImageFont,ImageOps
from datetime import datetime
import random,os,datetime
import qrcode

#The below code make a template of 1000x900 size of white color over which we will perform printing

image=Image.new('RGB',(800,550),(216,191,216))
draw=ImageDraw.Draw(image)
font=ImageFont.truetype('Verdana.ttf',80)
#image.show()

print("ID GENERATOR BY AMAN RASTOGI")
print("ALL ENTRIES ARE MANDATORY")
print("ENTRIES MUST BE IN PRESCRIBED FORMAT")

#COLLEGE NAME
(x,y)=(70,50)
message=input("\n Enter College Name")
college=message
color='rgb(0,0,0)'
font=ImageFont.truetype('Verdana.ttf',40)
draw.text((x,y),message,fill=color,font=font)

#COLLEGE CITY AND STATE
(x,y)=(300,100)
message=input("\n Enter City of College")
color='rgb(0,0,0)'
state=input("\Enter State of College")
color='rgb(0,0,0)'
font=ImageFont.truetype('Verdana.ttf',20)
draw.text((x,y),message+','+state,fill=color,font=font)

#YOUR NAME
(x,y)=(50,200)
message=input("\n Enter Your Name")
name=message
check="Name: "+message
color='rgb(0,0,0)'
font=ImageFont.truetype('Verdana.ttf',25)
draw.text((x,y),check,fill=color,font=font)

#YOUR BRANCH
(x,y)=(50,250)
message=input("\n Enter Your Branch(CS/IT/ME etc.)")
check="Branch: "+message
color='rgb(0,0,0)'
font=ImageFont.truetype('Verdana.ttf',25)
draw.text((x,y),check,fill=color,font=font)

#GENDER
(x, y) = (50, 300)
message = input('Enter Your Gender:(M/F/Other)')
if message=='M' or message=='F' or message=='m' or message=='Other' or message=='f' or message=='other':
    if message=='M' or message=='m':
        message="MALE"
    elif message=='F' or message=='f':
        message="FEMALE"
    else:
        message="Other"
else:
    print("INVALID ENTRY")
    input("TRY AGAIN")
    exit()
check="Gender: "+str(message)
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y),check, fill=color, font=font)

#AGE
(x, y) = (250, 300)
message = int(input('Enter Your Age: '))
if message <18 or message>65:
    print("ENTER VALID AGE BTW(18-65)")
    input("TRY AGAIN")
    exit()
check="Age: "+str(message)
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), check, fill=color, font=font)

#DOB
(x,y)=(50,350)
message=input('Enter DOB(YYYY/MM/DD)')
try:
    d =datetime.datetime.strptime(message,"%Y/%m/%d").strftime('%Y/%m/%d')
    check="DOB: "+d
except ValueError:
    print("Incorrect Format")
    print("TRY AGAIN")
    exit()
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), check, fill=color, font=font)

#BLOOD GROUP
(x, y) = (50, 400)
message = input('Enter Your Blood Group(O+,A+etc.): ')
l=['O+','O-','A+','A-','B+','B-','AB+','AB-']
if message not in l:
    print("INVALID BLOOD GROUP")
    input("TRY AGAIN")
    exit()
check="Blood Group: "+message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), check, fill=color, font=font)

# Address
(x, y) = (50, 450)
print('Enter Your Address Details: ')
house=input("Enter house number ")
city=input("Enter city name ")
state=input("Enter your state name")
check="Address: "+house
check2="           "+city+","+state
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), check, fill=color, font=font)
draw.text((50,480),check2,fill=color,font=font)




#image saved
image.save(str(name)+'.png')

#qr generator
img=qrcode.make(str(college)+str(name))
img.save(str(name+"id")+'.bmp')

til=Image.open(name+'.png')
im=Image.open(str(name+"id")+'.bmp')
photo=Image.open("amanface.jpg")       # image must be in the same directory or specify full path
til.paste(im.resize((80,80), Image.ANTIALIAS),(700,100))
til.paste(photo.resize((200,200)),(570,200))
til.save(name+'.png')
print('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png')

def add_border(input_image, output_image, border):
    img = Image.open(input_image)
 
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
 
    bimg.save(output_image)
    
add_border(r"C:\Users\Rastogi\AppData\Local\Programs\Python\Python36-32\AMAN RASTOGI.png", output_image=r'C:\Users\Rastogi\AppData\Local\Programs\Python\Python36-32\aman_rastogi.png',border=100)

