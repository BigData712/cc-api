# cc-api
This is the "middle man" between Opensearch on AWS and the frontend consumers of crime data. It simply passes along a url and authenticates itself to Opensearch and returns the result.
## Running
You too could run this (for some reason) by simply running
`pip install -r requirements.txt` and `gunicorn app:app`. Have fun and make sure to supply your own .env file!
## Deployment
This currently auto-deploys on-push to https://cc-api-wav6.onrender.com/ - it takes about 3 minutes!
