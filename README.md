# EcoSim
This repository contains a Python-based simulation that models the interaction between climate change and economics using **Agent-Based Modeling (ABM)**. The simulation tracks how different agents (such as countries or regions) behave over time, focusing on their economic output, carbon emissions, and investments in green technologies. The aim is to study how these factors influence global CO2 levels and temperature, as well as the potential impact of various climate-related policies.

## Features
- **Agent-based simulation**: Each agent represents a country or region with its own economy, CO2 emissions, and green technology investments.
- **Economic growth**: Agents grow their economy while balancing environmental impact.
- **Climate change dynamics**: The global climate changes based on cumulative CO2 emissions, increasing temperatures.
- **Green investments**: Agents can choose to invest in green technology to reduce future emissions.
- **Visualizations**: The simulation provides visual outputs of global CO2 levels and temperature changes over time.

## How the Model Works
In this simulation, each agent has an economy that produces carbon emissions based on its level of economic activity. Agents can also invest in green technology to reduce their emissions over time. However, high levels of carbon emissions lead to global temperature increases, which can negatively affect future economic growth.

### Key Concepts:
1. **Economic Growth**: Agents grow their economy each year, with higher emissions resulting in economic penalties.
2. **CO2 Emissions**: Agents emit CO2 proportional to their economic size, which contributes to global temperature rise.
3. **Green Investment**: Agents can invest in green technology, which reduces future emissions but may slow short-term economic growth.
4. **Global Temperature**: The cumulative emissions from all agents contribute to rising global temperatures, which has a feedback effect on economic output.

## Getting Started

### Prerequisites
To run the simulation, you’ll need Python 3.x and a few essential libraries installed.

1. **Python 3.x**: You can download and install Python from the [official website](https://www.python.org/downloads/).
2. **Required Libraries**: Install the following libraries using `pip`:
    ```bash
    pip install matplotlib numpy pandas
    ```

### Running the Simulation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. Run the Python script:
    ```bash
    python stock_price_tracker.py
    ```

3. The simulation will automatically run for a predefined number of years (default is 100). You’ll be prompted to enter a stock symbol, and after running, the script will display visualizations showing how the global temperature and CO2 levels have changed over time.

### Customizing the Simulation
You can easily modify parameters to test different scenarios. Some key parameters to experiment with include:
- **Initial Economy**: Adjust the starting size of each agent's economy.
- **CO2 Emissions**: Change the rate of CO2 emissions based on economic output.
- **Investment Rate**: Modify how agents decide to invest in green technologies.
- **Simulation Duration**: Change the number of years for the simulation.

## Results
The simulation generates two main outputs:
1. **Global Temperature Over Time**: A graph showing how global temperature increases as a result of cumulative CO2 emissions.
2. **Global CO2 Levels Over Time**: A graph that tracks the level of CO2 in the atmosphere as agents produce emissions or invest in green technology.

These visualizations give insight into how different economic policies and actions affect climate change.

## Example Output

Below is an example of what the simulation output might look like:

![Temperature and CO2 Simulation](path-to-your-image-if-you-want)

## Future Plans
This is just the beginning! Here are some potential areas for future development:
- **More Complex Agent Behaviors**: Implement decision-making models where agents perform cost-benefit analysis on climate actions.
- **Policy Options**: Add carbon taxes or caps-and-trade policies to see how they impact the economy and emissions.
- **Inter-agent Interactions**: Allow agents to trade resources, technology, or even emissions credits.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests if you have ideas for improving the simulation. Whether it's adding more features, fixing bugs, or enhancing the visualizations, your input is greatly appreciated.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions, feel free to reach out: nour.bousalman@unito.it
