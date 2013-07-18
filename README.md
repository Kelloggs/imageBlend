imageBlend
==========

Batch script: blends between the images in two folders by doing linear alpha blending on the x axis for a given value x and a bandwidth. 

Example:
--------
You have two folders containing different frames of the same scene (e.g. one final view and a mesh view). You want to blend these two frames in order to come up with a final folder of frames linearly blending between both representations.

```
python imageBlend pathDirectoryA pathDirectoryB splitLine bandWidth
```

splitline denotes the x position, at which the two frames should be blended. bandWith denotes the range on the x axis which should be considered for alpha blending.

Caveats:
--------
- The images in the folders have to be of equal size.
