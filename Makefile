PAYMENT_PORT ?= 8080
INVENTORY_PORT ?= 8081
HOST ?= "0.0.0.0"

start_payment:
	uvicorn payment.main:app \
		--reload \
		--reload-dir payment/ \
		--port $(PAYMENT_PORT) \
		--host $(HOST)

start_inventory:
	uvicorn inventory.main:app \
		--reload \
		--reload-dir inventory/ \
		--port $(INVENTORY_PORT) \
		--host $(HOST)
