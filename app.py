import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
from data_fetcher import DataFetcher
from ai_analyzer import AIAnalyzer
from utils import format_currency, cache_data, get_country_code, validate_api_keys

# Load environment variables from .env file (for local development)
try:
    load_dotenv()
except Exception:
    pass  # Ignore if dotenv fails (e.g., in cloud environment)

# Configure page
st.set_page_config(
    page_title="Airline Market Demand Analytics",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'data_fetcher' not in st.session_state:
    st.session_state.data_fetcher = DataFetcher()
if 'ai_analyzer' not in st.session_state:
    st.session_state.ai_analyzer = AIAnalyzer()
if 'flight_data' not in st.session_state:
    st.session_state.flight_data = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

def main():
    # Custom CSS for better UI
    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #1f77b4, #17a2b8);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .metric-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #1f77b4;
            margin: 0.5rem 0;
        }
        .insight-box {
            background: #e8f4f8;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
            border: 1px solid #bee5eb;
        }
        .status-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .status-online {
            background-color: #28a745;
        }
        .status-offline {
            background-color: #dc3545;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>✈️ Airline Market Demand Analytics</h1>
        <p>Analyze flight data and market trends for your hostel business</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for filters and controls
    with st.sidebar:
        st.header("🎛️ Control Panel")
        
        # API Status section
        st.subheader("📡 System Status")
        api_status = validate_api_keys()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if api_status.get("Gemini"):
                st.markdown('<span class="status-indicator status-online"></span>Gemini AI', unsafe_allow_html=True)
            else:
                st.markdown('<span class="status-indicator status-offline"></span>Gemini AI', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<span class="status-indicator status-online"></span>OpenSky API', unsafe_allow_html=True)
            
        with col3:
            if api_status.get("AviationStack"):
                st.markdown('<span class="status-indicator status-online"></span>AviationStack', unsafe_allow_html=True)
            else:
                st.markdown('<span class="status-indicator status-offline"></span>AviationStack', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Data source selection with enhanced descriptions
        data_source_options = {
            "AviationStack": "🔥 AviationStack (Premium) - Detailed flight schedules & airline data",
            "OpenSky Network": "🌐 OpenSky Network (Free) - Real-time flight positions"
        }
        
        selected_display = st.selectbox(
            "🔗 Select Data Source",
            list(data_source_options.values()),
            index=0,  # Default to AviationStack since we have the API key
            help="Choose your preferred aviation data source"
        )
        
        # Get the actual data source name
        data_source = [k for k, v in data_source_options.items() if v == selected_display][0]
        
        # Geographic filters
        st.subheader("📍 Geographic Filters")
        
        # Country selection with enhanced descriptions
        countries = [
            "Australia", "United States", "United Kingdom", "Germany", 
            "France", "Japan", "Singapore", "Canada", "Netherlands"
        ]
        selected_country = st.selectbox(
            "🌎 Country", 
            countries, 
            index=0,
            help="Select the country to analyze flight data for"
        )
        
        # City/Airport selection based on country
        if selected_country == "Australia":
            airports = {
                "Sydney (SYD)": "YSSY",
                "Melbourne (MEL)": "YMML", 
                "Brisbane (BNE)": "YBBN",
                "Perth (PER)": "YPPH",
                "Adelaide (ADL)": "YPAD"
            }
        else:
            airports = {
                "Major Hub": "AUTO",
                "Secondary Hub": "AUTO2"
            }
        
        selected_airport = st.selectbox(
            "✈️ Airport", 
            list(airports.keys()),
            help="Select the main airport for detailed analysis"
        )
        airport_code = airports[selected_airport]
        
        # Time range selection
        st.subheader("📅 Time Range")
        time_range = st.selectbox(
            "⏰ Analysis Period",
            ["Last 24 Hours", "Last 7 Days", "Last 30 Days"],
            index=1,
            help="Choose the time period for data analysis"
        )
        
        # Analysis type
        st.subheader("🔍 Analysis Type")
        analysis_types = st.multiselect(
            "📊 Select Analysis Types",
            ["Route Popularity", "Demand Trends", "Peak Hours", "Aircraft Types"],
            default=["Route Popularity", "Demand Trends"],
            help="Choose what aspects of flight data to analyze"
        )
        
        # AI Analysis toggle
        use_ai_analysis = st.checkbox(
            "🤖 Enable AI Insights", 
            value=True,
            help="Use AI to generate intelligent insights and recommendations"
        )
        
        # Fetch data button
        st.markdown("---")
        if st.button("🚀 Fetch & Analyze Data", type="primary", use_container_width=True):
            fetch_and_analyze_data(data_source, selected_country, airport_code, time_range, analysis_types, use_ai_analysis)
        
        # Quick info section
        st.markdown("---")
        st.subheader("ℹ️ Quick Info")
        st.info(
            "**Available Data Sources:**\n"
            "• AviationStack: Detailed flight schedules & airline info\n"
            "• OpenSky Network: Real-time global flight positions\n\n"
            "**Time Period Analysis:**\n"
            "• Current flight data is distributed across selected timeframe\n"
            "• Provides realistic market analysis patterns\n\n"
            "**Gemini AI Analysis provides:**\n"
            "• Market trend insights\n"
            "• Route popularity analysis\n"
            "• Peak hour analysis\n"
            "• Business recommendations for hostels"
        )
    
    # Main content area with enhanced layout
    if st.session_state.flight_data is not None:
        # Data overview section
        st.subheader("📊 Market Demand Overview")
        display_data_overview()
        
        # Two-column layout for charts and insights
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("📈 Data Visualizations")
            display_visualizations()
        
        with col2:
            st.subheader("🤖 AI Insights")
            if st.session_state.analysis_results is not None:
                display_ai_insights()
            else:
                st.info("AI insights will appear here after data analysis.")
    else:
        # Welcome section with improved styling
        st.markdown("""
        <div class="insight-box">
            <h3>🚀 Welcome to Airline Market Demand Analytics</h3>
            <p>This application helps you analyze flight data and market trends to make informed decisions for your hostel business.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature highlights
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>📊 Real-time Data</h4>
                <p>Access live flight data from global aviation networks</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>🤖 AI Analysis</h4>
                <p>Gemini AI provides intelligent insights and recommendations</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <h4>📈 Market Trends</h4>
                <p>Understand demand patterns and popular routes</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Getting started guide
        st.markdown("---")
        st.subheader("🎯 How to Get Started")
        
        step_col1, step_col2 = st.columns(2)
        
        with step_col1:
            st.markdown("""
            **Step 1: Configure Data Source**
            - Choose between OpenSky Network (free) or AviationStack
            - Select your target country and airport
            - Pick your analysis time period
            """)
            
        with step_col2:
            st.markdown("""
            **Step 2: Analyze & Insights**
            - Select analysis types (routes, trends, peak hours)
            - Enable AI insights for smart recommendations
            - Click "Fetch & Analyze Data" to start
            """)
        
        # Sample data preview
        st.markdown("---")
        st.subheader("💡 What You'll See")
        st.markdown("""
        Once you fetch data, you'll get:
        - **Interactive charts** showing flight routes and demand patterns
        - **AI-powered insights** about market trends and opportunities
        - **Actionable recommendations** for your hostel business
        - **Exportable data** for further analysis
        """)
            
    # Bottom section for detailed data
    if st.session_state.flight_data is not None:
        st.markdown("---")
        st.subheader("📋 Detailed Flight Data")
        
        # Data table with filtering
        if not st.session_state.flight_data.empty:
            # Add filters for the data table
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if 'origin' in st.session_state.flight_data.columns:
                    origin_filter = st.multiselect(
                        "Filter by Origin",
                        options=st.session_state.flight_data['origin'].unique(),
                        default=st.session_state.flight_data['origin'].unique()[:5]
                    )
                else:
                    origin_filter = []
            
            with col2:
                if 'destination' in st.session_state.flight_data.columns:
                    dest_filter = st.multiselect(
                        "Filter by Destination", 
                        options=st.session_state.flight_data['destination'].unique(),
                        default=st.session_state.flight_data['destination'].unique()[:5]
                    )
                else:
                    dest_filter = []
            
            with col3:
                show_rows = st.number_input("Rows to show", min_value=10, max_value=1000, value=50)
            
            # Apply filters
            filtered_data = st.session_state.flight_data.copy()
            if origin_filter and 'origin' in filtered_data.columns:
                filtered_data = filtered_data[filtered_data['origin'].isin(origin_filter)]
            if dest_filter and 'destination' in filtered_data.columns:
                filtered_data = filtered_data[filtered_data['destination'].isin(dest_filter)]
            
            # Display data
            st.dataframe(
                filtered_data.head(show_rows),
                use_container_width=True,
                hide_index=True
            )
            
            # Export functionality
            if st.button("📥 Export Data to CSV"):
                csv = filtered_data.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f"flight_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )

def fetch_and_analyze_data(data_source, country, airport_code, time_range, analysis_types, use_ai_analysis):
    """Fetch and analyze aviation data"""
    
    with st.spinner("🔄 Fetching flight data..."):
        try:
            # Fetch flight data
            if data_source == "OpenSky Network":
                flight_data = st.session_state.data_fetcher.fetch_opensky_data(
                    country=country,
                    time_range=time_range
                )
            else:
                flight_data = st.session_state.data_fetcher.fetch_aviationstack_data(
                    country=country,
                    airport_code=airport_code,
                    time_range=time_range
                )
            
            if flight_data is not None and not flight_data.empty:
                st.session_state.flight_data = flight_data
                st.success(f"✅ Successfully fetched {len(flight_data)} flight records!")
                
                # Perform AI analysis if enabled
                if use_ai_analysis:
                    with st.spinner("🤖 Analyzing data with AI..."):
                        analysis_results = st.session_state.ai_analyzer.analyze_flight_data(
                            flight_data, analysis_types
                        )
                        st.session_state.analysis_results = analysis_results
                        if analysis_results:
                            st.success("🎯 AI analysis completed!")
                
                # Auto-refresh the page to show new data
                st.rerun()
            else:
                st.error("❌ No flight data found for the selected criteria. Please try different filters.")
                
        except Exception as e:
            st.error(f"❌ Error fetching data: {str(e)}")
            st.error("Please check your API keys and try again.")

def display_data_overview():
    """Display overview statistics of the flight data"""
    
    if st.session_state.flight_data is None or st.session_state.flight_data.empty:
        return
    
    data = st.session_state.flight_data
    
    # Key metrics with enhanced styling
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_flights = len(data)
        st.metric("Total Flights", total_flights, delta=None)
    
    with col2:
        if 'origin' in data.columns:
            unique_origins = data['origin'].nunique()
            st.metric("Unique Origins", unique_origins)
        else:
            unique_aircraft = data['callsign'].nunique() if 'callsign' in data.columns else 0
            st.metric("Active Aircraft", unique_aircraft)
    
    with col3:
        if 'destination' in data.columns:
            unique_destinations = data['destination'].nunique()
            st.metric("Unique Destinations", unique_destinations)
        else:
            unique_countries = data['origin_country'].nunique() if 'origin_country' in data.columns else 0
            st.metric("Countries", unique_countries)
    
    with col4:
        if 'airline' in data.columns:
            unique_airlines = data['airline'].nunique()
            st.metric("Airlines", unique_airlines)
        else:
            st.metric("Data Points", len(data))
    
    # Additional metrics row
    if 'timestamp' in data.columns:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            date_range = (data['timestamp'].max() - data['timestamp'].min()).days
            st.metric("Date Range", f"{date_range} days")
        
        with col2:
            avg_per_day = len(data) / max(1, date_range)
            st.metric("Avg Daily Flights", f"{avg_per_day:.1f}")
        
        with col3:
            peak_hour = data['timestamp'].dt.hour.mode().iloc[0] if not data['timestamp'].dt.hour.empty else 0
            st.metric("Peak Hour", f"{peak_hour}:00")
        
        with col4:
            if 'velocity' in data.columns:
                avg_speed = data['velocity'].mean() * 2.237 if data['velocity'].notna().any() else 0
                st.metric("Avg Speed", f"{avg_speed:.0f} mph")

def display_visualizations():
    """Display interactive visualizations"""
    
    if st.session_state.flight_data is None or st.session_state.flight_data.empty:
        return
    
    data = st.session_state.flight_data
    
    # Route popularity chart
    if 'origin' in data.columns and 'destination' in data.columns:
        st.subheader("🗺️ Most Popular Routes")
        
        # Create route combinations
        data['route'] = data['origin'] + ' → ' + data['destination']
        route_counts = data['route'].value_counts().head(10)
        
        fig_routes = px.bar(
            x=route_counts.values,
            y=route_counts.index,
            orientation='h',
            labels={'x': 'Number of Flights', 'y': 'Route'},
            title="Top 10 Flight Routes"
        )
        fig_routes.update_layout(height=400)
        st.plotly_chart(fig_routes, use_container_width=True)
    
    # Time-based analysis
    if 'timestamp' in data.columns:
        st.subheader("⏰ Flight Activity Over Time")
        
        # Convert timestamp to datetime if it's not already
        if not pd.api.types.is_datetime64_any_dtype(data['timestamp']):
            data['timestamp'] = pd.to_datetime(data['timestamp'])
        
        # Group by hour
        data['hour'] = data['timestamp'].dt.hour
        hourly_counts = data.groupby('hour').size().reset_index(name='flight_count')
        
        fig_time = px.line(
            hourly_counts,
            x='hour',
            y='flight_count',
            title="Flight Activity by Hour of Day",
            labels={'hour': 'Hour of Day', 'flight_count': 'Number of Flights'}
        )
        fig_time.update_layout(height=300)
        st.plotly_chart(fig_time, use_container_width=True)
    
    # Geographic distribution
    if 'origin_country' in data.columns:
        st.subheader("🌍 Geographic Distribution")
        
        country_counts = data['origin_country'].value_counts().head(10)
        
        fig_geo = px.pie(
            values=country_counts.values,
            names=country_counts.index,
            title="Flights by Origin Country"
        )
        fig_geo.update_layout(height=400)
        st.plotly_chart(fig_geo, use_container_width=True)
    
    # Airline distribution
    if 'airline' in data.columns:
        st.subheader("🛫 Airline Market Share")
        
        airline_counts = data['airline'].value_counts().head(8)
        
        fig_airlines = px.bar(
            x=airline_counts.index,
            y=airline_counts.values,
            title="Flights by Airline",
            labels={'x': 'Airline', 'y': 'Number of Flights'}
        )
        fig_airlines.update_layout(height=300)
        st.plotly_chart(fig_airlines, use_container_width=True)

def display_ai_insights():
    """Display AI-generated insights"""
    
    if st.session_state.analysis_results is None:
        return
    
    results = st.session_state.analysis_results
    
    # Market trends with enhanced styling
    if 'market_trends' in results:
        st.markdown("""
        <div class="insight-box">
            <h4>📈 Market Trends</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(results['market_trends'])
    
    # Popular routes insights
    if 'popular_routes' in results:
        st.markdown("""
        <div class="insight-box">
            <h4>🎯 Route Insights</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(results['popular_routes'])
    
    # Demand patterns
    if 'demand_patterns' in results:
        st.markdown("""
        <div class="insight-box">
            <h4>⚡ Demand Patterns</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(results['demand_patterns'])
    
    # Peak hours analysis
    if 'peak_hours' in results:
        st.markdown("""
        <div class="insight-box">
            <h4>⏰ Peak Hours Analysis</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(results['peak_hours'])
    
    # Recommendations with special styling
    if 'recommendations' in results:
        st.markdown("""
        <div class="insight-box" style="border-left: 4px solid #28a745;">
            <h4>💡 Business Recommendations</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write(results['recommendations'])
    
    # Key insights as metrics
    if 'key_metrics' in results:
        st.markdown("---")
        st.subheader("🔑 Key Insights")
        
        metrics = results['key_metrics']
        if isinstance(metrics, dict):
            # Display metrics in a more organized way
            metric_items = list(metrics.items())
            if len(metric_items) <= 4:
                cols = st.columns(len(metric_items))
                for i, (key, value) in enumerate(metric_items):
                    with cols[i]:
                        st.metric(key, value)
            else:
                # Split into rows if more than 4 metrics
                for i in range(0, len(metric_items), 4):
                    chunk = metric_items[i:i+4]
                    cols = st.columns(len(chunk))
                    for j, (key, value) in enumerate(chunk):
                        with cols[j]:
                            st.metric(key, value)
    
    # Footer section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
        <h4>🏨 Airline Market Demand Analytics</h4>
        <p>Helping hostel businesses make data-driven decisions through aviation market analysis</p>
        <p style="color: #666; font-size: 0.9em;">
            Data Sources: OpenSky Network • AviationStack | AI Analysis: Google Gemini
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
