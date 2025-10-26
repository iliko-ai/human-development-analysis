# Human Development Analysis Dashboard

A comprehensive Streamlit-based interactive dashboard for analyzing global human development indicators using Gapminder data. This project provides insights into life expectancy, GDP per capita, Human Development Index (HDI), and CO2 consumption patterns across different continents and countries over time.

## 🌍 Overview

This dashboard analyzes human development data from 1998 to 2018, focusing on key indicators that measure the quality of life and economic development across different regions of the world. The application provides interactive visualizations and statistical analysis to help understand global development trends and patterns.

## 📊 Key Features

### 1. **Data Exploration**
- Interactive scatter plots showing the relationship between GDP per capita and life expectancy
- Year-based filtering to explore data for specific time periods
- Continent-wise color coding for easy comparison
- Key insights highlighting countries with very high human development (HDI ≥ 0.8)
- Average metrics display for GDP, life expectancy, and HDI

### 2. **Statistical Analysis**
- Box plots comparing life expectancy, GDP, and HDI across continents
- CO2 consumption analysis by continent
- Comprehensive statistical visualizations for the selected year
- Comparative analysis highlighting regional differences

### 3. **GDP Distribution Visualization**
- Interactive sunburst plot showing global GDP distribution
- Hierarchical view: Continent → Country
- Percentage share calculations within each continent
- Identification of highest GDP countries by region

### 4. **Time Series Analysis**
- Development trends over time (1998-2018) for:
  - GDP per capita
  - Human Development Index (HDI)
  - CO2 consumption
- Visual markers for significant events (e.g., 2008 Financial Crisis)
- Continent-wise trend comparison

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Plotly Express
- **Data Source**: Gapminder dataset
- **Package Management**: uv (Python package manager)

## 📈 Data Sources

The dashboard uses the Gapminder dataset (`gapminder_data_graphs.csv`) which includes:
- **Country**: Country names
- **Continent**: Geographic regions (Asia, Africa, Europe, North America, Oceania, South America)
- **Year**: Time period (1998-2016)
- **Life Expectancy**: Average life expectancy in years
- **HDI Index**: Human Development Index (0-1 scale)
- **CO2 Consumption**: Per capita CO2 consumption
- **GDP**: GDP per capita
- **Services**: Services sector data

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- uv package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Human-Development-Analysis
   ```

2. **Install dependencies using uv**:
   ```bash
   uv sync
   ```

3. **Run the application**:
   ```bash
   uv run streamlit run human_development_analysis/app.py
   ```

4. **Access the dashboard**:
   Open your browser and navigate to `http://localhost:8501`

## 📱 Usage

### Navigation
The dashboard includes a sidebar with the following sections:
- **Home**: Overview with all visualizations
- **Data Exploration**: Interactive scatter plots and metrics
- **Statistical Analysis**: Box plots and comparative analysis
- **GDP Distribution**: Sunburst plot for GDP distribution
- **Time Analysis**: Time series development trends

### Key Interactions
- **Year Selection**: Use the year dropdown to filter data for specific years
- **Interactive Charts**: Hover over data points for detailed information
- **Navigation**: Use sidebar buttons to switch between different analysis views

## 🔍 Key Insights

The dashboard reveals several important patterns:

1. **Development Correlation**: Strong positive correlation between GDP per capita and life expectancy
2. **Regional Variations**: Significant differences in development indicators across continents
3. **Temporal Trends**: Gradual improvement in human development indicators over time
4. **Crisis Impact**: Notable effects of the 2008 financial crisis on CO2 consumption patterns
5. **HDI Thresholds**: Clear identification of countries achieving very high human development levels

## 🎨 Design Features

- **Consistent Color Scheme**: Continent-specific color mapping for easy identification
- **Responsive Layout**: Wide layout optimized for data visualization
- **Interactive Elements**: Hover tooltips and clickable legends
- **Professional Styling**: Clean, white background with black text for readability
- **Custom CSS**: Enhanced styling for better user experience

## 📁 Project Structure

```
human_development_analysis/
├── app.py                          # Main Streamlit application
├── components/                     # UI components
│   ├── data_exploration.py        # Data exploration visualizations
│   ├── development_time_series.py # Time series analysis
│   ├── gdp_distribution.py        # GDP distribution plots
│   ├── sidebar.py                 # Navigation sidebar
│   └── stastistical_analysis.py   # Statistical analysis charts
├── constants/
│   └── constants.py               # Color mappings and configuration
├── data/
│   └── gapminder_data_graphs.csv  # Main dataset
├── styles/
│   └── style.css                  # Custom CSS styling
├── utils/
│   └── continent_utils.py         # Utility functions for data processing
├── pyproject.toml                 # Project dependencies
└── README.md                      # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Check out the app on Streamlit
https://human-development-analysis.streamlit.app/

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Gapminder Foundation** for providing the comprehensive global development dataset
- **Streamlit** for the excellent web application framework
- **Plotly** for interactive visualization capabilities

---

*This dashboard is designed to make global development data accessible and understandable, helping users explore the complex relationships between economic development, human well-being, and environmental factors across different regions and time periods.*
# human-development-analysis
