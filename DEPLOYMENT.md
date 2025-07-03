# Streamlit Cloud Deployment Guide

## Steps to Deploy on Streamlit Cloud

1. **Repository Setup**
   - Push your code to GitHub
   - Make sure all files are committed

2. **Streamlit Cloud Configuration**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - **Main file path**: Use `streamlit_app.py` (recommended) or `main.py`

3. **Environment Variables (Secrets)**
   Add these secrets in Streamlit Cloud settings:
   ```toml
   [secrets]
   GEMINI_API_KEY = "your_gemini_api_key_here"
   AVIATIONSTACK_API_KEY = "your_aviationstack_api_key_here"
   ```

4. **Dependencies**
   - The app will automatically install dependencies from `pyproject.toml`
   - All required packages are already configured

## Troubleshooting

If you encounter port connection errors:
- Use `streamlit_app.py` as the main file path
- Don't specify custom ports in Streamlit Cloud
- The `.streamlit/config.toml` has been configured for cloud deployment

## Files Created for Deployment
- `streamlit_app.py` - Main entry point for Streamlit Cloud
- `main.py` - Alternative entry point
- `.streamlit/config.toml` - Streamlit configuration (cloud-ready)
- `DEPLOYMENT.md` - This deployment guide