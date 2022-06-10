from duckapi.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("duckapi.tasks.example",)
