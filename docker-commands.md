# Docker Commands for AirCnC Clone

## Redis Development Setup

### Start Redis (Development)

```bash
# Option 1: Redis only
docker-compose -f docker-compose.dev.yml up -d redis

# Option 2: Redis + Web UI
docker-compose -f docker-compose.dev.yml up -d
```

### Stop Redis

```bash
docker-compose -f docker-compose.dev.yml down
```

### View Redis Logs

```bash
docker logs aircnc-redis-dev -f
```

### Connect to Redis CLI

```bash
docker exec -it aircnc-redis-dev redis-cli
```

### Redis Web UI

- URL: http://localhost:8081
- View all databases, keys, and values

## Production Setup (Full Stack)

### Start All Services

```bash
docker-compose up -d
```

### Stop All Services

```bash
docker-compose down
```

### View All Logs

```bash
docker-compose logs -f
```

## Useful Commands

### Check Container Status

```bash
docker ps
```

### Remove All Containers & Volumes

```bash
docker-compose down -v
docker system prune -a
```

### Backup Redis Data

```bash
docker exec aircnc-redis-dev redis-cli BGSAVE
```

### Monitor Redis Performance

```bash
docker exec -it aircnc-redis-dev redis-cli INFO
docker exec -it aircnc-redis-dev redis-cli MONITOR
```

## Environment Variables

Create `.env` file:

```bash
# Redis
REDIS_URL=redis://localhost:6379
REDIS_PASSWORD=your_password_here

# PostgreSQL
DB_NAME=aircnc_clone
DB_USER=aircnc_user
DB_PASSWORD=aircnc_password
DB_HOST=localhost
DB_PORT=5432
```
