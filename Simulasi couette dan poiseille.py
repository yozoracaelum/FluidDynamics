"""
Aliran Poiseuille: Explicit 
B_ 22.05.22
"""
import matplotlib.pyplot as plt
import numpy as np

# Deklarasi Variabel
h = 1               # Lebar Celah
N = 20              # Jumlah Grid
dy = h/N            # space step
dt = 0.001          # time step
m0 = 1e-4           # Kekentalan
#mu = m0*dt
mu = 1
d = (mu*dt)/(dy**2) # Konstanta Difusi

u = np.zeros([N])   # Kecepatan Awal (di set NOL)
G = 1

# Syarat Batas (Boundary Condition, B.C.)
u[-1] = 0    # Kecepatan Permukaan
u[0] = 0     # Kecepatan Dasar

# # PLOT
plt.plot(u,range(1,N+1),'*',linewidth=2.0, label='1')
plt.legend()

tol = 1e-5
err = 1
nn = 1
#itval = int(input('Interval: '))
while (err > tol):
    # Update Kecepatan
    # Cara-1: Pengulangan
    '''if nn % itval == 0:
        u[-1] = 2
    else:
        u[-1] = 1'''
    #print(u[-1])
    mu = m0*nn
    d = (mu*dt)/(dy**2)
    for ni in range(1,N-1):
        u_old = np.copy(u)
        u[ni] = u_old[ni] + G*dt + d*(u_old[ni+1] - 2*u_old[ni] + u_old[ni-1])

    # Plot setiap NLoops/5 (supaya tidak terlalu banyak yg di plot)
    if (nn % 10 == 0):
        plt.plot(u,range(1,N+1),'-',linewidth=2.0)
    
    # Hitung Perubahan Kecepatan Sebelum dan Sesudah
    err = np.abs(np.sum(u-u_old))
    
    nn += 1 # Update Indeks Kecepatan
    #print(nn)
    #print(err)
    if nn == 200:
        break
plt.xlabel('u(y)', fontsize=16)
plt.ylabel('y', fontsize=16)
#plt.savefig('filePlot.png')
plt.show()