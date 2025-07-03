import json
import os
import pandas as pd
from typing import Dict, List, Optional, Any
import streamlit as st
from google import genai
from google.genai import types

class AIAnalyzer:
    """Handles AI-powered analysis of flight data using Google Gemini"""
    
    def __init__(self):
        # Try to get API key from Streamlit secrets first, then environment variables
        self.gemini_api_key = ""
        
        # Check Streamlit secrets (for cloud deployment)
        if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
            self.gemini_api_key = st.secrets["GEMINI_API_KEY"]
        # Fallback to environment variables (for local development)
        elif "GEMINI_API_KEY" in os.environ:
            self.gemini_api_key = os.environ.get("GEMINI_API_KEY", "")
        
        if self.gemini_api_key:
            self.client = genai.Client(api_key=self.gemini_api_key)
        else:
            self.client = None
            st.warning("Gemini API key not found. AI analysis features will be limited.")
    
    def analyze_flight_data(self, df: pd.DataFrame, analysis_types: List[str]) -> Dict[str, Any]:
        """
        Analyze flight data using AI to extract insights
        
        Args:
            df: Flight data DataFrame
            analysis_types: List of analysis types to perform
            
        Returns:
            Dictionary containing analysis results
        """
        if not self.client:
            return self._generate_basic_analysis(df, analysis_types)
        
        try:
            # Prepare data summary for AI analysis
            data_summary = self._prepare_data_summary(df)
            
            results = {}
            
            # Perform different types of analysis
            if "Route Popularity" in analysis_types:
                results['popular_routes'] = self._analyze_route_popularity(data_summary)
            
            if "Demand Trends" in analysis_types:
                results['demand_patterns'] = self._analyze_demand_trends(data_summary)
            
            if "Peak Hours" in analysis_types:
                results['peak_hours'] = self._analyze_peak_hours(data_summary)
            
            if "Aircraft Types" in analysis_types:
                results['aircraft_analysis'] = self._analyze_aircraft_types(data_summary)
            
            # Generate overall market trends
            results['market_trends'] = self._generate_market_trends(data_summary)
            
            # Generate recommendations
            results['recommendations'] = self._generate_recommendations(data_summary)
            
            # Extract key metrics
            results['key_metrics'] = self._extract_key_metrics(df)
            
            return results
            
        except Exception as e:
            st.error(f"Error in AI analysis: {str(e)}")
            return self._generate_basic_analysis(df, analysis_types)
    
    def _prepare_data_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Prepare a summary of the data for AI analysis"""
        summary = {
            'total_flights': len(df),
            'data_columns': list(df.columns),
            'date_range': {
                'start': df['timestamp'].min().isoformat() if 'timestamp' in df.columns else None,
                'end': df['timestamp'].max().isoformat() if 'timestamp' in df.columns else None
            }
        }
        
        # Add route information if available
        if 'origin' in df.columns and 'destination' in df.columns:
            df['route'] = df['origin'] + ' → ' + df['destination']
            top_routes = df['route'].value_counts().head(10).to_dict()
            summary['top_routes'] = top_routes
        
        # Add country information
        if 'origin_country' in df.columns:
            top_countries = df['origin_country'].value_counts().head(10).to_dict()
            summary['top_countries'] = top_countries
        
        # Add airline information
        if 'airline' in df.columns:
            top_airlines = df['airline'].value_counts().head(10).to_dict()
            summary['top_airlines'] = top_airlines
        
        # Add time-based patterns
        if 'timestamp' in df.columns:
            df['hour'] = df['timestamp'].dt.hour
            hourly_distribution = df['hour'].value_counts().sort_index().to_dict()
            summary['hourly_distribution'] = hourly_distribution
        
        return summary
    
    def _analyze_route_popularity(self, data_summary: Dict[str, Any]) -> str:
        """Analyze route popularity using AI"""
        if not self.client:
            return "AI analysis not available. Please check API key configuration."
        
        try:
            prompt = f"""
            Analyze the following flight route data and provide insights about route popularity:

            Data Summary:
            - Total flights: {data_summary.get('total_flights', 0)}
            - Top routes: {data_summary.get('top_routes', {})}
            - Top countries: {data_summary.get('top_countries', {})}

            Please provide:
            1. Analysis of the most popular routes
            2. Market demand patterns
            3. Geographic distribution insights
            4. Competitive landscape observations
            
            Keep the analysis concise and actionable for a hostel business looking to understand travel patterns.
            """
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "No analysis generated"
            
        except Exception as e:
            return f"Error analyzing route popularity: {str(e)}"
    
    def _analyze_demand_trends(self, data_summary: Dict[str, Any]) -> str:
        """Analyze demand trends using AI"""
        if not self.client:
            return "AI analysis not available. Please check API key configuration."
        
        try:
            prompt = f"""
            Analyze the following flight demand data and identify trends:

            Data Summary:
            - Total flights: {data_summary.get('total_flights', 0)}
            - Date range: {data_summary.get('date_range', {})}
            - Hourly distribution: {data_summary.get('hourly_distribution', {})}
            - Top airlines: {data_summary.get('top_airlines', {})}

            Please provide:
            1. Demand trend analysis
            2. Peak vs off-peak patterns
            3. Seasonal considerations
            4. Market opportunity identification
            
            Focus on actionable insights for hospitality businesses.
            """
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "No analysis generated"
            
        except Exception as e:
            return f"Error analyzing demand trends: {str(e)}"
    
    def _analyze_peak_hours(self, data_summary: Dict[str, Any]) -> str:
        """Analyze peak hours using AI"""
        if not self.client:
            return "Peak hours analysis not available without AI."
        
        try:
            hourly_data = data_summary.get('hourly_distribution', {})
            
            if not hourly_data:
                return "No hourly data available for peak hours analysis."
            
            prompt = f"""
            Analyze the following hourly flight distribution data:

            Hourly Distribution: {hourly_data}

            Please provide:
            1. Identification of peak hours
            2. Low-demand periods
            3. Business implications for hospitality
            4. Recommended strategies based on patterns
            
            Be specific about timing and provide actionable recommendations.
            """
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "No analysis generated"
            
        except Exception as e:
            return f"Error analyzing peak hours: {str(e)}"
    
    def _analyze_aircraft_types(self, data_summary: Dict[str, Any]) -> str:
        """Analyze aircraft types if data is available"""
        if not self.client:
            return "Aircraft analysis not available without AI."
        
        return "Aircraft type analysis requires more detailed flight data. Consider upgrading data sources for comprehensive aircraft insights."
    
    def _generate_market_trends(self, data_summary: Dict[str, Any]) -> str:
        """Generate overall market trends analysis"""
        if not self.client:
            return "Market trends analysis not available without AI."
        
        try:
            prompt = f"""
            Based on the following aviation data, provide a comprehensive market trends analysis:

            Flight Data Summary:
            - Total flights analyzed: {data_summary.get('total_flights', 0)}
            - Geographic coverage: {list(data_summary.get('top_countries', {}).keys())[:5]}
            - Major routes: {list(data_summary.get('top_routes', {}).keys())[:5]}
            - Time period: {data_summary.get('date_range', {})}

            Please provide:
            1. Overall market health assessment
            2. Growth indicators
            3. Competitive landscape
            4. Future outlook
            5. Strategic recommendations for hospitality businesses

            Make it relevant for a hostel chain looking to understand travel patterns.
            """
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "No analysis generated"
            
        except Exception as e:
            return f"Error generating market trends: {str(e)}"
    
    def _generate_recommendations(self, data_summary: Dict[str, Any]) -> str:
        """Generate actionable recommendations"""
        if not self.client:
            return "Recommendations not available without AI."
        
        try:
            prompt = f"""
            Based on the aviation market data analysis, provide specific recommendations for a hostel chain:

            Key Data Points:
            - Flight volume: {data_summary.get('total_flights', 0)} flights analyzed
            - Top destinations: {list(data_summary.get('top_countries', {}).keys())[:3]}
            - Popular routes: {list(data_summary.get('top_routes', {}).keys())[:3]}

            Please provide:
            1. Location strategy recommendations
            2. Pricing optimization suggestions
            3. Marketing timing recommendations
            4. Capacity planning insights
            5. Partnership opportunities

            Make recommendations specific and actionable.
            """
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "No recommendations generated"
            
        except Exception as e:
            return f"Error generating recommendations: {str(e)}"
    
    def _extract_key_metrics(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Extract key metrics from the data"""
        metrics = {}
        
        try:
            # Basic metrics
            metrics['Total Flights'] = len(df)
            
            if 'origin_country' in df.columns:
                metrics['Countries'] = df['origin_country'].nunique()
            
            if 'origin' in df.columns and 'destination' in df.columns:
                metrics['Unique Routes'] = df[['origin', 'destination']].drop_duplicates().shape[0]
            
            if 'airline' in df.columns:
                metrics['Airlines'] = df['airline'].nunique()
            
            # Time-based metrics
            if 'timestamp' in df.columns:
                date_range = (df['timestamp'].max() - df['timestamp'].min()).days
                metrics['Date Range (Days)'] = max(1, date_range)
            
            return metrics
            
        except Exception as e:
            st.error(f"Error extracting metrics: {str(e)}")
            return {'Total Records': len(df)}
    
    def _generate_basic_analysis(self, df: pd.DataFrame, analysis_types: List[str]) -> Dict[str, Any]:
        """Generate basic analysis without AI when API is not available"""
        results = {}
        
        try:
            # Basic route analysis
            if "Route Popularity" in analysis_types and 'origin' in df.columns and 'destination' in df.columns:
                df['route'] = df['origin'] + ' → ' + df['destination']
                top_routes = df['route'].value_counts().head(5)
                results['popular_routes'] = f"Top routes by frequency:\n" + "\n".join([f"• {route}: {count} flights" for route, count in top_routes.items()])
            
            # Basic demand analysis
            if "Demand Trends" in analysis_types:
                total_flights = len(df)
                if 'timestamp' in df.columns:
                    date_range = (df['timestamp'].max() - df['timestamp'].min()).days
                    avg_daily = total_flights / max(1, date_range)
                    results['demand_patterns'] = f"Average daily flights: {avg_daily:.1f}\nTotal flights analyzed: {total_flights}"
                else:
                    results['demand_patterns'] = f"Total flights in dataset: {total_flights}"
            
            # Basic recommendations
            results['recommendations'] = "• Monitor peak travel periods for pricing optimization\n• Focus on popular routes for marketing\n• Consider seasonal variations in demand\n• Analyze competitor presence on key routes"
            
            # Extract key metrics
            results['key_metrics'] = self._extract_key_metrics(df)
            
            return results
            
        except Exception as e:
            return {'error': f"Error in basic analysis: {str(e)}"}
