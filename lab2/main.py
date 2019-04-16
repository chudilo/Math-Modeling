import math
import pprint

tableI = ([0.5, 6400, 0.4],
                [1.0, 6790, 0.55],
                [5.0, 7150, 1.7],
                [10.0, 7270, 3],
                [50.0, 8010, 11],
                [200.0, 9185, 32],
                [400.0, 10010, 40],
                [800.0, 11140, 41],
                [1200.0, 12010, 39])


def linInterpol(I, tbl, index=1):
        if I < tbl[0][0]:
                return tbl[0][index]
        elif I > tbl[len(tbl)-1][0]:
                return tbl[len(tbl)-1][index]
        else:
                for i in range(len(tbl)-1):
                        if tbl[i][0] < I <= tbl[i+1][0]:
                                return tbl[i][index] + \
        (tbl[i+1][index] - tbl[i][index])/(tbl[i+1][0] - tbl[i][0])*(I - tbl[i][0])


tableSigm = ([4000,  0.031],
                [5000, 0.27],
                [6000, 2.05],
                [7000, 6.06],
                [8000, 12],
                [9000, 19.9],
                [10000, 29.6],
                [11000, 41.1],
                [12000, 54.1],
                [13000, 67.7],
                [14000, 81.5])


def logInterpol(T, tbl, index=1):
    if T < tbl[0][0]:
        return tbl[0][index]
    elif T > tbl[len(tbl)-1][0]:
        return tbl[len(tbl)-1][index]
    else:
        for i in range(len(tbl)-1):
                if tbl[i][0] < T <= tbl[i+1][0]:
                        print(tbl[i][0], tbl[i+1][0], tbl[i][index], tbl[i+1][index], T)
                        return math.exp(math.log(tbl[i][index]) +\
(math.log(tbl[i+1][index]) - math.log(tbl[i][index]))*(T - tbl[i][0])/(tbl[i+1][0] - tbl[i][0]))


# calculating an integral by Simpson's method
def simpsonIntegr(a, b, func, stepcnt=41):
	if(stepcnt and stepcnt%2 == 1):
		step = (b-a)/(stepcnt-1)
		ret = func(a) + func(b)

		for i in range(1, stepcnt-1):
			a += step
			if i%2 == 1:
				ret += 4*func(a)
			else:
				ret += 2*func(a)

		return ret*step/3


def integrFunc(x):
	return x*(T0 + (Tw - T0)*x**n)




def getR(I):
    l_e = 12 #sm
    R = 0.35 #sm
    #sigm
    return l_e/(2*math.pi*R*R)


def gU(I):
    C_k = 150e-6
    return -I/C_k


def dI(I, U_c):
    R_k = 0.2
    L_k = 60e-6
    R_p = getR(I)
    return (U_c - I*(R_k - R_p))/L_k


def difRungeKutta(dt, I_n, U_n):

    m1 =
    U_n1 = U_n + dt*(m1 + 2*m2 + 2*m3 + m4)/6
    #I_n+1 = return I_n + dt*(k1 + 2*k2 + 2*k3 + k4)/6
    #U_n+1 = U_n + dt*(m1 + 2*m2 + 2*m3 + m4)/6
    pass
    return None, None

if __name__ == "__main__":
	#print(simpsonIntegr(0, 5, my_func))
	#print(linInterpol(7, tableI, 1))
    #print(logInterpol(13950, tableSigm))

    dt = 1e-03
    step_num = 1000
    I_0 = 0.2
    U_0 = 1500
    R = getR(I_0)

    data = [[0, I_0, U_0, R]]

    for i in range(step_num):
        I, U = difRungeKutta(dt, data[i][1], data[i][2])
        R = getR(I)
        data.append([dt*i, I, U, R])
