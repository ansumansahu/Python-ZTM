#Exercise :GUI
#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
# print(len(picture[0]))
i=0
for i in range(len(picture[i])-1):
  for j in range(len(picture[i])):
    if picture[i][j]==0:
      print(' ',end=' ')
    else:
      print('*',end=' ')
  i+=1
  print('')

print('')

#preffered solution (which sarcastically is simpler also)
for i in picture:
  for j in i:
    if(j==0):
      print(' ',end=' ')
    else:
      print('*',end=' ')
  print('')


#well mine solution is way too complicated and could have been done better but i'll leave both as is for now .. 
#note: simpler the code better the programmer     
