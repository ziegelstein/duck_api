FLASK_ENV=development
FLASK_APP=duckapi.app:create_app
SECRET_KEY=changeme
DATABASE_URI=sqlite:///duckapi.db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://
