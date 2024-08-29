Replace the mc server files on the nas with the ones on my desktop and make sure the dockerfile is there


docker build -t mc-server-1.20 .
docker run -d -p 25565:25565 --name minecraft-server-container mc-server-1.20