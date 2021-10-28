
import numpy as np

import matplotlib.pyplot as plt

import cairo as pyc


from skimage import io, color, transform, filters


class TwoDPhaseRet:



    def __init__(self, obj_pix = 64, img_pix = 128, letter='o', perfect_supp=False):

        self.obj_pix = obj_pix
        self.img_pix = img_pix
        self.letter = letter

        self.obj_bb = ( int((self.img_pix-self.obj_pix)/2), int((self.img_pix+self.obj_pix)/2) )

        self.obj_arr = np.zeros( (self.img_pix, self.img_pix))
        if letter=='cat':
            self.obj_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = self.make_cat()
        else:
            self.obj_arr[self.obj_bb[0]:self.obj_bb[1], self.obj_bb[0]:self.obj_bb[1]] = self.make_data(self.letter)

        # self.obj_arr = self.obj_arr*10 +np.random.random(self.obj_arr.shape)

        self.dat_arr = np.abs( self.fft(self.obj_arr))**2


        self.iter_rho_arr = np.random.random( (self.img_pix, self.img_pix))

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




    def ER(self, ):
        _, self.iter_rho_arr = self.Pm(self.iter_rho_arr)
        _, self.iter_rho_arr = self.Ps(self.iter_rho_arr)



    def HIO(self, beta=0.99):

        rho_pm_in, rho_pm_out = self.Pm(self.iter_rho_arr)
        rho_pm_in, self.iter_rho_arr = self.Ps(self.iter_rho_arr)

        self.iter_rho_arr[self.supp_loc] = self.iter_rho_arr[self.supp_loc]
        self.iter_rho_arr[self.supp_notloc] = rho_pm_in[self.supp_notloc] - beta*self.iter_rho_arr[self.supp_notloc]

    def DM(self, beta=0.7, gamma_m=-1/0.7,  gamma_s=1/0.7):

        rho_in = np.copy(self.iter_rho_arr)

        _, p1 = self.Rm(rho_in, gamma_m)
        _, p1 = self.Ps(p1)

        _, p2 = self.Rs(rho_in, gamma_s)
        _, p2 = self.Pm(p2)


        self.iter_rho_arr = rho_in + beta * (p1 -p2)


    def shrinkwrap(self, thresh=0.1):

        blurred = filters.gaussian(self.iter_rho_arr)

        blurred_loc = np.where(blurred > thresh)

        self.supp_arr = np.zeros(self.supp_arr.shape)
        self.supp_arr[blurred_loc] = 1

        self.supp_loc = np.where(self.supp_arr==1)
        self.supp_notloc = np.where(self.supp_arr==0)











    def Rm(self, rho_in,  gamma):

        _, pm_out = self.Pm(rho_in)

        rho_out = (1 + gamma)*pm_out - gamma*rho_in

        return rho_in, rho_out


    def Rs(self, rho_in,  gamma):

        _, ps_out = self.Ps(rho_in)

        rho_out = (1 + gamma)*ps_out - gamma*rho_in

        return rho_in, rho_out





    def Pm(self, rho_in):

        psi_arr = self.fft(rho_in)

        phi_arr = np.angle(psi_arr)
        # phi_arr = np.pi*2*np.random.random( psi_arr.shape)
        # psip_arr = np.sqrt(self.dat_arr)*np.exp(phi_arr*1j)
        psip_arr = np.sqrt(self.dat_arr)*psi_arr/np.abs(psi_arr)


        rho_out = np.abs(self.ifft(psip_arr))

        return rho_in, rho_out



    def Ps(self, rho_in):

        rho_out = self.supp_arr*rho_in

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








