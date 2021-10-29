import numpy as np



class SchemesMixin:




    def ER(self, rho_in=None):

        if rho_in is not None:
            pm_out = self.Pm(rho_in)
            rho_out = self.Ps(pm_out)
            return rho_out
        else:
            self.iter_rho_arr = self.Pm(self.iter_rho_arr)
            self.iter_rho_arr = self.Ps(self.iter_rho_arr)




    def HIO(self, beta=0.99, rho_in=None):
        if rho_in is not None:
            pm_out = self.Pm(rho_in)
            rho_out = self.Ps(pm_out)
            rho_out[self.supp_notloc] = rho_in[self.supp_notloc] - beta*pm_out[self.supp_notloc]
            return rho_out
        else:
            rho_in = np.copy(self.iter_rho_arr)
            pm_out = self.Pm(rho_in)
            self.iter_rho_arr = self.Ps(pm_out)
            self.iter_rho_arr[self.supp_notloc] = rho_in[self.supp_notloc] - beta*pm_out[self.supp_notloc]





    def DM(self, beta=0.5, gamma_m=-1/0.5,  gamma_s=1/0.5, rho_in=None):


        if rho_in is not None:

            p1 = self.Rm(rho_in, gamma_m)
            p1 = self.Ps(p1)

            p2 = self.Rs(rho_in, gamma_s)
            p2 = self.Pm(p2)

            rho_out = rho_in + beta*(p1-p2)
            return rho_out


        else:
            rho_in = np.copy(self.iter_rho_arr)
            p1 = self.Rm(self.iter_rho_arr, gamma_m)
            p1 = self.Ps(p1)

            p2 = self.Rs(self.iter_rho_arr, gamma_s)
            p2 = self.Pm(p2)

            self.iter_rho_arr = rho_in + beta*(p1-p2)



    def RAAR(self, beta=0.5, gamma_m=1, gamma_s=1, rho_in=None):
        if rho_in is not None:

            p1 = self.Rm(rho_in, gamma_m)
            p1 = self.Rs(p1, gamma_s)
            p1 += rho_in
            p1 *= beta/2

            p2 = (1-beta)*self.Pm(rho_in)

            rho_out = p1 + p2

            return rho_out

        else:
            rho_in = np.copy(self.iter_rho_arr)

            p1 = self.Rm(rho_in, gamma_m)
            p1 = self.Rs(p1, gamma_s)
            p1 += rho_in
            p1 *= beta/2

            p2 = (1-beta)*self.Pm(rho_in)

            self.iter_rho_arr = p1 + p2





















