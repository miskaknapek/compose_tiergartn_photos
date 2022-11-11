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