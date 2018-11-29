import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv("data.csv")

print(csv_file.head())
print(csv_file.columns)


# -----------------------------------------------Client vs Protocol------------------------------------#

plt.plot(csv_file['Protocol'], csv_file['Destination'], '*')
plt.title('Client vs Protocol')
plt.xlabel('protocol -> ')
plt.ylabel('Destination ->')

plt.autoscale(enable=True, axis='x', tight=False)
plt.tight_layout()  # plt.axis('tight')
plt.show()

fig = plt.gcf()
fig.set_size_inches(11, 8)

# ------------------------------------------Length of the packets VS Destination--------------------------------#

plt.plot(csv_file['Length'], csv_file['Destination'], '^')
plt.xlabel('Length of packet->')
plt.ylabel('Destination Address ->')
plt.title('Length of the packets VS Destination')
plt.autoscale(enable=True, axis='x', tight=False)
plt.tight_layout()  # plt.axis('tight')
plt.show()

# print(csv_file["Info"])
















