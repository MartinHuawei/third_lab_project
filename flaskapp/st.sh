gunicorn --bind 127.0.0.1:5000 wsgi:app & APP_PID=$!

echo ...
sleep 5

echo start client
python3 client.py

echo ...
sleep 5

echo PID: $APP_PID
kill -TERM $APP_PID

echo process gunicorns kills
exit 0
