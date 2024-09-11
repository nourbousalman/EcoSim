import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants for the simulation
INIT_ECONOMY = 1000  # Initial economic strength of each agent
INIT_CO2 = 300  # Initial CO2 emissions in ppm
TEMP_INCREASE_RATE = 0.02  # Rate of temperature increase per unit of CO2
CO2_ABSORPTION_RATE = 0.01  # Rate at which CO2 is naturally absorbed

class Agent:
    def __init__(self, name, economy, co2_emissions, green_investment):
        self.name = name
        self.economy = economy
        self.co2_emissions = co2_emissions
        self.green_investment = green_investment

    def produce_co2(self):
        """Simulate CO2 production based on economic activity and green investments."""
        self.co2_emissions += self.economy * (1 - self.green_investment)

    def invest_in_green_tech(self):
        """Increase green technology investment, reducing future emissions."""
        self.green_investment += random.uniform(0.01, 0.05)
        self.green_investment = min(self.green_investment, 1.0)  # Capping at 100%

    def economic_growth(self):
        """Simulate economic growth, which is tied to investments and emissions."""
        growth_rate = 0.03 - (self.co2_emissions / 5000)  # Penalty for high CO2 emissions
        self.economy += self.economy * growth_rate

    def take_action(self):
        """Decide whether to invest in green tech or prioritize economic growth."""
        if random.random() < 0.5:
            self.invest_in_green_tech()
        self.economic_growth()
        self.produce_co2()

def simulate_climate_economics(agents, years):
    global_co2 = INIT_CO2
    global_temp = 0
    history = []

    for year in range(years):
        year_data = {'Year': year}
        for agent in agents:
            agent.take_action()
            year_data[agent.name + '_Economy'] = agent.economy
            year_data[agent.name + '_CO2'] = agent.co2_emissions

        # Global CO2 emissions and temperature rise
        total_co2 = sum(agent.co2_emissions for agent in agents)
        global_co2 += total_co2 - (global_co2 * CO2_ABSORPTION_RATE)
        global_temp += global_co2 * TEMP_INCREASE_RATE

        year_data['Global_CO2'] = global_co2
        year_data['Global_Temperature'] = global_temp
        history.append(year_data)

    return pd.DataFrame(history)

def plot_results(df):
    """Plot economic, CO2, and temperature trends over time."""
    years = df['Year']

    plt.figure(figsize=(10, 6))

    # Plotting global temperature
    plt.subplot(2, 1, 1)
    plt.plot(years, df['Global_Temperature'], label="Global Temperature", color="red")
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.title('Global Temperature Over Time')
    plt.legend()

    # Plotting CO2 emissions
    plt.subplot(2, 1, 2)
    plt.plot(years, df['Global_CO2'], label="Global CO2 (ppm)", color="blue")
    plt.xlabel('Year')
    plt.ylabel('CO2 Levels (ppm)')
    plt.title('Global CO2 Levels Over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Create agents
agents = [
    Agent(name="Country_A", economy=INIT_ECONOMY, co2_emissions=INIT_CO2, green_investment=0.1),
    Agent(name="Country_B", economy=INIT_ECONOMY, co2_emissions=INIT_CO2, green_investment=0.05),
]

# Run simulation
years = 100
simulation_data = simulate_climate_economics(agents, years)

# Plot the results
plot_results(simulation_data)
