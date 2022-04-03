PAYMENT_PORT ?= 8080
INVENTORY_PORT ?= 8081
HOST ?= "0.0.0.0"

## start_payment: starts the payment microservice with a default port 8080
start_payment:
	uvicorn payment.main:app \
		--reload \
		--reload-dir payment/ \
		--port $(PAYMENT_PORT) \
		--host $(HOST)

## start_inventory: starts the inventory microservice with a default port 8081
start_inventory:
	uvicorn inventory.main:app \
		--reload \
		--reload-dir inventory/ \
		--port $(INVENTORY_PORT) \
		--host $(HOST)

## start_consumer: start listening to a consumer of the redis stream
CWD = $(pwd)
start_consumer:
	PYTHONPATH=/Users/bolajide/workspace/fastapi-microservices/inventory python inventory/consumer.py

## :
## help: Print out available make targets.
help: Makefile
	@echo
	@echo " Choose a command run:"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo
