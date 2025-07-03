# Airline Market Demand Analytics

## Overview

This is a Python web application built with Streamlit that analyzes airline booking market demand data. The application fetches real-time flight data from aviation APIs, processes it using AI-powered analytics, and presents insights through an interactive web interface. It's designed to help businesses understand market demand trends, popular routes, pricing patterns, and peak travel periods.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

### Frontend Architecture
- **Framework**: Streamlit for rapid web app development
- **UI Components**: Interactive sidebar controls, data visualization charts, and dashboard-style layout
- **Visualization**: Plotly Express and Plotly Graph Objects for interactive charts and graphs
- **State Management**: Streamlit session state for maintaining application state across user interactions

### Backend Architecture
- **Data Layer**: Modular data fetching system supporting multiple aviation APIs
- **Processing Layer**: AI-powered analytics engine using OpenAI GPT-4o
- **Utility Layer**: Common functions for data formatting, caching, and country code mapping

## Key Components

### 1. Data Fetcher (`data_fetcher.py`)
- **Purpose**: Handles data retrieval from external aviation APIs
- **Supported APIs**: OpenSky Network (free), AviationStack (requires API key)
- **Features**: Geographic filtering, time range selection, data caching
- **Rationale**: Abstracted to easily add new data sources and handle API rate limits

### 2. AI Analyzer (`ai_analyzer.py`)
- **Purpose**: Processes flight data using OpenAI GPT-4o for intelligent insights
- **Analysis Types**: Route popularity, demand trends, peak hours, aircraft types
- **Fallback**: Basic analysis when OpenAI API is unavailable
- **Rationale**: Provides value-added insights beyond raw data presentation

### 3. Main Application (`app.py`)
- **Purpose**: Streamlit web interface orchestrating all components
- **Features**: Interactive controls, real-time data visualization, responsive layout
- **State Management**: Session state for maintaining user preferences and cached data

### 4. Utilities (`utils.py`)
- **Purpose**: Common helper functions and decorators
- **Features**: Currency formatting, data caching, country code mapping
- **Rationale**: Reduces code duplication and provides consistent functionality

## Data Flow

1. **User Input**: Users select data source, geographic filters, and analysis preferences through the Streamlit sidebar
2. **Data Fetching**: DataFetcher retrieves flight data from selected APIs based on user criteria
3. **Data Processing**: Raw flight data is cleaned and structured into pandas DataFrames
4. **AI Analysis**: AIAnalyzer processes the data to extract insights and trends
5. **Visualization**: Results are displayed through interactive Plotly charts and Streamlit components
6. **Caching**: Data and analysis results are cached to improve performance and reduce API calls

## External Dependencies

### APIs
- **OpenSky Network**: Free aviation data API (no authentication required)
- **AviationStack**: Premium aviation data API (requires API key)
- **Google Gemini**: AI-powered data analysis (requires API key)

### Python Libraries
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualization
- **Requests**: HTTP client for API calls
- **Google GenAI**: Official Google Gemini Python client

### Environment Variables
- `GEMINI_API_KEY`: Required for AI analysis features
- `AVIATIONSTACK_API_KEY`: Required for AviationStack data source

## Deployment Strategy

The application is designed for easy deployment on Replit:

1. **Environment Setup**: API keys configured through Replit secrets
2. **Dependencies**: All requirements specified in requirements.txt
3. **Entry Point**: `streamlit run app.py` as the main command
4. **Scalability**: Modular design allows for easy feature additions and API integrations

### Deployment Considerations
- **Performance**: Caching implemented to reduce API calls and improve response times
- **Reliability**: Graceful fallbacks when APIs are unavailable
- **User Experience**: Loading states and error handling for better UX

## Changelog

```
Changelog:
- July 03, 2025. Initial setup
- July 03, 2025. Fixed time period analysis bug showing minutes instead of days
- July 03, 2025. Made OpenSky Network the default data source due to AviationStack limitations
- July 03, 2025. Fixed session state AttributeError for guest mode access
- July 03, 2025. Improved layout to better utilize horizontal space and reduce empty areas
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```