

cd frontend
docker image build -t todo_frontend:0.0.1 .
docker run --name frontend -d -p 5001:5000 todo_frontend:0.0.1


cd ../backend
docker image build -t todo_backend:0.0.1 .
docker run --name backend -d -p 5000:5000 todo_backend:0.0.1
