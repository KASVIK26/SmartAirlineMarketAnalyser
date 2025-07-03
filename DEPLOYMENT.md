# 🚀 Deployment Guide for Smart Airline Market Analyzer

## Option 1: Streamlit Community Cloud (Recommended - FREE)

### Prerequisites:
- GitHub account
- Your code pushed to a GitHub repository

### Step-by-Step Instructions:

#### 1. **Push Your Code to GitHub**
```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit - Smart Airline Market Analyzer"

# Add your GitHub repository as origin
git remote add origin https://github.com/YOUR_USERNAME/SmartAirlineMarketAnalyser.git

# Push to GitHub
git push -u origin main
```

#### 2. **Deploy to Streamlit Community Cloud**
1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your GitHub repository: `SmartAirlineMarketAnalyser`
5. Choose the main branch
6. Set main file path: `app.py`
7. Click "Deploy!"

#### 3. **Configure Your API Keys**
1. Once deployed, go to your app settings (gear icon)
2. Click on "Secrets"
3. Paste your API keys in this format:
```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
AVIATIONSTACK_API_KEY = "your_actual_aviationstack_api_key_here"
```
4. Click "Save"

#### 4. **Your App is Live!**
- Your app will be available at: `https://your-app-name.streamlit.app`
- It will automatically update when you push changes to GitHub

---

## Option 2: Railway (Alternative - FREE Tier)

### Steps:
1. Go to [railway.app](https://railway.app/)
2. Sign up with GitHub
3. Click "New Project" > "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect it's a Python app
6. Add environment variables in Railway dashboard:
   - `GEMINI_API_KEY`: your Gemini API key
   - `AVIATIONSTACK_API_KEY`: your AviationStack API key
7. Deploy!

---

## Option 3: Render (Alternative - FREE Tier)

### Steps:
1. Go to [render.com](https://render.com/)
2. Sign up with GitHub
3. Click "New" > "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.headless true`
6. Add environment variables:
   - `GEMINI_API_KEY`: your Gemini API key
   - `AVIATIONSTACK_API_KEY`: your AviationStack API key
7. Deploy!

---

## 🔧 Files Created for Deployment:

1. **`requirements.txt`** - Lists all Python dependencies
2. **`streamlit_app.py`** - Deployment configuration file
3. **`.streamlit/secrets.toml`** - Template for API keys (don't commit this)

## 🔒 Security Notes:

- ✅ `.env` file is in `.gitignore` (won't be committed)
- ✅ `secrets.toml` is in `.gitignore` (won't be committed)
- ✅ API keys are stored securely in deployment platform
- ✅ Never commit API keys to GitHub

## 📝 Deployment Checklist:

- [ ] Code pushed to GitHub
- [ ] `requirements.txt` created
- [ ] API keys configured in deployment platform
- [ ] App deployed and accessible
- [ ] All features working correctly

## 🎯 Recommended: Streamlit Community Cloud

**Why Streamlit Community Cloud is the best choice:**
- ✅ **Free**: No cost for public apps
- ✅ **Easy**: Built specifically for Streamlit
- ✅ **Automatic**: Updates when you push to GitHub
- ✅ **Secure**: Proper secrets management
- ✅ **Fast**: Optimized for Streamlit apps

## 🆘 Troubleshooting:

**Common Issues:**
1. **Import errors**: Check `requirements.txt` has all dependencies
2. **API key errors**: Verify keys are set correctly in secrets
3. **Port errors**: Streamlit Community Cloud handles this automatically
4. **File not found**: Make sure `app.py` is in the repository root

**Need Help?**
- Streamlit Community Cloud: [docs.streamlit.io](https://docs.streamlit.io/)
- Railway: [docs.railway.app](https://docs.railway.app/)
- Render: [render.com/docs](https://render.com/docs)

---

**🎉 Your Smart Airline Market Analyzer will be live and accessible worldwide once deployed!**
