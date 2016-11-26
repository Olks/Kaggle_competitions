
# # Import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
#
# year = [2010,2011,2012,2013,2014,2015,2016]
# pop  = [2,6,12,15,17,18,19]
#
# # Make a line plot: year on the x-axis, pop on the y-axis
# plt.plot(year,pop)
# plt.show()
# plt.clf()
#
# # Change the line plot below to a scatter plot
# plt.scatter(year, pop)
#
# # Put the x-axis on a logarithmic scale
# plt.yscale('log')
#
# # Show plot
# plt.show()
# plt.clf()
#
# #help(plt.hist)


##########################################
##########################################

# Import numpy as np
# import numpy as np
#
# pop = [1,2,2,4,5]
#
# # Store pop as a numpy array: np_pop
# np_pop = np.array(pop)
#
# # Double np_pop
# np_pop = 200*np_pop
#
# gdp_cap = [3,4,1,6,2]
# life_exp = [6,4,1,8,2]
# col = ['green', 'red', 'yellow', 'black', 'purple']
#
#
# # Update: set s argument to np_pop
# plt.scatter(gdp_cap, life_exp, s = np_pop, c=col, alpha=0.8)
#
# # Previous customizations
# plt.xscale('log')
# plt.xlabel('GDP per Capita [in USD]')
# plt.ylabel('Life Expectancy [in years]')
# plt.title('World Development in 2007')
# plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
#
# # Display the plot
# plt.show()

###############################################


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 1000 times
for i in range(1000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
