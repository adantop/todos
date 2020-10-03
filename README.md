TEST ME

```
docker image build -t backend:0.0.1 .
docker run --name backend -d -p 5000:5000 backend:0.0.1
```