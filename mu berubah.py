"""
Aliran Poiseuille: Explicit 
B_ 22.05.22
"""
import matplotlib.pyplot as plt
import numpy as np

# Deklarasi Variabel
h = 1;               # Lebar Celah
N = 20;              # Jumlah Grid
dy = h/N;            # space step
dt = 0.001;          # time step
mu = np.ones(N);              # Kekentalan

u = np.zeros([N]);   # Kecepatan Awal (di set NOL)
G = 1;

# Syarat Batas (Boundary Condition, B.C.)
u[-1] = 0;     # Kecepatan Permukaan
u[0] = 0;      # Kecepatan Dasar

# # PLOT
plt.plot(u,range(1,N+1),'-',linewidth=2.0)

tol = 1e-5;
err = 1;
nn = 1;
while (err > tol):
    # Update Kecepatan
    # Cara-1: Pengulangan
    for ni in range(1,N-1):
        u_old = np.copy(u);
        u[ni] = u_old[ni] + G*dt + ((mu[ni]-mu[ni-1])/dy)*(u_old[ni+1] - 2*u_old[ni] + u_old[ni-1]);

    # Plot setiap NLoops/5 (supaya tidak terlalu banyak yg di plot)
    if (nn % 100 == 0):
        plt.plot(u,range(1,N+1),'-',linewidth=2.0)
    
    # Hitung Perubahan Kecepatan Sebelum dan Sesudah
    err = np.abs(np.sum(u-u_old));
    
    nn = nn + 1; # Update Indeks Kecepatan

plt.xlabel('u(y)', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.savefig('filePlot.png')

plt.show()
