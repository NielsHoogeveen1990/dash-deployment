# How to run this dash app with Docker?
0. Make sure Docker Desktop is installed
1. Create a virtual environment
2. Activate the virtual environment
3. Build the Docker image
```
$ docker build -t navara-dash -f Dockerfile . 
```
4. Run the Docker container
```
$ docker run -p 8050:8050 navara-dash
```
5. Go to your browser at IP address: 0.0.0.0 and port 8050