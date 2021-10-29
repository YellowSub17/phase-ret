import numpy as np



class SchemesMixin:


    def ER1(self, ):
        self.iter_rho_arr = self.Pm(self.iter_rho_arr)
        self.iter_rho_arr = self.Ps(self.iter_rho_arr)




    def ER2(self, rho_in):
        pm_out = self.Pm(rho_in)
        rho_out = self.Ps(pm_out)
        return rho_out


    def ER3(self, rho_in=None):

        if rho_in is not None:
            pm_out = self.Pm(rho_in)
            rho_out = self.Ps(pm_out)
            return rho_out
        else:
            self.iter_rho_arr = self.Pm(self.iter_rho_arr)
            self.iter_rho_arr = self.Ps(self.iter_rho_arr)






    # def HIO(self, beta=0.99):

        # rho_pm_in, rho_pm_out = self.Pm(self.iter_rho_arr)
        # rho_pm_in, self.iter_rho_arr = self.Ps(self.iter_rho_arr)

        # self.iter_rho_arr[self.supp_loc] = self.iter_rho_arr[self.supp_loc]
        # self.iter_rho_arr[self.supp_notloc] = rho_pm_in[self.supp_notloc] - beta*self.iter_rho_arr[self.supp_notloc]

    # def DM(self, beta=0.5, gamma_m=-1/0.5,  gamma_s=1/0.5):

        # rho_in = np.copy(self.iter_rho_arr)

        # _, p1 = self.Rm(rho_in, gamma_m)
        # _, p1 = self.Ps(p1)

        # _, p2 = self.Rs(rho_in, gamma_s)
        # _, p2 = self.Pm(p2)


        # self.iter_rho_arr = rho_in + beta * (p1 -p2)



