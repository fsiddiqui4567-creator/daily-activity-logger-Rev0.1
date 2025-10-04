from app import app
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(debug=True, host='0.0.0.0', port=port)  # Bind to 0.0.0.0 for Render
