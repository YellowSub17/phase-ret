
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from twodphaseret import TwoDPhaseRet








if __name__ == "__main__":


    ### Test Solution
    x = TwoDPhaseRet( 64, 128, 's')

    x.iter_rho_arr = np.copy(x.obj_arr)

    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('input')
    plt.colorbar()

    iter_in, iter_out = x.Pm()

    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('output')
    plt.colorbar()




    ### Test Idempotence
    x = TwoDPhaseRet( 64, 128, 'i')


    iter_1, iter_2 = x.Pm()

    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('iter_1')
    plt.colorbar()

    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('iter_2')
    plt.colorbar()

    iter_3, iter_4 = x.Pm()

    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('iter_3')
    plt.colorbar()

    plt.figure()
    plt.imshow(x.iter_rho_arr)
    plt.title('iter_4')
    plt.colorbar()







    



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


