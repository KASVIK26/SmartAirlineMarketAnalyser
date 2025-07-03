#!/usr/bin/env python3
"""
Setup script to install dependencies and configure the Smart Airline Market Analyzer
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    try:
        # Install using uv (faster package manager)
        subprocess.run([sys.executable, "-m", "uv", "pip", "install", "-e", "."], check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error installing dependencies with uv, trying pip...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True)
            print("✅ Dependencies installed successfully with pip!")
        except subprocess.CalledProcessError:
            print("❌ Error installing dependencies. Please install manually.")
            return False
    return True

def check_env_file():
    """Check if .env file exists and has required keys"""
    env_file = ".env"
    if not os.path.exists(env_file):
        print(f"❌ {env_file} file not found!")
        return False
    
    with open(env_file, 'r') as f:
        content = f.read()
        
    required_keys = ["GEMINI_API_KEY", "AVIATIONSTACK_API_KEY"]
    missing_keys = []
    
    for key in required_keys:
        if f"{key}=your_" in content or f"{key}=" not in content:
            missing_keys.append(key)
    
    if missing_keys:
        print(f"⚠️  Please update your {env_file} file with actual API keys:")
        for key in missing_keys:
            print(f"   - {key}")
        return False
    
    print("✅ API keys configured in .env file!")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Smart Airline Market Analyzer...")
    print("-" * 50)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check environment file
    if not check_env_file():
        print("\n📝 Next steps:")
        print("1. Edit the .env file and add your API keys")
        print("2. Get Gemini API key from: https://makersuite.google.com/app/apikey")
        print("3. Get AviationStack API key from: https://aviationstack.com/dashboard")
        print("4. Run: streamlit run app.py")
    else:
        print("\n🎉 Setup complete! You can now run the application:")
        print("   streamlit run app.py")

if __name__ == "__main__":
    main()
