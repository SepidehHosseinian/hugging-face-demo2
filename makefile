install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_app.py

format:
	black *.py

run:
	python app.py

run-uvicorn:
	uvicorn app:app --reload

killweb:
	sudo killall uvicorn

lint:
	pylint --disable=R,C app.py

all: install lint test