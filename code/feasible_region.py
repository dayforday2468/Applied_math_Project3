import matplotlib.pyplot as plt
import numpy as np

# Theoritical limit
alpha_bound = 0.75

# trade-off slope
slope=2

def is_feasible(hypothesis,alpha,beta):
    if alpha<0 or 1<alpha: 
      return False
    if beta<0 or 1<beta:
      return False

    if hypothesis == "Avirulence":
       if alpha_bound<alpha:
          return False
    
    elif hypothesis == "Trade-off":
       if alpha>slope*beta:
          return False
    
    return True
        

def plot_avirulence():
    fig, ax = plt.subplots(figsize=(6,6))
    x = np.linspace(0, 1, 100)
    ax.fill_between(x, alpha_bound, 1, color='blue', alpha=0.3)
    ax.plot(x, [alpha_bound]*100, '--', color='blue')
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel("Virulence")
    ax.set_ylabel("Transmission rate")
    ax.set_title("Avirulence Theory")
    plt.show()

def plot_tradeoff(m):
    fig, ax = plt.subplots(figsize=(6,6))
    x = np.linspace(0, 1, 100)
    y = m * x
    y = np.clip(y, 0, 1)
    ax.fill_between(x, y, 1, color='blue', alpha=0.3)
    ax.plot(x, y, '--', color='blue')
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel("Virulence")
    ax.set_ylabel("Transmission rate")
    ax.set_title(f"Trade-off (slope={m})")
    plt.show()

# plot_avirulence()
# plot_tradeoff(slope)
