#!/usr/bin/env bash
set -euo pipefail   # crash on missing env variables, stop on any error, and exit if a pipe fails
set -x   # Enable verbose output for debugging

# echo "Start with a fresh database"
# export PGPASSWORD=${DATABASE_PASSWORD}
# psql -h ${DATABASE_HOST_OVERRIDE} -p 5432 -d ${DATABASE_NAME} -U ${DATABASE_USER} -c "drop schema public cascade;"
# psql -h ${DATABASE_HOST_OVERRIDE} -p 5432 -d ${DATABASE_NAME} -U ${DATABASE_USER} -c "create schema public;"

# Define the path to the uWSGI log file
UWSGI_LOG="/app/uwsgi.log"

# Ensure the uWSGI log file exists and set appropriate permissions
touch "$UWSGI_LOG"
chown "$APP_USER:$APP_USER" "$UWSGI_LOG"
chmod 644 "$UWSGI_LOG"

# Log a message indicating the script has started
echo "Docker entrypoint script has started."

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Create a superuser (if not already created)
echo "Creating superuser..."
if ! python manage.py createsuperuser --noinput; then
    echo "Superuser creation failed or already exists."
fi

# Create users for app to app communication
echo Create users
python manage.py createusers --noinput || true

# Log a message indicating the script has completed
echo "Docker entrypoint script has completed."

# Execute uWSGI with the specified configuration file
exec uwsgi --ini /app/deploy/config.ini
