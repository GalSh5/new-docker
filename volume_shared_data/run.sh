docker run --detach --volume newvol:/data/ --name container1 myapp:latest ./app.py 1
docker run --detach --volume newvol:/data/ --name container2 myapp:latest ./app.py 2
