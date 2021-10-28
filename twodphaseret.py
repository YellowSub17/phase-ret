
import numpy as np

import matplotlib.pyplot as plt

import cairo as pyc





class TwoDPhaseRet:



    def __init__(self, obj_pix = 64, img_pix = 128, letter='o'):

        self.obj_pix = obj_pix
        self.img_pix = img_pix
        self.letter = letter

        self.obj_bb = ( int((self.img_pix-self.obj_pix)/2), int((self.img_pix+self.obj_pix)/2) )

        ## set up support constraint array
        self.supp_arr = np.zeros( (self.img_pix, self.img_pix))
        self.supp_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = 1

        self.supp_loc = np.where(self.supp_arr==1)
        self.supp_notloc = np.where(self.supp_arr==0)

        self.obj_arr = np.zeros( (self.img_pix, self.img_pix))
        self.obj_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = self.make_data(self.letter)

        self.dat_arr = np.abs( self.fft(self.obj_arr))**2


        self.iter_rho_arr = np.random.random( (self.img_pix, self.img_pix))

        # self.iter_phi_arr = 2*np.pi*np.random.random( (self.img_pix, self.img_pix))
        # self.iter_psi_arr = np.sqrt(self.dat_arr)*np.exp(self.iter_phi_arr*1j)




    def ER(self):
        self.Pm()
        self.Ps()



    def HIO(self, beta=0.45):
        rho_pm_in, rho_pm_out = self.Pm()
        rho_ps_in, rho_ps_out = self.Ps()

        self.iter_rho_arr[self.supp_loc] = self.iter_rho_arr[self.supp_loc]
        self.iter_rho_arr[self.supp_notloc] = rho_pm_in[self.supp_notloc] - beta*rho_ps_out[self.supp_notloc]





    def Pm(self):
        rho_in = np.copy(self.iter_rho_arr)

        self.psi_arr = self.fft(self.iter_rho_arr)

        self.phi_arr = np.angle(self.psi_arr)

        # self.psip_arr = np.sqrt(self.dat_arr)*np.exp(self.phi_arr*1j)
        self.psip_arr = self.dat_arr*np.exp(self.phi_arr*1j)
        # self.psip_arr = (self.psi_arr/np.abs(self.psi_arr)) * self.dat_arr

        self.iter_rho_arr = self.ifft(self.psip_arr).real

        rho_out = np.copy(self.iter_rho_arr)

        return rho_in, rho_out



    def Ps(self):
        rho_in = np.copy(self.iter_rho_arr)

        self.rhop_arr = self.supp_arr*self.iter_rho_arr

        self.iter_rho_arr = np.copy(self.rhop_arr)

        rho_out = np.copy(self.iter_rho_arr)

        return rho_in, rho_out





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








