# coding=utf-8
# Reference:
# https://matplotlib.org/users/pyplot_tutorial.html
# https://matplotlib.org/tutorials/introductory/sample_plots.html
# legend:  https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend

import scipy.io
import matplotlib.pyplot as plt
data = scipy.io.loadmat('iden_xyz.mat')
print(data.keys())

plt.figure(1)

plt.subplot(3, 1, 1)
ATT = data['ATT']
plt.plot(ATT[:, 1]/1e6, ATT[:, 2], 'r:', ATT[:, 1]/1e6, ATT[:, 3], 'k--', linewidth=2)
plt.grid(True)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel("Roll (deg)", fontsize=14)

# plt.axis([40, 160, 0, 0.03])
# plt.ylim(-2,2)
# plt.title('Roll tracking', fontsize=14)
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

plt.subplot(3, 1, 2)
ATT = data['ATT']
plt.plot(ATT[:, 1]/1e6, ATT[:, 4], 'r:', ATT[:, 1]/1e6, ATT[:, 5], 'k--', linewidth=2)
plt.grid(True)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel("Pitch (deg)", fontsize=14)

plt.subplot(3, 1, 3)
ATT = data['ATT']
plt.plot(ATT[:, 1]/1e6, ATT[:, 6], 'r:', label="ref", linewidth=2)
plt.plot(ATT[:, 1]/1e6, ATT[:, 7], 'k--', label="real", linewidth=2)
plt.legend(loc='upper right', fontsize=12)
# plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.grid(True)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel("Pitch (deg)", fontsize=14)

plt.draw()

# plot angular rate of quadrotor
RATE = data['RATE']

plt.figure(2)

plt.subplot(3, 1, 1)
plt.plot(RATE[:, 1]/1e6, ATT[:, 2], 'r:', RATE[:, 1]/1e6, RATE[:, 3], 'k--', linewidth=2)
plt.grid(True)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel("Pitch (deg)", fontsize=14)

plt.subplot(3, 1, 2)
plt.plot(RATE[:, 1]/1e6, ATT[:, 5], 'r:', RATE[:, 1]/1e6, RATE[:, 6], 'k--', linewidth=2)
plt.grid(True)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel("Pitch (deg)", fontsize=14)

plt.subplot(3, 1, 3)
ax1, = plt.plot(RATE[:, 1]/1e6, ATT[:, 9], 'r:', linewidth=2)
ax2, = plt.plot(RATE[:, 1]/1e6, RATE[:, 10], 'k--', linewidth=2)

plt.grid(True)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel("Pitch (deg)", fontsize=14)
plt.legend((ax1, ax2), ("reference", "real"), loc='upper right')

plt.show()
plt.close('all')





