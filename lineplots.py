import matplotlib.pyplot as plt
import numpy as np

# set style for plots
plt.style.use('seaborn-v0_8-deep')
print(plt.style.available)

x_vals = np.linspace(0, 10, 100)

# line plots work well when graphing functions
# for example, y = f(x) or sin/cos/tan
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

# show figure in the dev environment
# plt.show()

# Save figure in a PNG file
plt.savefig('lineplot.png')
plt.close() # clear the figure before making another

# Demo on customization
# f(x) = 2x
plt.plot(x_vals, 2*x_vals, '-m')
# Add titles, labels, legend
plt.title('A Simple Line: y=2x')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('lineplot2.png')
plt.close()