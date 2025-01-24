#!/bin/bash
# Login to AWS ECR
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/b2r6l3l6


# Pull the latest image
docker pull public.ecr.aws/b2r6l3l6/color-reg:latest


# Check if the container 'v3' is running
if [ "$(docker ps -q -f name=v3)" ]; then
    # Stop the running container
    docker stop campusx-app
fi

# Check if the container 'v3' exists (stopped or running)
if [ "$(docker ps -aq -f name=v3)" ]; then
    # Remove the container if it exists
    docker rm v3
fi

# Run a new container
docker  run -d -p 80:5000 -e DAGSHUB_PAT=65078b3cf64cdf7a632725fb2b881048addcdceb  --name color-reg:latest public.ecr.aws/b2r6l3l6/color-reg:latest 