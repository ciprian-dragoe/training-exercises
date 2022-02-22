# What is it ?
It's a front end site where user's solve a predefined list of exercises.

## Steps to start the project
1. Make a copy of `env.template` as `.env` in the same folder
1. In the `.env` file set the ADMIN_DASHBOARD_PASS (this will be used to log in the admin interface)
1. In the `.env` file set the APP_SECRET_KEY (just some random gibberish text that will be used as a seed)
1. Install python
1. Create a virtual environment by writing in the termin `python -m venv`
1. !!! Before each run of the applicaiton activate the virtual environment by writing in the terminal `.\venv\Scripts\Activate.ps1`
1. (OPTIONAL - if you have authorization error when activating the virtual environment) Run in a powershell with admin privileges `Set-ExecutionPolicy RemoteSigned`
1. (OPTIONAL - if you have windows you might need to install extra softeare) Download & isntall https://aka.ms/vs/16/release/vs_buildtools.exe
3. Install external libraries by writing in a terminal windows `pip install -r requirements.txt`
5. Start the project via `python server.py`

## Optional - if you want to run python exercises
1. Install docker from https://docs.docker.com/get-docker/
1. Run in a terminal  `docker build -t learn-coding .`


## What is the `Admin` interface for
Non `js` code can only be executed while the admin is logged in.
To login access the link `/admin/dashboard` by supplying the password  set in the `.env` file for the field `ADMIN_DASHBOARD_PASS`

## Make the exercises page accessible as a public link when you are on a local host
1. Install npm
2. `npm install -g localtunnel`
3. Run the app on your local computer via `python server.py`
4. Make your local host port 5000 (default dev port when running starting the app) available publicly `lt --port 5000`
5. Copy the generated link by `lt`and send it to the students
