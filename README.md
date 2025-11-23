

# Build and Run

```
docker build -t ocrapi-py
docker run -it --rm -p 8080:8080 ocrapi-py
```

# Push Docker Image

```
docker tag ocrapi-py your-dockerhub-username/ocrapi-py:latest
docker push your-dockerhub-username/ocrapi-py:latest
```
