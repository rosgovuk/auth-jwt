import os
from src.auth import app

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=os.getenv("PORT", "5000"),
        debug=os.getenv("FLASK_DEBUG")
    )
