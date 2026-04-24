
# TP04 - Docker pour les systèmes IoT

## Description
Système IoT avec Docker composé de 3 conteneurs communicant via MQTT.

## Architecture
## Conteneurs
- **sensor** : envoie la température toutes les 3 secondes
- **broker** : Mosquitto MQTT broker
- **server** : reçoit et affiche les données

## Lancer le projet
```bash
docker compose up --build
```

## Images Docker Hub
- Sensor : https://hub.docker.com/r/radjague/sensor
- Server : https://hub.docker.com/r/radjague/server
- Tp3-image   : https://hub.docker.com/r/radjague/tp3-image 
