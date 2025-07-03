# ✈️ SmartAirlineMarketAnalyser

A comprehensive Python web application for analyzing airline booking market demand data using real-time flight information and AI-powered insights.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.46+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Overview

SmartAirlineMarketAnalyser is a web application designed to help businesses in the travel and hospitality industry understand airline booking market demand trends. The app fetches real-time flight data from multiple aviation APIs and uses AI-powered analysis to provide actionable insights about route popularity, demand patterns, peak hours, and aircraft utilization.

### Key Features

- **Real-time Data Fetching**: Integrates with OpenSky Network and AviationStack APIs for live flight data
- **AI-Powered Analysis**: Uses Google Gemini API for intelligent data interpretation
- **Interactive Dashboard**: Built with Streamlit for a user-friendly interface
- **Visual Analytics**: Rich charts and graphs using Plotly
- **Multi-Country Support**: Analyze flight data for different countries
- **Time Range Selection**: View data for last 24 hours, 7 days, or 30 days
- **Demand Insights**: Identify popular routes, peak hours, and trends

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- API keys for:
  - Google Gemini API (for AI analysis)
  - AviationStack API (optional, for additional data)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SmartAirlineMarketAnalyser.git
   cd SmartAirlineMarketAnalyser
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if using uv:
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   AVIATIONSTACK_API_KEY=your_aviationstack_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the web app**
   Open your browser and go to `http://localhost:8501`

## 🛠️ Project Structure

```
SmartAirlineMarketAnalyser/
├── app.py                 # Main Streamlit application
├── data_fetcher.py        # Handles API data fetching
├── ai_analyzer.py         # AI-powered data analysis
├── utils.py              # Utility functions
├── pyproject.toml        # Project configuration
├── uv.lock              # Dependency lock file
├── README.md            # This file
└── attached_assets/     # Project documentation and assets
```

## 📊 Features in Detail

### Data Sources

1. **OpenSky Network API**
   - Free, no API key required
   - Real-time flight tracking data
   - Global flight coverage

2. **AviationStack API**
   - Comprehensive flight information
   - Historical flight data
   - Airline and airport details

### Analysis Types

- **Route Popularity**: Identify the most frequently traveled routes
- **Demand Trends**: Track booking patterns and market demand
- **Peak Hours**: Discover busiest times for air travel
- **Aircraft Types**: Analyze aircraft utilization and preferences

### AI Capabilities

The application uses Google Gemini API to:
- Extract meaningful insights from flight data
- Identify patterns and trends
- Generate actionable recommendations
- Provide natural language explanations

## 🖥️ User Interface

The web app features:
- **Interactive Sidebar**: Country selection, time range, and analysis options
- **Real-time Metrics**: Key performance indicators and statistics
- **Visual Charts**: Interactive plots for data visualization
- **AI Insights**: Natural language summaries and recommendations
- **Data Export**: Download analysis results
![image](https://github.com/user-attachments/assets/d0ce9d8e-93ce-4596-93a2-40f2fb96395c)


## 🔧 Configuration

### API Keys Setup

1. **Google Gemini API**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add to your environment variables

2. **AviationStack API** (Optional)
   - Sign up at [AviationStack](https://aviationstack.com/)
   - Get your free API key
   - Add to your environment variables

### Customization

You can customize the application by:
- Modifying analysis parameters in `ai_analyzer.py`
- Adding new data sources in `data_fetcher.py`
- Customizing the UI in `app.py`
- Adding new utility functions in `utils.py`

## 📈 Use Cases

### For Hostel Chains
- Monitor guest travel patterns
- Optimize location strategies
- Predict demand fluctuations

### For Travel Agencies
- Identify popular destinations
- Track seasonal trends
- Optimize pricing strategies

### For Market Researchers
- Analyze aviation market trends
- Study route performance
- Generate industry reports

## 🔍 Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Requests**: HTTP library for API calls
- **Google GenAI**: AI analysis capabilities
- **NumPy**: Numerical computing

### Data Processing

The application processes flight data through:
1. **Data Fetching**: Retrieve real-time flight information
2. **Data Cleaning**: Handle missing values and format data
3. **Feature Engineering**: Create meaningful metrics
4. **AI Analysis**: Generate insights using machine learning
5. **Visualization**: Create interactive charts and graphs

## 🚨 Error Handling

The application includes comprehensive error handling for:
- API connection failures
- Invalid API keys
- Data processing errors
- Network timeouts
- Rate limiting

## 📊 Performance

- **Caching**: 5-minute TTL for API responses
- **Efficient Data Processing**: Optimized pandas operations
- **Responsive UI**: Real-time updates and feedback
- **Scalable Architecture**: Modular design for easy extension

## 🔐 Security

- Environment variables for API keys
- Input validation and sanitization
- Rate limiting compliance
- Error message sanitization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/SmartAirlineMarketAnalyser/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 🙏 Acknowledgments

- [OpenSky Network](https://opensky-network.org/) for free flight data
- [AviationStack](https://aviationstack.com/) for comprehensive aviation API
- [Google Gemini](https://ai.google.dev/) for AI analysis capabilities
- [Streamlit](https://streamlit.io/) for the amazing web framework

---

**Built with ❤️ for the travel and hospitality industry**
