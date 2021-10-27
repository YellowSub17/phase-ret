
import numpy as np

import matplotlib.pyplot as plt

import cairo as pyc





class TwoDPhaseRet:



    def __init__(self):

        self.obj_pix = 256
        self.img_pix = 1024

        self.obj_bb = ( int((self.img_pix-self.obj_pix)/2), int((self.img_pix+self.obj_pix)/2) )

        ## set up support constraint array
        self.supp_arr = np.zeros( (self.img_pix, self.img_pix))
        self.supp_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = 1

        self.obj_arr = np.zeros( (self.img_pix, self.img_pix))
        self.obj_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = self.make_data('&')

        self.dat_arr = np.abs( self.fft(self.obj_arr))**2

        self.ite_arr  = np.random.random((img_pix, img_pix))



    def Pm(self):
        









    def make_data(self, letter):
        surf = pyc.ImageSurface(pyc.FORMAT_ARGB32, self.obj_pix, self.obj_pix)
        ctx = pyc.Context(surf)
        ctx.scale(self.obj_pix, self.obj_pix)
        ctx.set_font_face(pyc.ToyFontFace('Monospace'))
        ctx.set_font_size(0.9)
        (x, y, width, height, dx, dy) = ctx.text_extents(f'{letter}')
        ctx.move_to(0.25 , 0.75)
        ctx.show_text(f'{letter}')

        letter_array = np.ndarray( shape=(self.obj_pix, self.obj_pix),
                                dtype=np.uint32, buffer = surf.get_data())
        letter_array[np.where(letter_array >0)] = 1

        return letter_array




    def fft(self,x):
        z = np.fft.fftshift(np.fft.fft2(x))
        return z

    def ifft(self,z):
        x = np.fft.ifft2(np.fft.fftshift(z))
        return x








