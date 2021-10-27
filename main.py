
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from twodphaseret import TwoDPhaseRet








if __name__ == "__main__":
    x = TwoDPhaseRet()



    plt.figure()
    plt.title('Object')
    plt.imshow(x.obj_arr)

    plt.figure()
    plt.title('Support')
    plt.imshow(x.supp_arr)


    psi = x.fft(x.obj_arr)
    inten = np.abs(psi)**2

    plt.figure()
    plt.imshow(np.log10(inten+1))


    rho = x.ifft(psi).real



    plt.figure()
    plt.title('rho')
    plt.imshow(rho)





    plt.show()


