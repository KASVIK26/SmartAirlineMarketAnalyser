import streamlit as st
import pandas as pd
from typing import Any, Dict, Optional
import time
from datetime import datetime, timedelta

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format currency values for display"""
    try:
        if currency == "USD":
            return f"${amount:,.2f}"
        elif currency == "EUR":
            return f"€{amount:,.2f}"
        elif currency == "GBP":
            return f"£{amount:,.2f}"
        elif currency == "AUD":
            return f"A${amount:,.2f}"
        else:
            return f"{amount:,.2f} {currency}"
    except:
        return str(amount)

def cache_data(func):
    """Decorator for caching data with TTL"""
    cache = {}
    cache_time = {}
    
    def wrapper(*args, **kwargs):
        # Create cache key
        key = str(args) + str(sorted(kwargs.items()))
        
        # Check if data is in cache and not expired
        if key in cache and key in cache_time:
            if time.time() - cache_time[key] < 300:  # 5 minutes TTL
                return cache[key]
        
        # Execute function and cache result
        result = func(*args, **kwargs)
        cache[key] = result
        cache_time[key] = time.time()
        
        return result
    
    return wrapper

def get_country_code(country_name: str) -> str:
    """Get country code from country name"""
    country_codes = {
        "Australia": "AU",
        "United States": "US",
        "United Kingdom": "GB",
        "Germany": "DE",
        "France": "FR",
        "Japan": "JP",
        "Singapore": "SG",
        "Canada": "CA",
        "Netherlands": "NL",
        "Italy": "IT",
        "Spain": "ES",
        "Sweden": "SE",
        "Norway": "NO",
        "Denmark": "DK",
        "Finland": "FI"
    }
    return country_codes.get(country_name, "XX")

def validate_api_keys() -> Dict[str, bool]:
    """Validate that required API keys are available"""
    import os
    
    keys_status = {
        "OpenAI": bool(os.environ.get("OPENAI_API_KEY")),
        "AviationStack": bool(os.environ.get("AVIATIONSTACK_API_KEY")),
        "Gemini": bool(os.environ.get("GEMINI_API_KEY"))
    }
    
    return keys_status

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safely divide two numbers, avoiding division by zero"""
    try:
        if denominator == 0:
            return default
        return numerator / denominator
    except:
        return default

def format_large_number(num: int) -> str:
    """Format large numbers with appropriate suffixes"""
    try:
        if num >= 1_000_000:
            return f"{num/1_000_000:.1f}M"
        elif num >= 1_000:
            return f"{num/1_000:.1f}K"
        else:
            return str(num)
    except:
        return str(num)

def get_time_range_dates(time_range: str) -> tuple:
    """Get start and end dates for a time range"""
    end_date = datetime.now()
    
    if time_range == "Last 24 Hours":
        start_date = end_date - timedelta(hours=24)
    elif time_range == "Last 7 Days":
        start_date = end_date - timedelta(days=7)
    elif time_range == "Last 30 Days":
        start_date = end_date - timedelta(days=30)
    else:
        start_date = end_date - timedelta(days=1)
    
    return start_date, end_date

def display_api_status():
    """Display API status in sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔧 API Status")
    
    api_status = validate_api_keys()
    
    for api_name, is_available in api_status.items():
        if is_available:
            st.sidebar.success(f"✅ {api_name} API")
        else:
            st.sidebar.error(f"❌ {api_name} API")
    
    if not any(api_status.values()):
        st.sidebar.warning("⚠️ No API keys configured. Some features may be limited.")

def create_download_link(df: pd.DataFrame, filename: str) -> str:
    """Create a download link for DataFrame"""
    try:
        csv = df.to_csv(index=False)
        return csv
    except Exception as e:
        st.error(f"Error creating download link: {str(e)}")
        return ""

def format_percentage(value: float, decimals: int = 1) -> str:
    """Format percentage values"""
    try:
        return f"{value:.{decimals}f}%"
    except:
        return "0.0%"

def clean_flight_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize flight data"""
    if df.empty:
        return df
    
    try:
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Clean string columns
        string_columns = df.select_dtypes(include=['object']).columns
        for col in string_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
                df[col] = df[col].replace('nan', '')
        
        # Clean numeric columns
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Sort by timestamp if available
        if 'timestamp' in df.columns:
            df = df.sort_values('timestamp', ascending=False)
        
        return df
        
    except Exception as e:
        st.error(f"Error cleaning data: {str(e)}")
        return df

def get_system_info() -> Dict[str, Any]:
    """Get system information for debugging"""
    import platform
    import sys
    
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "timestamp": datetime.now().isoformat()
    }

@st.cache_data(ttl=300)
def cached_api_call(func, *args, **kwargs):
    """Generic cached API call wrapper"""
    return func(*args, **kwargs)

def handle_api_error(func):
    """Decorator to handle API errors gracefully"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            st.error(f"API Error: {str(e)}")
            return None
    return wrapper

def create_summary_stats(df: pd.DataFrame) -> Dict[str, Any]:
    """Create summary statistics for the dataset"""
    if df.empty:
        return {}
    
    try:
        stats = {
            'total_records': len(df),
            'columns': list(df.columns),
            'missing_data': df.isnull().sum().to_dict(),
            'data_types': df.dtypes.to_dict()
        }
        
        # Add time-based stats if timestamp exists
        if 'timestamp' in df.columns:
            stats['date_range'] = {
                'start': df['timestamp'].min(),
                'end': df['timestamp'].max(),
                'days': (df['timestamp'].max() - df['timestamp'].min()).days
            }
        
        return stats
        
    except Exception as e:
        st.error(f"Error creating summary stats: {str(e)}")
        return {}
