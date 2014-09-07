import os, sys, cv2 

base = '/Users/dantone/git-repos/landmarks/original_images/'
for img_path in os.listdir(base):
  print img_path
  if 'surf' in img_path: continue
  if '.jpg' not in img_path.lower(): continue
  
  image = cv2.imread(base+img_path.lower(),1)
  height, width = image.shape[:2]  
  scale = 1000.0 / max(height, width)
  img = cv2.resize(image, (0,0), fx=scale, fy=scale) 

  surf = cv2.SURF(400)
  surf.hessianThreshold = 3000
  kp, des = surf.detectAndCompute(img,None)
  
  #for k in kp:
#		k.pt = (k.pt[0] / scale, k.pt[1] / scale )
#		k.size /= scale
  
  img_path_new = base+img_path.lower()
  print img_path_new
  img_path_new = img_path_new.replace('.jpg','_surf.jpg')
  img_path_org = img_path_new.replace('.jpg','_org.jpg')

  print img_path_new
  img2 = cv2.drawKeypoints(img,kp,None,(255,255,0),4)
  cv2.imwrite(img_path_new,img2)
  cv2.imwrite(img_path_org,img)

  #cv2.imshow('image',img2)
  #cv2.waitKey(10)