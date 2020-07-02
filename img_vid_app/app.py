'''
This is a simple python based program for video and photo editing, coded just to revisit the basics of image processing and python and oops.
Using the simple idea of video playing at different speeds gives slo mo and fast mo videos, this command line app was developed.
Idea: Find the current frame rate and increase it by mutlitple of 1.5x. For now it is a random frame rate will be modified in further updates.
There are two folders input and output where each of them have photos and video inputs. 
The program takes all the contents of the folders and does the relevant processing and output in corresponding output video and photo subfolders.

'''

#import the required packages.
import cv2
import sys
import getopt
import os


#class for video related programs.
class Video:
	def __init__(self):
		print("\t\t*********************")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t** VIDEO PROCESSING**")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t*********************")
	
	def fast_mo(self,name):
		cap_name=(os.path.join("input/video/",name))
		video = cv2.VideoCapture(cap_name)
		frame_width = int(video.get(3)) 
		frame_height = int(video.get(4)) 
		size = (frame_width, frame_height) 
		name="output/video/fastmo_"+name+'.avi'
		fourcc = cv2.cv.VideoWriter_fourcc(*'MJPG')
		result = cv2.VideoWriter(name,fourcc,60, size) 
		while(True): 
			ret, frame = video.read() 
			if ret == True:  
				result.write(frame) 
			else:
				break
		print("FastMo Done Sucessfully\n")

	def slow_mo(self,name):
		cap_name=(os.path.join("input/video/",name))
		video = cv2.VideoCapture(cap_name)
		frame_width = int(video.get(3)) 
		frame_height = int(video.get(4)) 
		size = (frame_width, frame_height) 
		name="output/video/slomo_"+name+'.avi'
		fourcc = cv2.cv.VideoWriter_fourcc(*'MJPG')
		result = cv2.VideoWriter(name,fourcc,10, size) 
		while(True): 
			ret, frame = video.read() 
			if ret == True:  
				result.write(frame) 
			else:
				break
		print("Slomo Done Sucessfully")
	


	
#class for photo related programs.
class Photo:
	def __init__(self):

		print("\t\t*********************")
		print("\t\t*********************")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t** PHOTO PROCESSING**")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t**                 **")
		print("\t\t*********************")
		print("\t\t*********************")

# code for processing the image goes here.
	def process_image(self,name): # Image read from name and process basic.
		image=cv2.imread(name)
		return image

	def black_white(self,name):
		image=self.process_image(os.path.join("input/photo",name))
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		name="output/photo/blk_wht_"+name
		cv2.imwrite(name,gray)
		
	def silhoute(self,name):
		image=self.process_image(os.path.join("input/photo",name))
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gray = cv2.medianBlur(gray, 3) 
		gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		name="output/photo/silhoute_"+name
		cv2.imwrite(name,gray)
		
		
		
	def pencil_sketch(self,name):
		image=self.process_image(os.path.join("input/photo",name))
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)	
		inverted=255-gray
		inverted=cv2.blur(inverted,(5,5))
		name="output/photo/pencil_"+name
		cv2.imwrite(name,inverted)
	
	def blur(self,name):
		image=self.process_image(os.path.join("input/photo",name))
		blur = cv2.blur(image,(5,5))
		name="output/photo/blur_"+name
		cv2.imwrite(name,blur)
		


def default():
	print("Please follow the instructions correctly and enter try again")

def photo_menu():
	print("Available options:")
	print("1.Get black and white photo.\n")
	print("2. Get pencil sketch photo\n")
	print("3. Get a blured photo\n")
	print("4. Get the silhoute of the photo\n")
	print("5. Sharp the photo.\n")
	choice=input("Enter the choice.\n")
	return choice
	
def video_menu():	
	print("Available options:")
	print("1. Get SLO-MO video\n")	
	print("2. Get FAS-MO video\n")	
	choice=input("Enter the choice.\n")
	return choice



def main():
	print("The following options are available for the multimedia\n")
	choice=input("Enter the choice\n   0.To exit \n   1.Photo \n   2.Video\n")
	while choice !=0:
		if choice==1:
			c=photo_menu()	
			a=Photo()
			for each_photo in os.listdir("./input/photo"):
				print(each_photo)
				print(c)
				if c==1:
					a.black_white(each_photo)
				elif c==2:
					a.pencil_sketch(each_photo)
				elif c==3:
					a.blur(each_photo)
				elif c==4:
					a.silhoute(each_photo)
				elif c==5:
					a.sharp(each_photo)
				else :	
					print("Enter a valid choice")
		elif choice==2:
			c=video_menu()	
			v=Video()
			for each_video in os.listdir("./input/video"):
				print(each_video)
				if c==1:
					v.slow_mo(each_video)
				else:
					v.fast_mo(each_video)	
		else:
			default()
		choice=input("Enter the choice\n   0.To exit \n   1.Photo \n   2.Video\n")
		os.system('clear')	

if __name__=="__main__":		
	os.system('clear')
	print("Hello welcome to multimedia app\n")
	main()

