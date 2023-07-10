start:
	poetry run flask --app routes run --port 8000

start-debug:
	poetry run flask --app routes --debug run --port 8000