# Docker compose build the containers with the local docker-compose file
docker compose \
  -f docker-compose.yml \
  -f docker-compose.local.yml build

# Docker compose up the containers with the local docker-compose file
docker compose \
  -f docker-compose.yml \
  -f docker-compose.local.yml up \
  -d
