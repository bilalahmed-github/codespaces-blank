# Pull latest Docker images
docker pull gcr.io/your-project/my-backend:latest
docker pull gcr.io/your-project/my-frontend:latest

# Run Docker containers
docker run -d -p 5000:5000 gcr.io/your-project/my-backend:latest
docker run -d -p 80:80 gcr.io/your-project/my-frontend:latest
