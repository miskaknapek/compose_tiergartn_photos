what's this about?

----------------------------------------------------------

howto : ideas about how the architecture of this code
-------------------


possible outputs : 
------

- very general : consecutive images. one after another. can be in rows. 
(more on this in the ouput parts below) parameters set the distance between photos, cropping, resizing, num of images per row, width of rows, etc… 

- just dump all the input images after one another i given dimensions
- make groups of images from a given time-range
-- ie these groups can either be a group of images (such that they just arrive after the previous images in the collage) or as a row on their own.
--- this raises the question of how to suggest how they enter the collage.


how to handle each image slice
------
- depends on how the image ordering is done?
- what are the variables one can act on the image slices with?


consecutive order and row width/height
------
- also a question here of how the total canvas size is calculated.
-- discussion waiting

- do we set a given number of images per row, or do we let a max row width handle that?
-- again, how to calculate canvas final outsize?
--- set final outsize of canvas manually, or calculate coordinates of slices and then figure out what canvas size would contain that…


grouping (maybe continuing on the above)
------
- consecutive, one by one from an image list ( several image lists could be put together)
- groups of images:
-- of given parameters, eg time ranges, or just a given list of images
-- as a specific number of images, or arbitrary number of images, or maybe the block has a specific width…limit…
-- as just consecutive images after the previous group of images
-- as a whole 'free floating' block (one might need to specify the starting positions though…in which case it's good to have standard slice dimensions, of some sort)


make a cut+paste motor for images?
------
- (could even be on an image object level…)
- rather than have some super super function, do the cut+paste, that's different with each image grouping, etc, just gave each image grouping export relevant image cropping/resizing/paste-position/etc…

- relevant settings : 
-- crop : all or some
--- besides fitting images to standard widths/heights, one could crop images to makes sure all the output slices have the same width/height. But then the cropping function needs to be a bit intelligent, to make sure one, eg., gets the middle of the image rather than just some rectangle starting in the top left corner.

- try 2:
-- cropping mode : 1. whole image? 2. aspect constrained center? 3. 



low resolition output?
------
- how?
- just draw outlines of images, for testing proportions? ( or do altering shades of grey, to give an idea of the composition a bit more than by just drawing outlines)
-- low resolution output calculation?
-- low resolution input?
- - - how, low res input?
- - - - given that reading low resolution pngs could take a bit of time… 


to do
------
- image cropping funciton that gets eg the middle of the image, in a particular aspect ratio…)
- function : find the number of images within a given time range, of different groups of images. give the min/max number of relevant images per group of images.
- function : gather statistics relevant to cropping images for a certain output size or aspect ratio.
-- OR DIFFERENTLY : if you want a given aspect ratio crop of images, some images might require that one doesn't get the whole width/height of an image, but needs to crop it further within, to get the right proportions. MAYBE one could have a function to check what images don't satisfy the aspect ratio cropping, or what the relevant max/mind dimensions are.


rough : SOOOO.... (rough mental sketch)
-----
- to take a quick example of the steps for handling single images when just posting a row of images.
-- make a new array of out image objects
-- for each planned out image : 
--- prepare the coordinates for cropping, resizing, etc… in an object
---- add the relevant image object to the positioning object ( or just the path? ) to the abovementioned object
---- add geometry+path object to the out image objects array
- to get out image : 
( calculate out canvas size, from the various image coordinates… make out canvas of relevant size )
- do the geometry manipulation + paste operation 
- get out image


rough : questions : 
-----
* when to do geometric manipulation?
  * does one indicate on the object when to do it... and calculations are done when copy-pasting? 
    * but then it would be difficult to get the final coords, for figuring out the out canvas size....
    * maaaaybe best to do the coords things at once.
      * BUUUUT .... how does the object know which steps to do? --- make a languge?
      * eg. DEPENDS ON WHAT THE OUT IMAGE THING SHOULD BE ... eg fixed width or height, or fixed height and width....
      * likely, input : crop X aspect ratio, save coords for cropping, paste WIDTH/HEIGHT size, ie save output size. save absolute paste coordinates.



  rough : another rough skecth of how things work : 
  -----

  - basically, at the end, a cut+paste engine will need to paste something at given coordinates. 
  maybe that would be the natural place to start thinking, in regards to what's needed to amke something that works.
  
  - pseudo code for simmple cut+paste: 
  for copy_paste_metadata_item in list_of_copy_paste_metadata_objects:
    load_image()
    copy_relevant_image_region from coords in copy_paste_metadata_item.
    transform()
    paste copied regions into specified outcanvas area in copy_paste_metadata_item

- and what if we take things a bit further, introduce transforamtions?
how introduce transformations?
- do we give the cut+paste function some parsing abilities, to send asks for functions and arguments?
- do we simply run a high level function that does what we want. ie not so much modularity . 

pseudo code for both : 

pseudo code for precalculated coords
  for copy_paste_metadata_item in list_of_copy_paste_metadata_objects:
    load_image()
    if operations.copy_central_region == true:
      - copy given image region
    paste relevant image region to output coords.


pseudo code for some high level functionality in code
  for copy_paste_metadata_item in list_of_copy_paste_metadata_objects:
    load_image()
    for desired_image_operation in copy_paste_metadata_item.list_of_operations:
      // does desired operation and returns the output to relevant persistent variable, so one has access to variables that persist over several operations
      array_of_operation_functions[ desired_image_operation.operation ]( desired_image_operation.arguments )


now, what does pre-processing look like?
-----
- where we establish the coordinates of things to cut+paste?
- ( note, eg if we have different groups/blocks of images that are supposed to make up a cohesive whole, the coords generating function needs to knew where the previous function left off, so it knows where to continue. maybe some persistent object variables can be used for that... or at least some starting poitn variables should be around :)



#### IMPORTANT NOTE : either the coordinates calculation happens in the pre-calculations section, or it happens when the final cutting+pasting is done.
if the coordinate calculations are done in the pre-calculation stage, then the cut+paste stage is basically just copyying image regions from the in-image and pasting them into the out image.


## Random notes : 

- if the output coordinates are precalculated, then scaling images can happen really quite quickly.
could perhaps make cut+paste work a bit quicker.


### Python Image Library reference notes … 
reference : https://pillow.readthedocs.io/en/stable/handbook/tutorial.html 

##### copy
Copying a subrectangle from an image
box = (100, 100, 400, 400)
region = im.crop(box)

##### paste
Processing a subrectangle, and pasting it back
region = region.transpose(Image.Transpose.ROTATE_180)
im.paste(region, box)


##### cutting+pasting image
( *note* the copy/paste regions need to be the same size )

##### resizing image
Simple geometry transforms
out = im.resize((128, 128))
out = im.rotate(45) # degrees counter-clockwise