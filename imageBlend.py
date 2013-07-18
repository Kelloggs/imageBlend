import Image
import sys
import os

def usage():
	print "******************************************************************************"
	print "Usage:"
	print "python imageBlend pathDirectoryA pathDirectoryB splitLine bandWidth"
	print "______________________________________________________________________________"
	print "pathDirectoryA  path to the directory containing the left hand side images"
	print "pathDirectoryB  path to the directory containing the right hand side images"
	print "splitLine       integer x value of the transition center (in pixels)"
	print "bandWidth       integer value for the width of the transition band (in pixels)"
	print ""
	print "The number of files in pathDirectoryA has to match pathDirectoryB"
	print "The directories must only contain image files (png, jpg)"
	print "******************************************************************************"

#get parameters and check correct usage of script	
try:
	directoryA = sys.argv[1]
	directoryB = sys.argv[2]
	middle = int(sys.argv[3]) 
	kernelsize = int(int(sys.argv[4])/2.0)

	filesA = os.listdir(directoryA)
	filesB = os.listdir(directoryB)
except:
	usage()
	sys.exit(1)

#file numbers must match
if len(filesA) != len(filesB):
	print "ERROR: Different number of files in directories"
	usage()
	sys.exit(1)

count = 0
for fileA, fileB in zip(filesA, filesB):
	imA = Image.open(directoryA + "/" + fileA)
	imB = Image.open(directoryB + "/" + fileB)

	#compare image sizes
	if imA.size != imB.size:
		print "ERROR: Image sizes do not match for files " + fileA + " and " + fileB
		usage()
		sys.exit(1)

	#compute alpha blending for transition band
	for x in range(middle - kernelsize, middle + kernelsize + 1):
		for y in range(imA.size[1]):
			val = x - middle + kernelsize
			alpha = val/(2.0 * kernelsize)
			colorA = tuple([int((1.0 - alpha)*mbA) for mbA in imA.getpixel((x,y))])
			colorB = tuple([int(alpha*mbB) for mbB in imB.getpixel((x,y))])
			resultColor = tuple(colA + colB for colA, colB in zip(colorA, colorB))
			imA.putpixel((x,y), resultColor)

	#finally, paste left hand side of transition band from imB to imA
	box_left = (0,0,middle + kernelsize, imA.size[1])
	left_part = imA.crop(box_left)
	result = imB.copy()
	result.paste(left_part, box_left)

	#save and output progress
	result.save("new_" + str(count) + ".png")
	print "Created new_" + str(count) + ".png"
	count += 1

#that's it
print "Finished blending " + str(count) + " files"

