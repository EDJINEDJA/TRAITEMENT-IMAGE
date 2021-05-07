#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Convertion de l'image en niveau de gris avec pillow

image=Image.open('LARIS.jpg')
gray_image=image.convert('L')
gray_image_array=np.array(gray_image)

matrice_compte_nombre_niveau_de_gris=list()

def  f_compte_nombre_niveau_de_gris(mat):
    
    compt=0

    while(compt<256):

      matrice_compte_nombre_niveau_de_gris.append(np.count_nonzero(mat == compt))

      compt=compt + 1
    return matrice_compte_nombre_niveau_de_gris

#Soit h l'histogramme et f le niveau de gris de l'image tracons l'histogramme h(f)
compte_nombre_niveau_de_gris=f_compte_nombre_niveau_de_gris(gray_image_array)

#print(compte_nombre_niveau_de_gris)

point_extreme=compte_nombre_niveau_de_gris.index(min(compte_nombre_niveau_de_gris[213:232]))

#print(point_extreme)





iprint=0

if iprint==1:
    X=np.arange(0,256)

    plt.hist(X,weights=compte_nombre_niveau_de_gris,density=True,bins=256,rwidth=0.5)

    plt.title("histograme h(f)",fontsize=10)

    plt.xlabel("Nivau de gris",fontsize=10)

    plt.ylabel("nombre d'occurence",fontsize=10)

    plt.show(block=True)


#Affichaage de l'image

if iprint==1:
   plt.imshow(gray_image_array,cmap='gray', vmin = 0, vmax = 256)
   #plt.imshow(gray_image_array)
   plt.show(block=True)

#Biniaire

def biniaire(mat,point):

    for i in np.arange(0,np.shape(mat)[0]):

        for j in np.arange(0,np.shape(mat)[1]):

            if mat[i,j]<point_extreme:

                mat[i,j]=0
            else:

                mat[i,j]=1
    return mat


iprint = 1


if iprint==1:

    X=np.arange(0,256)

    plt.hist(X,weights=compte_nombre_niveau_de_gris,density=True,bins=256,rwidth=0.5)

    plt.title("histograme h(f)",fontsize=10)

    plt.xlabel("Nivau de gris",fontsize=10)

    plt.ylabel("nombre d'occurence",fontsize=10)

    plt.show(block=True)



if iprint==1:

    image_b=biniaire(gray_image_array,point_extreme)

    plt.imshow(image_b,cmap='gray', vmin = 0, vmax = 1)

    plt.show(block=True)

#Codage algorithme  de contraste


def t_c(a ,b,mat):

    for i in np.arange(0,np.shape(mat)[0]):

        for j in np.arange(0,np.shape(mat)[1]):

            

            if (mat[i,j]<a):

                mat[i,j]=0

            elif (mat[i,j]>b):

                    mat[i,j]=255

            else:

                        mat[i,j]=255* (mat[i,j]-a)/(b-a)
    
    return mat

iprint=0
if iprint==1:

    image_c=t_c(a=np.min(gray_image_array) ,b=np.max(gray_image_array),mat=gray_image_array)




if iprint==1:
    matrice_compte_nombre_niveau_de_gris=list()

    def  f_compte_nombre_niveau_de_gris(mat):
    
        compt=0

        while(compt<256):

           matrice_compte_nombre_niveau_de_gris.append(np.count_nonzero(mat == compt))

           compt=compt + 1
        return matrice_compte_nombre_niveau_de_gris


        
 #Soit h l'histogramme et f le niveau de gris de l'image tracons l'histogramme h(f)
    compte_nombre_niveau_de_gris=f_compte_nombre_niveau_de_gris(image_c)

    X=np.arange(0,256)

    plt.hist(X,weights=compte_nombre_niveau_de_gris,density=True,bins=256,rwidth=0.5)

    plt.title("histograme h(f)",fontsize=10)

    plt.xlabel("Nivau de gris",fontsize=10)

    plt.ylabel("nombre d'occurence",fontsize=10)

    plt.show(block=True)


if iprint==1:
   plt.imshow(image_c,cmap='gray', vmin = 0, vmax = 256)
   plt.show(block=True)




#Codage algorithme de haussement de contraste

def t_h_c(a,b,mat):

    for i in np.arange(0,np.shape(mat)[0]):

        for j in np.arange(0,np.shape(mat)[1]):

            if mat[i,j]>=0 and mat[i,j]<=a :

                mat[i,j]=((b*mat[i,j])/a)

            elif mat[i,j]>=a and mat[i,j]<=255:

                mat[i,j]=((255-b)*mat[i,j]+255*(b-a))/(255-a)

            else:

                mat[i,j]=mat[i,j]
    return mat

iprint=0
if iprint==1:

    image_hc=t_h_c(80,200,gray_image_array)




if iprint==1:
    matrice_compte_nombre_niveau_de_gris=list()

    def  f_compte_nombre_niveau_de_gris(mat):
    
        compt=0

        while(compt<256):

           matrice_compte_nombre_niveau_de_gris.append(np.count_nonzero(mat == compt))

           compt=compt + 1
        return matrice_compte_nombre_niveau_de_gris


        
 #Soit h l'histogramme et f le niveau de gris de l'image tracons l'histogramme h(f)
    compte_nombre_niveau_de_gris=f_compte_nombre_niveau_de_gris(image_hc)

    X=np.arange(0,256)

    plt.hist(X,weights=compte_nombre_niveau_de_gris,density=True,bins=256,rwidth=0.5)

    plt.title("histograme h(f)",fontsize=10)

    plt.xlabel("Nivau de gris",fontsize=10)

    plt.ylabel("nombre d'occurence",fontsize=10)

    plt.show(block=True)


if iprint==1:
   plt.imshow(image_hc,cmap='gray', vmin = 0, vmax = 256)
   plt.show(block=True)
   