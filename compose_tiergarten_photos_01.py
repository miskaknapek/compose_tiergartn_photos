
"""
importss  --------------------------------------------------
"""

import os


"""
code?  --------------------------------------------------
"""




class Image_object:
	def __init__( self ):
		print("\n- initialising Image_object");
		self.url = ""

		self.width = -1
		self.height = -1 

	def print_img_values( self ):
		print("url : "+self.url)
		print("width/height : "+str( self.width )+" / "+str( self.height) ) 




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


make_test_image_class_and_print_values()


make_imge_objects_of_all_images_in_given_folder( "/Users/miska/Desktop/onpeplus_photos_dl" )