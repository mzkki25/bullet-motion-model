# Model Gerak Peluru berdasarkan simulasinya menggunakan modul matplotlib dan numpy
# Golf Ball Trajectory Simulation
# Created by Akmal, Namira, and Zaki at 20/10/2022

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
Problem Example
1. Kecepatan awal
2. Sudut elevasi
3. Posisi, ketinggian, dan jarak tempuh horizontal, dicatat setiap 0.1 detik
'''

'''
seorang pemain golf melempar bola golf dengan kecepatan awal V0 m/s dan sudut elevasi @ derajat. 
pemain golf tersebut ingin mengetahui jarak terjauh dan total waktu saat bola mendarat yang dapat dicapai bola 
golf tersebut dengan rincian posisi, ketinggian, dan jarak tempuh horizontal, dicatat setiap 0.1 detik dengan 
asumsi hambatan udara diabaikan, pemain tersebut ingin mensimulasikan pergerakan bola golf dengan menggunakan 
bahasa pemrograman python, dan berikut adalah hasil simulasinya
'''

'''
Rumus yang digunakan untuk gerak parabola
1. tmax = 2*v0*sin@/g (waktu saat benda mendarat)
2. vx = v0*cos@*t atau x = v0*cos@*2*v0*sin@/g = v0^2*sin2@/g (kecepatan arah horizontal)
3. hy = v0*sin@*t - 0.5*g*t^2 (ketinggian atau jarak vertikal)
'''

'''
fungsi yang digunakan
1. projectile_airtime(v0, degree) untuk menghitung waktu saat benda mendarat
2. horizontal_distance(v0, t, degree) untuk menghitung jarak atau jarak terjauh
3. vertical_distance(v0, t, degree) untuk menghitung jarak vertikal atau tinggi
4. update_category(num, lines) untuk menghitung menampilkan pergerakan benda
'''

'''
variabel yang diguanakan
1. v0 = kecepatan awal
2. degree = sudut elevasi
3. g = percepatan gravitasi
4. time_interval = interval waktu
5. horizontal_distances = jarak horizontal
6. vertical_distances = jarak vertikal
7. t = waktu
8. tmax = waktu maksimum
9. v_horizontal = kecepatan horizontal
10. v_vertikal = kecepatan vertikal
11. h = ketinggian
12. radius = sudut elevasi dalam radian
13. time_steps = waktu per langkah
14. h_max = ketinggian maksimum
15. v_max = kecepatan maksimum
16. time_grounds = waktu saat benda mendarat
17. lines = subjek yang akan di animasikan
18. figure = gambar
19. style = model grafik
20. axes = sumbu
'''
g = 9.8

# Fungsi untuk menghitung waktu saat benda mendarat
def projectile_airtime(v0, degree):
    return 2*v0*np.sin(np.radians(degree))/g

# Fungsi untuk menghitung jarak atau jarak terjauh
def horizontal_distance(v0, t, degree):
    tmax = projectile_airtime(v0, degree)
    v_horizontal = v0*np.cos(np.radians(degree))
    if t <= tmax:
        return v_horizontal*t
    else:
        return v_horizontal*tmax

# Fungsi untuk menghitung jarak vertikal atau tinggi
def vertical_distance(v0, t, degree):
    radius = np.radians(degree)
    v_vertikal = v0*np.sin(radius)
    h = v_vertikal*t - 0.5*g*t**2
    if h >= 0:
        return h
    else:
        return 0

# Fungsi untuk menghitung menampilkan pergerakan benda
def update_category(num, lines):
    for i in range(len(lines)):
        lines[i].set_data(horizontal_distances[i][:num], vertical_distances[i][:num])
    tm = np.round(num * time_interval, 1)
    plt.title('Kecepatan awal: {} m/s | Waktu simulasi: {} detik'.format(v0,tm))    
    return lines

# Input kecepatan awal dan sudut elevasinya
v0 = int(input('Masukkan kecepatan awal (m/s): '))
degree = list(map(int, input("Masukkan sudut elevasi (derajat): ").split()))

time_grounds = [projectile_airtime(v0, degrees) for degrees in degree]
time_ground = max(time_grounds)

# Penetapan interval waktu
time_interval = 0.1
time_steps = np.arange(0, time_ground + time_interval, time_interval)

# Menghitung jarak tempuh horizontal dan vertikal
horizontal_distances = [[horizontal_distance(v0, time_step, degrees) for time_step in time_steps] for degrees in degree]
vertical_distances = [[vertical_distance(v0, time_step, degrees) for time_step in time_steps] for degrees in degree]

# Membuat plot animasi
h_max = np.ceil(max([max(horizontal_distance) for horizontal_distance in horizontal_distances]))
v_max = np.ceil(max([max(vertical_distance) for vertical_distance in vertical_distances]))

# membuat plot table dan axis
figure, axes = plt.subplots()
plt.gca().set_aspect('equal')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True, which='both', color='0.65', linestyle='-')

# membuat plot garis
lines = [axes.plot([], [], label='{} degree'.format(degree))[0] for degrees in degree]
axes.axis([0, h_max, 0, v_max])
axes.legend()

# Tampilkan plot
style = animation.FuncAnimation(figure, update_category, frames=len(time_steps), fargs=[lines], interval=1000*time_interval)
plt.show()