import numpy as np





class OperatorsMixin:



#     def Rm(self, rho_in,  gamma=1):
        # pm_out = self.Pm(rho_in)
        # rho_out = (1 + gamma)*pm_out - gamma*rho_in
        # return rho_out


    # def Rs(self, rho_in,  gamma=1):
        # ps_out = self.Ps(rho_in)
        # rho_out = (1 + gamma)*ps_out - gamma*rho_in
        # return rho_out


    def Ref_fn(self, rho_in, fn, gamma=1):

        fn_out = fn(rho_in)

        rho_out = (1 + gamma)*fn_out - gamma*rho_in

        return rho_out




    def Pm(self, rho_in):

        psi_arr = self.fft(rho_in)

        psip_arr = np.sqrt(self.dat_arr)*psi_arr/np.abs(psi_arr)

        rho_out = np.abs(self.ifft(psip_arr))

        return rho_out



    def Ps(self, rho_in):

        rho_out = self.supp_arr*rho_in

        return rho_out

