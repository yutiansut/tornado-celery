apt-get update --fix-missing

apt-get install gcc

apt-get install make

wget http://download.redis.io/releases/redis-4.0.8.tar.gz
tar xzf redis-4.0.8.tar.gz
cd redis-4.0.8/
make MALLOC=libc