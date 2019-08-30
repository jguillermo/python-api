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
	docker build -f container/dev/Dockerfile -t $(IMAGE_DEV) .


up: ## up docker containers: make up
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





log: ## Show container logs make : make log
	docker-compose -f container/docker-compose.yml logs -f

log-backend: ## Show container logs make : make log
	docker-compose -f container/docker-compose.yml logs -f backend



tests: ## Run the unitTests : make tests
	@docker run --rm -t -v $(PWD)/application:/application:rw --entrypoint /resources/test.sh $(IMAGE_DEV)


## Documentacion##
raml-generate: ## build image to raml: make build-raml
	#docker build -f container/doc/Dockerfile -t $(IMAGE_RAML) container/doc/
	docker run --rm -v $(PWD):/application $(IMAGE_RAML) -i /application/doc/gamma/api.raml -o /application/application/doc/gamma.html
	docker run --rm -v $(PWD):/application $(IMAGE_RAML) --theme raml2html-markdown-theme -i /application/doc/gamma/api.raml -o /application/DOC.md

raml-live: ## build image to raml: make raml-live
	#docker rm -f api-designer
	docker run -d --name api-designer -v $(PWD)/doc:/raml -p 3000:3000 loostro/api-designer:0.3.2
	open http://localhost:3000/

## Console Backend DB##
console: ## Connect to container for ssh protocol : make console a='pwd'
	docker exec -it $(CONTAINER_NAME) ${a}

ssh: ## Connect to container for ssh protocol : make ssh
	make console a='bash'

install-lib: ## Connect to container for ssh protocol install with pip: make install-lib
	make console a='pip install $(LIB)'

freeze: ## Connect to container for ssh protocol install with pip: make install-lib
	make console a='pip freeze'

## Migrate DB##
db-upgrade: ## Execute migrate db : make db-upgrade
	make console a='flask db upgrade'

db-upgrade-info: ## show history changes : make db-upgrade-info
	make console a='flask db upgrade head --sql'

db-migrate: ## Create a new migrate : make revision
	make console a='flask db migrate'

db-revision: ## Create a new revision. file empty : make revision
	make console a='flask db revision'

db-dump: ## create a database.sql file : make migrate
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
