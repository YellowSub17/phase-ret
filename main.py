
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from twodphaseret import TwoDPhaseRet



import timeit





if __name__ == "__main__":


    x = TwoDPhaseRet(obj_pix = 100, img_pix = 220, letter='y', perfect_supp=False)


    ns = [1, 10, 25, 50, 75, 100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000]

    t1s = []
    t2s = []
    t3s = []
    t4s = []

    for n in ns:
        print(n)

        s1 = f"""

for _ in range({n}):
    x.ER1()

        """
        t1 = timeit.timeit(s1, number=10, globals=globals())
        t1s.append(t1)





        x = TwoDPhaseRet(obj_pix = 100, img_pix = 220, letter='y', perfect_supp=False)

        s2 = f"""

rho_in = np.copy(x.iter_rho_arr)
for _ in range({n}):
    rho_in = x.ER2(rho_in)

        """
        t2 = timeit.timeit(s2, number=10, globals=globals())
        t2s.append(t2)






        x = TwoDPhaseRet(obj_pix = 100, img_pix = 220, letter='y', perfect_supp=False)

        s3 = f"""

for _ in range({n}):
    x.ER3()

        """
        t3 = timeit.timeit(s3, number=10, globals=globals())
        t3s.append(t3)




        x = TwoDPhaseRet(obj_pix = 100, img_pix = 220, letter='y', perfect_supp=False)

        s4 = f"""

rho_in = np.copy(x.iter_rho_arr)
for _ in range({n}):
    rho_in = x.ER3(rho_in)

        """
        t4 = timeit.timeit(s4, number=10, globals=globals())
        t4s.append(t4)

    plt.figure()
    plt.plot(ns, t1s, label='T1')
    plt.plot(ns, t2s, label='T2')
    plt.legend()
    plt.xlabel('N')
    plt.ylabel('t')

    # t1 = timeit.timeit





    # plt.figure()
    # plt.imshow(x.obj_arr)
    # plt.title('Target')


    # plt.figure()
    # plt.imshow(np.log10(x.dat_arr+1))
    # plt.title('Measured Data')

    # plt.figure()
    # plt.imshow(x.supp_arr)
    # plt.title('Inital Support')




    # # plt.figure()
    # # plt.imshow(np.abs(x.iter_rho_arr))
    # # x.ER()
    # # plt.figure()
    # # plt.imshow(np.abs(x.iter_rho_arr))







    # for _ in range(400):
        # x.HIO(beta=0.99)
    # for _ in range(100):
        # x.ER()

    # x.shrinkwrap()

    # for i in range(20):
        # for _ in range(400):
            # x.HIO(beta=0.4)



        # for _ in range(400):
            # x.ER()

        # for _ in range(20):
            # x.DM()



        # x.shrinkwrap()
        # print(i, end='\r')

    # for _ in range(400):
        # x.HIO(beta=0.99)
    # for _ in range(100):
        # x.ER()

    # for i in range(20):
        # for _ in range(400):
            # x.HIO(beta=0.4)



        # for _ in range(400):
            # x.ER()

        # for _ in range(20):
            # x.DM()





















    # # for _ in range(400):
        # # x.HIO(beta=0.99)
    # # for _ in range(100):
        # # x.ER()

    # # x.shrinkwrap()

    # # for i in range(10):
        # # for _ in range(400):
            # # x.HIO(beta=0.4)

        # # # plt.figure()
        # # # plt.imshow(x.iter_rho_arr)
        # # # plt.title(f'hio {i}')

        # # for _ in range(400):
            # # x.ER()

        # # # plt.figure()
        # # # plt.imshow(x.iter_rho_arr)
        # # # plt.title(f'ER {i}')
        # # x.shrinkwrap()
        # # print(i, end='\r')











    # plt.figure()
    # plt.imshow(x.iter_rho_arr)
    # plt.title('Final Rho')

    # plt.figure()
    # plt.imshow(x.supp_arr)
    # plt.title('Final Support')










    plt.show()


