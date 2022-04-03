# Importing everything
import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np
import pandas as pd

# DPI value for plotting
dpi_val = 1500

# Matplotlib setting to use LaTeX font for plots
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"]})

# Set up plotting
plotting.setup_mpl()

# Enabling cache
ff1.Cache.enable_cache(
    'path/to/cache')
# Get rid of some pandas warnings that are not relevant
pd.options.mode.chained_assignment = None


def f1_analysis(year, location, session, driver):
    # Getting race specified by user
    race = ff1.get_session(year, location, session)
    race.load()

    # Getting all the race laps with telemetry included
    laps_race = race.load_laps(with_telemetry=True)

    # Isolating the telemetry of the driver provided by the user
    laps_driver_race = laps_race.pick_driver(driver)

    # Getting the fastest lap of the driver
    fastest_driver_race = laps_driver_race.pick_fastest()

    # Getting all of the car data for the dirver's fastest lap
    telemetry_driver_race = fastest_driver_race.get_car_data().add_distance()

    return telemetry_driver_race


# Plots distance, throttle, and speed
def f1_plot(telemetry_1, telemetry_2, driver_1, driver_2, color_1, color_2, title, dpi_val, file_name):
    # Plotting the data using subplots; one for speed, throttle, and brake
    fig, ax = plt.subplots(3)
    fig.suptitle(title)

    ax[0].plot(telemetry_1['Distance'], telemetry_1['Speed'], label=driver_1, color=color_1)
    ax[0].plot(telemetry_2['Distance'], telemetry_2['Speed'], label=driver_2, color=color_2)
    ax[0].set(ylabel='Speed')
    ax[0].legend(loc='lower right')

    ax[1].plot(telemetry_1['Distance'], telemetry_1['Throttle'], label=driver_1, color=color_1)
    ax[1].plot(telemetry_2['Distance'], telemetry_2['Throttle'], label=driver_2, color=color_2)
    ax[1].set(ylabel='Throttle')

    ax[2].plot(telemetry_1['Distance'], telemetry_1['Brake'], label=driver_1, color=color_1)
    ax[2].plot(telemetry_2['Distance'], telemetry_2['Brake'], label=driver_2, color=color_2)
    ax[2].set(ylabel='Brakes')

    # Hide x-labels and tick labels for top plots and y ticks for right plots.
    for a in ax.flat:
        a.label_outer()

    plt.savefig(file_name, dpi=dpi_val)
    plt.show()

    return ax


# Calling analysis function for Bahrain GP - Ferrari 2022
lec_bahrain_2022 = f1_analysis(2022, "Bahrain", "r", "LEC")
sai_bahrain_2022 = f1_analysis(2022, "Bahrain", "r", "SAI")

# Calling alaysis function for Bahrain GP - Mercedes 2022
ham_bahrain_2022 = f1_analysis(2022, "Bahrain", "r", "HAM")
rus_bahrain_2022 = f1_analysis(2022, "Bahrain", "r", "RUS")

# Calling analysis function for Bahrain GP - Ferrari 2021
lec_bahrain_2021 = f1_analysis(2021, "Bahrain", "r", "LEC")
sai_bahrain_2021 = f1_analysis(2021, "Bahrain", "r", "SAI")

# Calling analysis function for Bahrain GP - Mercedes 2021
ham_bahrain_2021 = f1_analysis(2021, "Bahrain", "r", "HAM")
bot_bahrain_2021 = f1_analysis(2021, "Bahrain", "r", "BOT")

# Plotting Ferrari vs. Mercedes, Bahrain 2022

data_2022 = [lec_bahrain_2022, ham_bahrain_2022, "LEC", "HAM", 'r', 'c', "LEC vs. HAM - Bahrain GP 2022", 1500,
        "lec_ham_bahrain_2022.png"]

ferari_merc_b_2022 = f1_plot(data_2022[0], data_2022[1], data_2022[2], data_2022[3], data_2022[4], data_2022[5],
                             data_2022[6], data_2022[7], data_2022[8])


data_2021 = [lec_bahrain_2021, ham_bahrain_2021, "LEC", "HAM", 'r', 'c', "LEC vs. HAM - Bahrain GP 2021", 1500,
             "lec_ham_bahrain_2021.png"]

ferrari_merc_b_2021 = f1_plot(data_2021[0], data_2021[1], data_2021[2], data_2021[3], data_2021[4], data_2021[5],
                              data_2021[6], data_2021[7], data_2021[8])
