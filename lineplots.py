import matplotlib.pyplot as plt
import numpy as np

# set style for plots
plt.style.use('seaborn-v0_8-deep')
print(plt.style.available)

x_vals = np.linspace(0, 10, 100)

# line plots work well when graphing functions
# for example, y = f(x) or sin/cos/tan
plt.plot(x_vals, np.sin(x_vals), label='y=sin(x)')
plt.plot(x_vals, np.cos(x_vals), label='y=cos(x)')

# show figure in the dev environment
# plt.show()

# Save figure in a PNG file
plt.legend()
plt.savefig('lineplot.png')
plt.close() # clear the figure before making another

# Demo on customization
# f(x) = 2x
m = 2 # slope (rise / run)
b = 10 # y-intercept
# Set the y values to the equation
plt.plot(x_vals, (m*x_vals + b), label='y=2x+10', color='c')
plt.plot(x_vals, 3*x_vals, label='y=3x', color="#6c009a")
plt.plot(x_vals, 4*x_vals, label='y=4x', linestyle='dashed')
plt.plot(x_vals, 5*x_vals, label='y=5x', linestyle='dashdot')
plt.plot(x_vals, 0.5*x_vals, label='y=1/2x', linestyle='dotted')
# Add titles, labels, legend
plt.title('Linear Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('lineplot2.png')
plt.close()