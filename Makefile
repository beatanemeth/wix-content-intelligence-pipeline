# .PHONY ensures these run even if a file with the same name exists
.PHONY: help docker-start docker-stop build-jwt up-jwt build-jup up-jup \
        token-jup down rmi-jwt rmi-jup rmi-all clear clear-all lint
		
# Default target when you just type 'make'
help:
	@echo "Available commands:"
	@echo "  docker-start   : Start Docker Desktop"
	@echo "  docker-stop    : Stop Docker Desktop"
	@echo "  build-jwt      : Build JWT microservice image"
	@echo "  up-jwt         : Spin up JWT container"
	@echo "  build-jup      : Build Jupyter image"
	@echo "  up-jup         : Spin up Jupyter container"
	@echo "  token-jup      : Get the Jupyter login token"
	@echo "  down           : Stop and remove all containers"
	@echo "  rmi-jwt        : Remove JWT microservice images"
	@echo "  rmi-jup        : Remove Jupyter images"
	@echo "  rmi-all        : Remove both service images"
	@echo "  clear          : Remove outputs from a specific .ipynb file"
	@echo "  clear-all      : Remove outputs from all .ipynb files"
	@echo "  lint           : Run pre-commit checks on all files"

	@echo ""
	@echo "Usage example    : make up-jup"

docker-start:
	docker desktop start

docker-stop:
	docker desktop stop

build-jwt:
	docker compose build jwt_microservice

up-jwt:
	docker compose up -d jwt_microservice

build-jup:
	docker compose build jupyter

up-jup:
	docker compose up -d jupyter

token-jup:
	docker compose logs jupyter

down:
	docker compose down

rmi-jwt:
	docker rmi jwt_microservice

rmi-jup:
	docker rmi jupyter

rmi-all: rmi-jwt rmi-jup

# Usage: make clear FILE=./ETL/1_notebook.ipynb OR make clear ./ETL/1_notebook.ipynb
clear:
	@$(eval FILE_TO_STRIP=$(if $(FILE),$(FILE),$(filter-out $@,$(MAKECMDGOALS))))
	@if [ -z "$(FILE_TO_STRIP)" ]; then \
		echo "ERROR: Please specify a file, e.g., make clear FILE=analysis.ipynb or make clear analysis.ipynb"; \
		exit 1; \
	fi
	@nbstripout $(FILE_TO_STRIP)
	@echo "✓ Stripout complete for: $(FILE_TO_STRIP)"

# This trick allows passing arbitrary arguments to make without it complaining about unknown targets
%:
	@:

clear-all:
	@find . -name "*.ipynb" -not -path "*/.*" -exec nbstripout {} +
	@echo "✓ All notebooks in project have been stripped."

lint:
	pre-commit run --all-files

