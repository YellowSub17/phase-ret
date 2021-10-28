
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from twodphaseret import TwoDPhaseRet








if __name__ == "__main__":


    x = TwoDPhaseRet(obj_pix = 100, img_pix = 220, letter='%', perfect_supp=False)

    plt.figure()
    plt.imshow(x.obj_arr)
    plt.title('Target')


    plt.figure()
    plt.imshow(np.log10(x.dat_arr+1))
    plt.title('Measured Data')

    plt.figure()
    plt.imshow(x.supp_arr)
    plt.title('Inital Support')




    # plt.figure()
    # plt.imshow(np.abs(x.iter_rho_arr))
    # x.ER()
    # plt.figure()
    # plt.imshow(np.abs(x.iter_rho_arr))



    # for j in range(40):
        # x.DM()

        # if j%10==9:
            # x.shrinkwrap()

    # plt.figure()
    # plt.imshow(np.abs(x.iter_rho_arr))







    for _ in range(400):
        x.HIO(beta=0.99)
    for _ in range(100):
        x.ER()

    x.shrinkwrap()

    for i in range(10):
        for _ in range(400):
            x.HIO(beta=0.1)

        # plt.figure()
        # plt.imshow(x.iter_rho_arr)
        # plt.title(f'hio {i}')

        for _ in range(400):
            x.ER()

        # plt.figure()
        # plt.imshow(x.iter_rho_arr)
        # plt.title(f'ER {i}')
        x.shrinkwrap()
        print(i, end='\r')











    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('Final Rho')

    plt.figure()
    plt.imshow(x.supp_arr)
    plt.title('Final Support')










    plt.show()


