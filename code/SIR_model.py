import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# model parameters
K=500
recovery_rate=0.07
death_rate=0.00002

# Initial conditions
S0 = 499
I0 = 1
R0 = 0

# Time span
T=(int)(2/recovery_rate)
t_span = (0, T)
t_eval = np.linspace(t_span[0], t_span[1], 4*T)


# Define SIRS model
def SIR_model(t,y,alpha,beta):
  S,I,R=y
  N=S+I+R
  dS=N*(1-N/K)-(S/N)*I*alpha-S*death_rate
  dI=(S/N)*I*alpha-I*(recovery_rate+beta+death_rate)
  dR=I*recovery_rate-R*death_rate

  return [dS,dI,dR]

# Solve the system
def solve(alpha,beta):
  sol = solve_ivp(lambda t, y: SIR_model(t, y, alpha, beta),t_span, [S0, I0, R0], t_eval=t_eval)
  return sol


def plot_model(sol):
  plt.figure(figsize=(10,6))
  plt.plot(sol.t, sol.y[0], label='Susceptible (S)')
  plt.plot(sol.t, sol.y[1], label='Infected (I)')
  plt.plot(sol.t, sol.y[2], label='Recovered (R)')
  plt.plot(sol.t,sol.y[0]+sol.y[1]+sol.y[2],label='Total (N)')
  plt.xlabel('Time')
  plt.ylabel('Population')
  plt.title('SIR Model Dynamics')
  plt.legend()
  plt.grid()
  plt.show()

