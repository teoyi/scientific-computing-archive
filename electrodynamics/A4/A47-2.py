import numpy as np 
import matplotlib.pyplot as plt 
'''
PH 403 Assignment 4
Plots for Griffith's Question 7.2
'''
# Declaring constants and derived values 
V0 = 120 # Initial voltage of the battery 
R = 110*10**3 # Resistance of the resistor  
C = 27*10**-6 # Capacitance of the capacitor 

Q0 = V0*C # Initial charge used for discharge situation 
tc = R*C # Time constant for the circuit (tau)

## For part a) 
def q_a(t): 
    return Q0 * np.exp(-t/tc)

def i_a(t): 
    return (V0/R) * np.exp(-t/tc)

## For part c) 
def q_c(t): 
    return C * V0 * (1 - np.exp(-t/tc))

def i_c(t): 
    return (V0/R) * np.exp(-t/tc)


t = np.arange(0,25,0.001)
fig = plt.figure()
plot1 = fig.add_subplot(1,2,1) 
plt.plot(t, q_a(t), label = "Q(t) for a)", zorder = 2)
plt.plot(t, q_c(t), label = "Q(t) for c)", zorder = 2)
plt.axvline(tc, linestyle = '--', color = 'black', label = "Time Constant", zorder = 1)
plt.xlabel("Time (s)")
plt.ylabel("Charge (C)")
plt.legend()

plot2 = fig.add_subplot(1,2,2)
plt.plot(t, i_a(t), label = "I(t) for a)", zorder = 2)
plt.plot(t, i_c(t), label = "I(t) for c)", zorder = 2)
plt.axvline(tc, linestyle = '--', color = 'black', label = "Time Constant", zorder = 1)
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.legend()

plt.show()