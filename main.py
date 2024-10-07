
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from twodphaseret import TwoDPhaseRet











if __name__ == "__main__":


    # LIST OF UNICODE letters
    # https://symbl.cc/en/unicode-table://symbl.cc/en/unicode-table/

    # x = TwoDPhaseRet(obj_pix = 200, img_pix = 440, letter='\u0428', perfect_supp=False)
    x = TwoDPhaseRet(obj_pix = 200, img_pix = 440, letter='\u0324', perfect_supp=False)
    # x = TwoDPhaseRet(obj_pix = 200, img_pix = 440, letter='i', perfect_supp=False)
    # x = TwoDPhaseRet(obj_pix = 200, img_pix = 440, letter='cat', perfect_supp=False)



    for _ in range(5):
        for _ in range(25):
            x.ER()

        x.shrinkwrap(thresh_percent=0.5)

    for _ in range(30):
        for _ in range(50):
            x.ER()


    plt.figure()
    plt.imshow(x.supp_arr)
    plt.title('Final Support')

    plt.figure()
    plt.imshow(x.obj_arr)
    plt.title('Target')

    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('Solution')






    plt.show()


