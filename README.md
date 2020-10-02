

cd frontend
docker image build -t frontend:0.0.1 .
docker run --name frontend -d -p 5001:5000 frontend:0.0.1


cd ../backend
docker image build -t backend:0.0.1 .
docker run --name backend -d -p 5000:5000 backend:0.0.1
