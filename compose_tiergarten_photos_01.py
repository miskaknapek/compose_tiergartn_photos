

"""
TO DO ? 
--------

2022.09.28
1_ - how about making an array of image *objects*
-- currently the iage holder only finds relevant images, but not an array of image objects.
-- an array of image objects can help with knowing the sizes of the images, if one 
-- needs to do some sort of overall calculation of images … 

2_- remember that the image object is closed once loaded... otherwise PIL tells me too many images are open at once…








"""



"""
importss  --------------------------------------------------
"""

import os
import time


from PIL import Image 

"""
code?  --------------------------------------------------
"""



class Image_object_HOLDER:
	def __init__( self, relev_url ):
		print("\n- initialising Image_object_HOLDER");
		self.url = relev_url
		self.relevant_file_endings = ['png', 'jpg', 'jpeg']
		self.array_of_relevant_iamges = []
		self.array_of_relevant_iamges_OBJECTS = []
		#
		self.run_me()


	def run_me( self ):
		print("\n >>> Image object holder : runme() ")
		print("\t - got url of |"+str( self.url)+"|" )
		#
		self.extract_relevant_images_from_given_url()


	def extract_relevant_images_from_given_url( self ):
		print("\n >>>> extract_relevant_images_from_given_url() - url : |"+str(self.url)+"|")
		
		fl = os.listdir( self.url )
		print("\t - got a file listing of "+str(len(fl))+"files in the given url.\n\t - looking for relevant files ")
		#
		# next step 
		self.return_file_names_with_relevant_file_endings( fl )


	def return_file_names_with_relevant_file_endings( self, inlist ):
		print(">>>> return_file_names_with_relevant_file_endings() ")

		for item in inlist:
			end_of_filename = item.split(".")[-1]
			if end_of_filename in self.relevant_file_endings:
				print("\t\t -- file name |"+str(item)+"| has a relevant file name, adding to outlist of relevant filenames")
				self.array_of_relevant_iamges.append( item )

		print("\t - - - end of file name with relevant filenames filtering.... found "+str( len(self.array_of_relevant_iamges))+" relevant images of "+str( len( inlist ))+" files ")
		#
		self.add_url_path_to_array_of_relevant_images();


	def add_url_path_to_array_of_relevant_images( self ):
		print("\n>>>> add_url_path_to_array_of_relevant_images() - main url : "+str( self.url)+" - got "+str( len(self.array_of_relevant_iamges))+" files ")

		# check if the self.url has a slash at the end 
		if self.url[-1] != "/":
			print("\t - looks like self.lurl is missing a slash at the end. current : |"+self.url+"|")
			self.url = self.url + "/"
			print("\t - new : |"+self.url+"|")

		outlist_of_full_filenames = []

		for item in self.array_of_relevant_iamges:
			outlist_of_full_filenames.append( self.url+item )

		self.array_of_relevant_iamges = outlist_of_full_filenames

		# next step - actually load the images and make image objects of them 
		self.make_image_object_array_of_all_relevant_images()


	def make_image_object_array_of_all_relevant_images( self ):
		print(">>>> make_image_object_array_of_all_relevant_images() - got "+str( len( self.array_of_relevant_iamges ))+" relevant images ")

		starttime = time.time()

		self.array_of_relevant_iamges_OBJECTS = []

		counter_i = 0
		for img_url in self.array_of_relevant_iamges:
			print("-- working on image "+str( counter_i )+"/"+str(len(self.array_of_relevant_iamges)))
			self.array_of_relevant_iamges_OBJECTS.append( Image_object( img_url ) )
			counter_i = counter_i + 1 

		print("\t - and all that image loading took  "+str( time.time() - starttime ))




class Image_object:
	def __init__( self, url ):
		print("\n- initialising Image_object - or url |"+str(url)+"|");
		self.url = url

		self.image_obj = -1 

		self.width = -1
		self.height = -1 

		self.load_image()


	def print_img_values( self ):
		print("url : "+self.url)
		print("width/height : "+str( self.width )+" / "+str( self.height) ) 


	def load_image( self ):
		self.image_obj = Image.open( self.url )

		self.width = self.image_obj.width
		self.height = self.image_obj.height
		# print("\t - - image loaded - with dimensions : "+str( self.width)+"/"+str(self.height) )
		self.print_img_values()

		# CLOSE IMAGE 
		self.image_obj.close()



"""
CHECK THIS - as I made the image object do something more than intended here… 
		- eg load an image, where I put some bad image urls here...

"""
def make_test_image_class_and_print_values():


	# make obj
	new_dummy_class_array = [];

	# fill obj with values #1
	new_img_obj = Image_object();
	new_img_obj.url = "url url url"
	new_img_obj.width = -111
	new_img_obj.height = -222

	# add object to array
	new_dummy_class_array.append( new_img_obj )


	# fill obj with values #2
	new_img_obj = Image_object();
	new_img_obj.url = "url url url 2222222"
	new_img_obj.width = -111222222
	new_img_obj.height = -22222222

	# add object to array
	new_dummy_class_array.append( new_img_obj )



	# ---- print 
	for obj_i in range( len( new_dummy_class_array ) ):
		print( "\n --- printing values of obj #"+str( obj_i ) )
		curr_obj = new_dummy_class_array[ obj_i ]
		curr_obj.print_img_values()



def make_image_object_HOLDER_of_given_url( relev_url ):
	print("\n >>>> make_image_object_HOLDER_of_given_url() of url |"+str()+"| ")

	return Image_object_HOLDER( relev_url )



def make_imge_objects_of_all_images_in_given_folder( folder_path_url ):
	print(">>>> make_imge_objects_of_all_images_in_given_folder() of folder : |"+str( folder_path_url+"|") )

	if folder_path_url[-1] == '/':
		print("\t filename has a dash at the end - do nothing ")
	else:
		print("\t filename HAS NO DASH AT THE END - adding dash ")
		folder_path_url = folder_path_url + '/'

	print("-- reprinting path url : |"+str(folder_path_url)+"|" )





def sayHello():
	print("hellow pythong world")


"""
------------------------------- RUN RUN RUN ---------------------------
"""

# variable 
images_url = "/Users/miska/Desktop/onpeplus_photos_dl"

# test
sayHello()


# - invalid function as I made the image object do something new… 
# make_test_image_class_and_print_values()


make_imge_objects_of_all_images_in_given_folder( images_url )


# let's try making an array of 
make_image_object_HOLDER__ONE = make_image_object_HOLDER_of_given_url( images_url )



