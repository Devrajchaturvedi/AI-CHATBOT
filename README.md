ai-chatbot/
│
├── app/                          # Core application package
│   ├── __init__.py              # Initializes Flask app and extensions
│   ├── routes.py                # Defines Flask routes and handles chatbot requests
│   ├── chatbot.py               # Main chatbot logic (rule-based or AI-driven)
│   ├── static/                  # Static assets (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css        # Custom styling for UI
│   │   ├── js/
│   │   │   └── script.js        # Frontend logic (AJAX calls, DOM handling)
│   └── templates/
│       └── index.html           # Main HTML interface
│
├── .env                         # Environment variables (keep secret, not tracked in Git)
├── .gitignore                   # Specifies files/folders to ignore in version control
├── Procfile                     # For deploying on Heroku
├── requirements.txt             # Python package dependencies
├── runtime.txt                  # Specifies Python version (optional, used by Heroku)
├── app.py                       # Development entry point (runs the Flask app)
├── config.py                    # (Optional) Centralized config for environments/settings
├── README.md                    # Project overview and setup instructions
└── wsgi.py                      # Production entry point (used by Gunicorn)
