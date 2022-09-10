Build image

```
docker build -t python .          
```

Run with docker

```
docker run --rm --volume="$PWD:/app" -it python python /app/scrap.py
```