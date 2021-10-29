
import numpy as np

import matplotlib.pyplot as plt

import cairo as pyc


from skimage import io, color, transform, filters

from operators import OperatorsMixin
from schemes import SchemesMixin


class TwoDPhaseRet(OperatorsMixin, SchemesMixin):



    def __init__(self, obj_pix = 64, img_pix = 128, letter='o', perfect_supp=False):

        self.obj_pix = obj_pix
        self.img_pix = img_pix
        self.letter = letter

        ## min and max values for the object bounds
        self.obj_bb = ( int((self.img_pix-self.obj_pix)/2), int((self.img_pix+self.obj_pix)/2) )

        ## create target object
        self.obj_arr = np.zeros( (self.img_pix, self.img_pix))
        if letter=='cat':
            self.obj_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = self.make_cat()
        else:
            self.obj_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = self.make_data(self.letter)

        ## create measured diffraction pattern 
        self.dat_arr = np.abs( self.fft(self.obj_arr))**2

        ## set up support constraint array
        if perfect_supp:
            self.supp_arr = np.copy(self.obj_arr)
            self.supp_arr[np.where(self.supp_arr < 1)] = 0
            self.supp_arr[np.where(self.supp_arr >= 1)] = 1
        else:
            self.supp_arr = np.zeros( (self.img_pix, self.img_pix))
            self.supp_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = 1

        self.supp_loc = np.where(self.supp_arr==1)
        self.supp_notloc = np.where(self.supp_arr==0)

        ## initial random start
        self.iter_rho_arr = np.random.random( (self.img_pix, self.img_pix))




    def shrinkwrap(self, thresh_percent=5):

        thresh = np.max(self.iter_rho_arr)*(thresh_percent/100)

        blurred = filters.gaussian(self.iter_rho_arr)

        blurred_loc = np.where(blurred > thresh)

        self.supp_arr = np.zeros(self.supp_arr.shape)
        self.supp_arr[blurred_loc] = 1

        self.supp_loc = np.where(self.supp_arr==1)
        self.supp_notloc = np.where(self.supp_arr==0)






    def make_data(self, letter):
        surf = pyc.ImageSurface(pyc.FORMAT_ARGB32, self.obj_pix, self.obj_pix)
        ctx = pyc.Context(surf)
        ctx.scale(self.obj_pix, self.obj_pix)
        ctx.set_font_face(pyc.ToyFontFace('Monospace'))
        ctx.set_font_size(0.9)
        (x, y, width, height, dx, dy) = ctx.text_extents(f'{letter}')
        ctx.move_to(0.25 , 0.75)
        ctx.show_text(f'{letter}')

        letter_array = np.ndarray( shape=(self.obj_pix, self.obj_pix), dtype=np.uint32, buffer = surf.get_data())
        letter_array[np.where(letter_array >0)] = 1

        return letter_array


    def make_cat(self):

        image = io.imread('./cat.png')
        x_true = color.rgb2gray(color.rgba2rgb(image))
        x_true = transform.resize(x_true, (self.obj_pix, self.obj_pix))
        x_true /= np.max(x_true)

        return x_true





    def fft(self,x):
        z = np.fft.fftshift(np.fft.fft2(x))
        return z

    def ifft(self,z):
        x = np.fft.ifft2(np.fft.fftshift(z))
        return x








