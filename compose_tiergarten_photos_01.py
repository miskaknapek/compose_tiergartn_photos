


"""

ideas: ...

- many in the readme. 
- - but basically :
	- composition groups ( ie an GROUP_for_image_composition instance ) describes which images to use in a group how the images are to be processed.
	-- ????? IF A TIME-SPAN IS INDICATED, THEN WHO FIGURES OUT HOW MANY IMAGES FIT IN THE TIME SPANS? ETC? WE NEED A FUNCTION FOR THAT SOMEWHERE? --->>> GROUP HOLDER??? 
	- groups holder : holds the different groups for a composition + some meta data (ie overall image size, scaling, whether to render with real images or do a mockup for rendering …)
	- the precalc engine figures out the varous cut+paste operations and relevant coordinates needed for each image in each group
	- the composition engine does the cut+pasting …and final output 

"""


"""
TO DO ? 
--------

2022.09.28
1_ - how about making an array of image *objects*
-- currently the iage holder only finds relevant images, but not an array of image objects.
-- an array of image objects can help with knowing the sizes of the images, if one 
-- needs to do some sort of overall calculation of images … 

2_- remember that the image object is closed once loaded... otherwise PIL tells me too many images are open at once…


2022.10.03
1. Parsing dates : 
	parsed dates = datetime.datetime.strptime( date, '%Y:%m:%d %H:%M:%S' )

2. parsin exif tages : 
		from PIL import ExifTags

		exifData = {}
		img = Image.open(picture.jpg)
		exifDataRaw = img._getexif()
		for tag, value in exifDataRaw.items():
		    decodedTag = ExifTags.TAGS.get(tag, tag)
		    exifData[decodedTag] = value



"""




"""
imports  --------------------------------------------------
"""

import os
import time


from PIL import Image 



"""
vars  
"""


# variable - osx 
images_url_OSX_1 = "/Users/miska/Desktop/onpeplus_photos_dl"
# old mac 
images_url_OSX_2 = "/Users/miska/Desktop/to_backups/oneplus_5t_since_20211216/favourites/4stars/6stars"
# windwos
images_url_WINDOWS = "/mnt/c/Users/stupi/Pictures/photos_for_health/export5_favourites/6stars"

## and this is what we're using 
curr_file_url = images_url_OSX_2



"""
code?  --------------------------------------------------
"""


"""
------------------ groups composition engine/object  - - - 
- does the cutting+pasting
"""



"""
------------------ groups preprocessor  - - - 
- calculcate operations and coordinates (and outer canvas size?)
"""



"""
------------------ group holder object  - - - 
"""

"""
 ------------------ image composotion group - - - 
- a compositin may have one or more such
- maybe some image selection based on time happens somewhere
- gets fed into the geometric precalc module, to figure out the various coords and operations, before things are fed to the composition engine
"""

class GROUP_for_image_composition:

	# ---------- parameters
	# who am i?
	my_name_is = "my name is GROUP_for_image_composition"

	# --- geometry 

	# do we start where the last image left off
	group_start_COORDS_from_previous_image = False
	# and if not, ie that we set the start coords manually 
	group_start_COORDS__LEFT = 0
	group_start_COORDS__TOP = 0

	# --- TEMP COORDS

	# - maybe these won't be needed, but just in case…
	# - - in any event, these are where the previous image in the loop had its coordinates, set to make it easier for the next loop image to know wheere to go 
	last_image_LEFT = 0
	last_image_RIGHT = 0
	last_image_TOP = 0
	last_image_BOTTOM = 0

	last_image_WIDTH = 0
	last_image_HEIGHT = 0


	# --- out image size


	output_size__SET_WIDTH = "output_size__SET_WIDTH"
	output_size__SET_HEIGHT = "output_size__SET_HEIGHT"
	# - if choosing this, then the code will need some help deciding how to crop the image
	output_size__SET_HEIGHT_AND_HEIGHT = "output_size__SET_HEIGHT_AND_HEIGHT"

	# and what are we using?
	output_size__CURRENT = "output_size__SET_HEIGHT"

	# --- image cropping 

	# MAYBE THIS WILL be apparenty once one asks for a certain aspect ratio of the iamge 
	image_cropping__NONE = "image_cropping__NONE"
	image_cropping__MIDDLE = "image_cropping__MIDDLE"

	# --- 


	# ---- images in this group?
	group_images = []


	# ---------- initialise 

	def __init__( self ):
		print("\n- initialising GROUP_for_image_composition");
		print("\n\t the GROUP holds meta data about how they are to be processed, and the images that are supposed to be in the group, etc ")
		#
		#



		#
		#
		self.run_me()


	# ---------- various functions 

	def run_me( self ):
		print("\n >>> GROUP_for_image_composition : runme() ")
		print("\n\t - my_name_is is : "+str( self.my_name_is ))



# ------- image object holder v 0 


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


# test
sayHello()


# - invalid function as I made the image object do something new… 
# make_test_image_class_and_print_values()


make_imge_objects_of_all_images_in_given_folder( curr_file_url )


# let's try making an array of 
make_image_object_HOLDER__ONE = make_image_object_HOLDER_of_given_url( curr_file_url )



