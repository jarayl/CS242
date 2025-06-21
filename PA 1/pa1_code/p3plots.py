import matplotlib.pyplot as plt

# Data for Inner Product MM
inner_sizes = [16, 32, 64, 128, 256, 512, 1024]
inner_times = [1608, 14524, 431223, 2609776, 17655345, 151620594, 1298258722]

# Data for Outer Product MM
outer_sizes = [16, 32, 64, 128, 256, 512, 1024]
outer_times = [675, 4549, 48823, 189294, 2020087, 30324225, 249992849]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(inner_sizes, inner_times, label='Inner Product MM', marker='o', color='b')
plt.plot(outer_sizes, outer_times, label='Outer Product MM', marker='s', color='r')

# Adding titles and labels
plt.title('Matrix Multiplication Time Comparison (Inner vs Outer Product)')
plt.xlabel('Matrix Size N')
plt.ylabel('Average Time Over 5 Trials (ns)')
# plt.yscale('log')  # Logarithmic scale for better visibility
# plt.xscale('log')

# Adding legend
plt.legend()

# Show plot
plt.grid(True, which="both", ls="--")
plt.show()
