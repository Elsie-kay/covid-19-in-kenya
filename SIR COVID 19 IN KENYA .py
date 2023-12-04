import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
# parameters for the SIR model 
N = 55100586 # total population of Kenya 
I0 = 1 # initial number of infected individuals 
R0 = 0 # initial number of recovered individuals 
S0 = N - I0 - R0 # initial number of susceptible individuals 
beta = 0.3 # average contact rate in the population 
gamma = 0.1 # recovery rate 
# define the SIR model 
def sir_model(y, t, N, beta, gamma): 
 S, I, R = y 
 dSdt = -beta * S * I / N 
 dIdt = beta * S * I / N - gamma * I 
 dRdt = gamma * I 
 return dSdt, dIdt, dRdt
# initial conditions
y0 = S0, I0, R0
# time points
t = np.linspace(0, 1825, 1825)
# solve the ODEs
sol = odeint(sir_model, y0, t, args=(N, beta, gamma))
# plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, sol[:, 0], 'b', label='Susceptible')
plt.plot(t, sol[:, 1], 'r', label='Infected')
plt.plot(t, sol[:, 2], 'g', label='Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Number of individuals')
plt.title('Covid SIR Model in Kenya')
plt.legend()
plt.show()