import numpy as np
import matplotlib.pyplot as plt
plt.close('all')


from twodphaseret import TwoDPhaseRet


def test_solution():
    ### Test Solution
    x = TwoDPhaseRet( 64, 128, 'd')

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


def test_idempotence():

    ### Test Idempotence
    x = TwoDPhaseRet( 64, 128, 's')

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



if __name__ == "__main__":



    # test_solution()
    test_idempotence()


    plt.show()




