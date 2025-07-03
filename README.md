# Smart Airline Market Analyzer

A comprehensive web application for analyzing airline market demand data using AI-powered insights.

## 🚀 Features

- **Real-time Flight Data**: Fetch live flight data from OpenSky Network and AviationStack APIs
- **AI-Powered Analysis**: Get intelligent insights using Google Gemini AI
- **Interactive Dashboard**: Beautiful visualizations with Plotly
- **Market Trends**: Analyze route popularity, demand patterns, and peak hours
- **Recommendations**: AI-generated business recommendations for hospitality industry

## 📋 Prerequisites

- Python 3.11 or higher
- API keys for external services

## 🔑 API Keys Setup

This application requires two API keys:

### 1. Google Gemini API Key
- **Purpose**: Powers AI analysis and insights
- **How to get**: 
  1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
  2. Sign in with your Google account
  3. Create a new API key
  4. Copy the generated key

### 2. AviationStack API Key
- **Purpose**: Fetches detailed flight data
- **How to get**:
  1. Go to [AviationStack](https://aviationstack.com/dashboard)
  2. Sign up for a free account
  3. Navigate to your dashboard
  4. Copy your API key

## 🛠️ Installation

### Method 1: Automated Setup (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd SmartAirlineMarketAnalyser
   ```

2. **Run the setup script**:
   ```bash
   python setup.py
   ```

3. **Configure API keys**:
   - Open the `.env` file in your project root
   - Replace the placeholder values with your actual API keys:
   ```env
   GEMINI_API_KEY=your_actual_gemini_key_here
   AVIATIONSTACK_API_KEY=your_actual_aviationstack_key_here
   ```

### Method 2: Manual Setup

1. **Install dependencies**:
   ```bash
   pip install -e .
   ```

2. **Create environment file**:
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_actual_gemini_key_here
   AVIATIONSTACK_API_KEY=your_actual_aviationstack_key_here
   ```

## 🚁 Running the Application

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application**:
   - Open your browser and go to `http://localhost:8501`
   - The app will automatically detect your API keys

## 📁 Project Structure

```
SmartAirlineMarketAnalyser/
├── app.py                 # Main Streamlit application
├── ai_analyzer.py         # AI analysis module
├── data_fetcher.py        # Data fetching from APIs
├── utils.py               # Utility functions
├── setup.py               # Setup script
├── .env                   # Environment variables (API keys)
├── .gitignore             # Git ignore file
├── pyproject.toml         # Project dependencies
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables

The application uses the following environment variables:

- `GEMINI_API_KEY`: Google Gemini AI API key
- `AVIATIONSTACK_API_KEY`: AviationStack API key

### API Rate Limits

- **OpenSky Network**: No API key required, but has rate limits
- **AviationStack**: Free tier allows 100 requests/month
- **Google Gemini**: Generous free tier available

## 🎯 Usage

1. **Select Analysis Parameters**:
   - Choose country/region
   - Select time range
   - Pick analysis types

2. **Fetch Data**:
   - Click "Fetch Flight Data" to get real-time information
   - The app will automatically process and analyze the data

3. **View Insights**:
   - Browse interactive charts and visualizations
   - Read AI-generated analysis and recommendations
   - Export data for further analysis

## 📊 Features Overview

### Data Sources
- **OpenSky Network**: Real-time flight tracking (free)
- **AviationStack**: Historical flight data and airline information

### Analysis Types
- **Route Popularity**: Most traveled routes and destinations
- **Demand Trends**: Temporal patterns and seasonal variations
- **Peak Hours**: Busiest times for air travel
- **Market Insights**: AI-powered business recommendations

### Visualizations
- Interactive maps showing flight routes
- Time-series charts for demand analysis
- Bar charts for route popularity
- Pie charts for market share analysis

## 🔒 Security

- **API Keys**: Stored securely in `.env` file
- **Git Protection**: `.env` file is excluded from version control
- **Best Practices**: Never commit API keys to repository

## 🐛 Troubleshooting

### Common Issues

1. **"API key not found" error**:
   - Ensure `.env` file exists in project root
   - Check that API keys are properly formatted
   - Restart the application after updating keys

2. **Import errors**:
   - Run `pip install -e .` to install dependencies
   - Check Python version (requires 3.11+)

3. **Data fetching errors**:
   - Verify API keys are valid and active
   - Check internet connection
   - Review API rate limits

### Debug Mode

To enable debug mode, add to your `.env` file:
```env
DEBUG=True
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section
2. Review API provider documentation
3. Create an issue in the repository

## 🎉 Acknowledgments

- OpenSky Network for free flight data
- AviationStack for comprehensive aviation APIs
- Google Gemini for AI analysis capabilities
- Streamlit for the amazing web framework
