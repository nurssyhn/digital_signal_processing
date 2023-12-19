import numpy as np
from numpy import arange, sin, pi
import matplotlib.pyplot as plt

# Kullanıcıdan öğrenci numarasını al
student_number = input("Lütfen öğrenci numaranızı girin: ")

# Öğrenci numarası üzerinden hesaplamalar
A = sum(int(digit) for digit in student_number)
frequencies = [1000, 2000, 5000]
first_digit = int(student_number[0])
last_digit = int(student_number[-1])
t_max = round(first_digit + last_digit) * 2
sampling_rate = 50000
t = arange(0, t_max, 1/sampling_rate)

# Sinyalleri ve gürültüyü oluştur
signals = {}
noisy_signals = {}
noise = np.random.normal(0, A / len(student_number), len(t))
for f in frequencies:
    signals[f] = A * sin(2 * pi * f * t)
    noisy_signals[f] = signals[f] + noise

# Kayan ortalama algoritması
def moving_average(signal, window_size=3):
    return np.convolve(signal, np.ones(window_size) / window_size, mode='valid')

# Grafik çizme fonksiyonu
def plot_signals(frequency):
    filtered_signal = moving_average(noisy_signals[frequency])

    plt.figure(figsize=(10, 20))

    # 1. Orijinal İşaret
    plt.subplot(5, 1, 1)
    plt.plot(t, signals[frequency], label="Orijinal İşaret")
    plt.title(f"f={frequency} Hz - Orijinal İşaret")
    plt.xlabel("Zaman")
    plt.ylabel("Amplitüd")
    plt.legend()

    # 2. Gürültü İşareti
    plt.subplot(5, 1, 2)
    plt.plot(t, noise, label="Gürültü İşareti", color='orange')
    plt.title("Gürültü İşareti")
    plt.xlabel("Zaman")
    plt.ylabel("Amplitüd")
    plt.legend()

    # 3. Gürültülü İşaret
    plt.subplot(5, 1, 3)
    plt.plot(t, noisy_signals[frequency], label="Gürültülü İşaret")
    plt.title("Gürültülü İşaret")
    plt.xlabel("Zaman")
    plt.ylabel("Amplitüd")
    plt.legend()

    # 4. Gürültüden Arındırılmış İşaret
    plt.subplot(5, 1, 4)
    plt.plot(t[:len(filtered_signal)], filtered_signal, label="Gürültüden Arındırılmış İşaret", color='green')
    plt.title("Gürültüden Arındırılmış İşaret")
    plt.xlabel("Zaman")
    plt.ylabel("Amplitüd")
    plt.legend()

    # 5. Gürültülü ve Gürültüden Arındırılmış İşaretler Üst Üste
    plt.subplot(5, 1, 5)
    plt.plot(t, noisy_signals[frequency], label="Gürültülü İşaret", alpha=0.5)
    plt.plot(t[:len(filtered_signal)], filtered_signal, label="Gürültüden Arındırılmış İşaret", color='red', alpha=0.5)
    plt.title("Gürültülü ve Gürültüden Arındırılmış İşaretler Karşılaştırması")
    plt.xlabel("Zaman ve amplitüd")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Her frekans için grafikleri çiz
for f in frequencies:
    plot_signals(f)

