import os

class Config:
    # Base configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Environment-specific configurations
    class Development:
        SERVER_URL = "http://localhost:5000"
        DEBUG = True

    class Production:
        SERVER_URL = "https://your-production-url.onrender.com"  # You'll update this later
        DEBUG = False

    @staticmethod
    def get_config():
        if os.getenv('ENVIRONMENT') == 'production':
            return Config.Production
        return Config.Development 