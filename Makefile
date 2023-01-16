image:
	docker build -t interface-tests .
run-tests: image
	docker run -tv $(shell pwd):/srv interface-tests python3 -m pytest tests.py

