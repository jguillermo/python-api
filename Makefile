.DEFAULT_GOAL := help

## GENERAL ##
OWNER 			= getmin
SERVICE_NAME 	= demoapi
PATH_PREFIX 	= "/v1"

## DEPLOY ##
ENV 			?= dev
version 		?= 1.0.0.1


## RESULT_VARS ##
export PROJECT_NAME	      = $(OWNER)-$(SERVICE_NAME)
export CONTAINER_NAME 	  = $(PROJECT_NAME)_backend
export CONTAINER_DB_NAME  = $(PROJECT_NAME)_db
export IMAGE_DEV		  = $(PROJECT_NAME):dev
export IMAGE_RAML         = $(PROJECT_NAME)_raml:1.0


## Target Commons ##

install: ## build image to dev: make build
	make build
	docker build -f container/doc/Dockerfile -t $(IMAGE_RAML) container/doc/

build: ## build image to dev: make build
	cp app/requirements.txt container/dev/resources/requirements.txt
	docker build -f container/dev/Dockerfile -t $(IMAGE_DEV) container/dev/
	rm -f container/dev/resources/requirements.txt



up: ## up docker containers: make up
	make set-config-local
	docker-compose -f container/docker-compose.yml up -d
	@make status

start: ## up docker containers: make up
	make up

down: ## Stops and removes the docker containers: make down
	docker-compose -f container/docker-compose.yml down

status: ## Show containers status: make status
	docker-compose -f container/docker-compose.yml ps

stop: ## Stops and removes the docker containers, use me with: make down
	docker-compose -f container/docker-compose.yml stop

restart: ## Restart all containers, use me with: make restart
	make down
	make start
	make status

ssh: ## Connect to container for ssh protocol : make ssh
	docker exec -it $(CONTAINER_NAME) bash

set-config-local: ## copia el archivo config/env.local al config : make set-config-local
	#cp ${PWD}/app/config/config.env.local ${PWD}/app/config/config.env
	mkdir -p ${PWD}/app/files && chmod 777 ${PWD}/app/files

log: ## Show container logs make : make log
	docker-compose -f container/docker-compose.yml logs -f

log-backend: ## Show container logs make : make log
	docker-compose -f container/docker-compose.yml logs -f backend

install-lib: ## Connect to container for ssh protocol install with pip: make install-lib
	docker exec -it $(CONTAINER_NAME) pip-3.5 install $(LIB)

tests: ## Run the unitTests : make tests
	@docker run --rm -t -v $(PWD)/app:/app:rw --entrypoint /resources/test.sh $(IMAGE_DEV)
	#@sudo chown -R $(USER):$(USER) $(PWD)/app/*


## Documentacion##
raml-generate: ## build image to raml: make build-raml
	#docker build -f container/doc/Dockerfile -t $(IMAGE_RAML) container/doc/
	docker run --rm -v $(PWD):/app $(IMAGE_RAML) -i /app/doc/gamma/api.raml -o /app/app/doc/gamma.html
	docker run --rm -v $(PWD):/app $(IMAGE_RAML) --theme raml2html-markdown-theme -i /app/doc/gamma/api.raml -o /app/DOC.md

raml-live: ## build image to raml: make raml-live
	#docker rm -f api-designer
	docker run -d --name api-designer -v $(PWD)/doc:/raml -p 3000:3000 loostro/api-designer:0.3.2
	open http://localhost:3000/


## Migrate DB##
migrate: ## Execute migrate : make migrate
	docker exec $(CONTAINER_NAME) /resources/alembic.sh upgrade head

migrate-info: ## Execute migrate : make migrate
	docker exec $(CONTAINER_NAME) /resources/alembic.sh upgrade head --sql

revision: ## Create a new revision : make revision
	docker exec $(CONTAINER_NAME) /resources/alembic.sh revision --autogenerate -m "migrate"
	#@sudo chown -R $(USER) $(PWD)/app/alembic/versions

dump: ## Execute migrate : make migrate
	docker exec $(CONTAINER_DB_NAME) /tmp/dump.sh


## Docker help ##
docker-kill: ## Execute migrate : make migrate
	docker rm -f $$(docker ps -aq)

docker-stats: ## Show container logs make : make stats
	docker stats $(CONTAINER_NAME)

## UPLOAD-DEPLOY ##
build-deploy: ## Generate image to aws deploy : make build-deploy
	docker build -f container/latest/Dockerfile --no-cache --build-arg IMAGE=$(IMAGE_DEV) -t $(IMAGE_DEPLOY) .


## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
