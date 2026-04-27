import random
import numpy as np
import matplotlib.pyplot as plt

""" lesson 1 """

# setting the measurement of the list
N1 = int(input('Enter N1: '))
N2 = int(input('Enter N2: '))
N3 = int(input('Enter N3: '))
MCS = int(input('Enter Amount of MK steps: '))
# T = float(input('Enter T: '))

def cell(N):
    S_alpha = [[0]*(N) for i in range(N)]
    S = np.array(S_alpha)
    # filling the list up with random elements 
    for i in range(0,N):
        for j in range(0,N):
            S[i][j] = int(random.choice([-1,1]))
    return S
        #S[i][j] = 1 """ for debugging """

# calulating the magnetic moment
def total_M(S):
    return np.sum(S)


def En_calc(S):
    summ = 0
    for i in range(len(S)):
        for j in range(len(S)-1):
                summ+=S[i][j]*S[i][j+1]+S.T[i][j]*S.T[i][j+1]
        summ+=S[i][0]*S[i][len(S)-1]+S.T[i][0]*S.T[i][len(S.T)-1]

    return -summ

cell_const = cell(N1)*1

""" lesson 2 """ # """ теперь через рандомайзер между 0 и 1 создаем некую вероятность, сравниваем ее с вычисленной вероятностью P и если Rnd < P, то принимаем эту конфигурацию E_c и работаем с ней, если нет - работаем с предыдущей конфигурацией E """

def mcstep(S, T, N):
    En_old = En_calc(S)
    ry, rx = random.randint(0, N-1), random.randint(0, N-1)
    S[ry][rx] *= -1 
    dE = En_calc(S) - En_old
    if dE < 0:
        pass

    elif dE >= 0:
        P = np.exp(-dE/T)
        R = random.uniform(0,1)
        if P > R:
            pass

        elif P < R:
            S[ry][rx] *= -1 
            pass

""" lesson 3 """

def capacity(S, T_t, MCS, N):
    E_ar = []
    E_av_of_sq = 0
    E_sq_of_av = 0
    step = 0
    while step < MCS:
        mcstep(S, T_t, N)
        E_ar.append(En_calc(S))
        step += 1    
    E_av_of_sq = np.mean(E_ar)
    E_sq_of_av = np.mean(np.array(E_ar)**2)
    return (abs(E_sq_of_av/MCS - (E_av_of_sq/MCS)**2))/((T_t**2)*(N**2))


def capacities(MCS, S, S_const, N):
    temperatures = np.arange(1.8, 2.8, 0.001)
    capacities = []
    for T_t in temperatures:
        S = S_const*1
        capacities.append(capacity(S, T_t, MCS, N))
    
    return temperatures, capacities

temps, caps = capacities(MCS, cell(N1), cell_const, N1)

""" lesson 4 """

""" def binder(S, MCS, N):
    temperatures = np.arange(1.8, 2.8, 0.001)
    binders = []
    for T_t in temperatures:
        turbo_total_M = []
        stepp = 0
        while stepp < MCS:
            mcstep(S, T_t, N)
            turbo_total_M.append(total_M(S))
            stepp += 1    
        M_sq_of_av = np.mean(np.array(turbo_total_M)**2)
        M_qd_of_av = np.mean(np.array(turbo_total_M)**4)
        U = 1 - (M_qd_of_av/(3*(M_sq_of_av)**2))
        binders.append(U)
    return binders

bin1 = binder(cell(N1), MCS, N1)
bin2 = binder(cell(N2), MCS, N2)
bin3 = binder(cell(N3), MCS, N3) """

# creating the graph space
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# graph 1: C(T)
ax1.plot(temps, caps, 'bo-', marker='o', linestyle='', linewidth=1, markersize=2)
ax1.set_xlabel('Температура, T', fontsize=12)
ax1.set_ylabel('Теплоемкость, C', fontsize=12)
Tc_theoretical = 2.269
ax1.axvline(x=Tc_theoretical, color='r', linestyle='--', alpha=0.7, label=f'Tc ≈ {Tc_theoretical}')
ax1.set_title(f'Зависимость теплоемкости от температуры\nN={N1}, MK steps={MCS}', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='both', which='major', labelsize=10)

# graph 2: M(T)
""" colors = ['#1f77b4', '#2ca02c', '#d62728']
ax2.plot(temps, bin1, 'bo-', marker='o', linestyle='', linewidth=1, markersize=2, color = colors[0])
ax2.plot(temps, bin2, 'bo-', marker='o', linestyle='', linewidth=1, markersize=2, color = colors[1])
ax2.plot(temps, bin3, 'bo-', marker='o', linestyle='', linewidth=1, markersize=2, color = colors[2])
ax2.set_xlabel('Температура, T', fontsize=12)
ax2.set_ylabel('Кумулянт Биндера, U', fontsize=12)
Tc_theoretical = 2.269
ax2.axvline(x=Tc_theoretical, color='r', linestyle='--', alpha=0.7, label=f'Tc ≈ {Tc_theoretical}')
ax2.set_title(f'Зависимость теплоемкости от температуры\nN={N1, N2, N3}, MK steps={MCS}', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.tick_params(axis='both', which='major', labelsize=10) """

# layout typo
plt.tight_layout()

# saving to file
plt.savefig(f'ising_model_N{N1, N2, N3}_A{MCS}.png', dpi=300, bbox_inches='tight')

# graph unleashed
plt.show()

""" general task """

""" lesson 3 """

"""Построить график зависимости теплоёмкости от температуры в модели Изинга.

Теплоёмкость:
С = (<Е^2> - <Е>^2)/Т^2
Где <Е^2> - средний квадрат энергии системы, 
<Е> - средняя энергия системы. (Средняя за 10000 шагов Монте-Карло)
Размер модели 10*10.
Область исследования температуры от 1 до 3 К. С шагом 0,1."""

""" lesson 4 """

"""Рассчитать величину Камуляр Биндера - 
U_L = 1 - ( <M^4> )/( 3<M^2>^2 ), где М - намагниченность
Четвёртая задача заключается в том, чтобы построить график 
зависимости кумулянта Биндера от температуры.
Комулянт Биндера:
U = 1 - <M^4>/3<M^2>^2
М - намагниченность (сумма всех элементов в модели изинга)
<M^4> - среднее значение  для М в четвертой степени;
<M^2>^2 - квадрат среднего значения для М в квадрате.
На графике должно быть построено несколько зависимостей 
для разных размеров модели изинга (10 на 10, 20 на 20 и 30 на 30). 
Значения графиков должно усредняется по 10 испытаниям. """
