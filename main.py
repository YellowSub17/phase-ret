
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from twodphaseret import TwoDPhaseRet








if __name__ == "__main__":


    x = TwoDPhaseRet(obj_pix = 64, img_pix = 128, letter='A')
    plt.figure()
    plt.imshow(x.iter_rho_arr)


    x.ER()
    plt.figure()
    plt.imshow(x.iter_rho_arr)

    x.ER()
    plt.figure()
    plt.imshow(x.iter_rho_arr)

    for i in range(200):
        print(i)

        for j in range(100):
            x.ER()
        for j in range(100):
            x.HIO()

        if i%20==9:
            plt.figure()
            plt.imshow(x.iter_rho_arr)








    # for i in range(500):
        # print(i, 'ER')
        # x.ER()

        # if i%100 ==99:
            # plt.figure()
            # plt.imshow(x.iter_rho_arr)
            # plt.title(f'ER: {i}')
            # plt.colorbar()




    # for i in range(250):
        # print(i, 'HIO')
        # x.HIO()

        # if i%100 ==99:
            # plt.figure()
            # plt.imshow(x.iter_rho_arr)
            # plt.title(f'HIO: {i}')





    # plt.figure()
    # plt.title('Object')
    # plt.imshow(x.obj_arr)

    # plt.figure()
    # plt.title('Support')
    # plt.imshow(x.supp_arr)


    # psi = x.fft(x.obj_arr)
    # inten = np.abs(psi)**2

    # plt.figure()
    # plt.imshow(np.log10(inten+1))


    # rho = x.ifft(psi).real



    # plt.figure()
    # plt.title('rho')
    # plt.imshow(rho)





    plt.show()


