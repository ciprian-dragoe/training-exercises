# What is it ?
It's a front end site where user's solve a predefined list of exercises.

## Steps to start the project

1. Make a copy of `.env.template` as `.env` in the same folder (optionally you can set different values)
* If you do not see the `.env.template` please make sure you have enabled from your operating system `show hidden files`
2. Install Docker
3. Open a terminal in the root project folder and type `docker-compose up` 
* The first time it will take a while (approximately 10m) before starting because the dependencies are being downloaded
4. Open the app in the browser on `localhost:5000` (default value set in `docker-compose.yml`)


## What is the `Admin` interface for
Backend code can only be executed only while the admin is logged in.
To login access the link `/admin/dashboard` by supplying the password  set in the `.env` file for the field `ADMIN_DASHBOARD_PASS`

## Make the exercises' page accessible as a public link when you are on a local host
1. Install npm & node
2. `npm install -g localtunnel`
3. Run the app on your local computer via `docker-compose up`
4. Make your local host port 5000 (default dev port when running starting the app) available publicly `lt --port 5000`
5. Copy the generated link by `lt`and send it to the students
