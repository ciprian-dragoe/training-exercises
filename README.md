# What is it ?
It's a front end site where user's solve a predefined list of exercises.

## Steps to start the project
1. Install requirements: `pip install -r requirements.txt in`
2. Create a copy of `.env.template` named `.env` and populate the empty fields
3. optional if you want to execute other exercises besides js `docker build -t learn-coding .`
4. Start the project via `python server.py`

## What is the `Admin` interface for
Non `js` code can only be executed while the admin is logged in.
To login access the link `/admin/dashboard` by supplying the password  set in the `.env` file for the field `ADMIN_DASHBOARD_PASS`

## Make the exercises page accessible as a public link when you are on a local host
1. Install npm
2. `npm install -g localtunnel`
3. Run the app on your local computer via `python server.py`
4. Make your local host port 5000 (default dev port when running starting the app) available publicly `lt --port 5000`
5. Copy the generated link by `lt`and send it to the students
