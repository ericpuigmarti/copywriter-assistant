import os

class Config:
    # Base configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # Fastest default for chat routes; override e.g. OPENAI_CHAT_MODEL=gpt-5.4-mini for heavier tasks
    OPENAI_CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-5.4-nano")
    
    # Environment-specific configurations
    class Development:
        SERVER_URL = "http://localhost:5000"
        DEBUG = True

    class Production:
        SERVER_URL = "https://copywriter-assistant-server.onrender.com/"  # You'll update this later
        DEBUG = False

    @staticmethod
    def get_config():
        if os.getenv('ENVIRONMENT') == 'production':
            return Config.Production
        return Config.Development 