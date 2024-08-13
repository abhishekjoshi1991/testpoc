# Steps to Run the Project
## A. Running Back-end code
### 1. Open new empty terminal on local machine

### 2. Connect to Remote Server
```bash
ssh -L 7015:127.0.0.1:7015 rikaian@34.93.196.11
```
Enter remote server password
### 3. Start Docker Service
```bash
cd /mnt/data1/imai
sudo docker-compose up -d
```
### 4. Activate Virtual Environment
```bash
cd /mnt/data1/imai_phase2/imai_poc
conda deactivate
source imaienv/bin/activate
```
### 5. Run the ETL Script
```bash
cd /mnt/data1/imai_phase2/imai_poc/etl
python3 etl.py
```
### 6. Run the Server
```bash
cd /mnt/data1/imai_phase2/imai_poc/
python3 run.py
```

## B. Running back-end for Web UI

### 1. Open new empty terminal on local machine
### 2. Connect to Remote Server
```bash
ssh -L 3000:127.0.0.1:3000 rikaian@34.93.196.11
```
Enter remote server password
### 3. Start back-end server for Web UI
```bash
cd /mnt/data1/node_imai/IMAI_back_end
node index.js
```


## C. Running front-end for Web UI

### 1. Open new empty terminal on local machine
### 2. Connect to Remote Server
```bash
ssh -L 3001:127.0.0.1:3001 rikaian@34.93.196.11
```
Enter remote server password
### 3. Start front-end server for Web UI
```bash
cd /mnt/data1/node_imai/imai_web/IMAI_front_end
npm start
```

### D. Access Web UI from URL
Open a web browser on your local machine and navigate to http://localhost:3001/login.
If user don't have an account, then he/she need to sign up first by clicking on SignUp.
Once account creation is successful, user can login through login page.
Once login successful, page is redirected to http://localhost:3001/user-routes/dashboard. User can select alert email file from the form field provided and click on submit to get further results.

After testing complete run "ctrl+c" from all local terminal and then "exit"


**Note:**
Currently redmine url is configured on 'origin1' and 'http' protocol. This configuration can be changed from .env file by changing 'REDMINE_HOST' and 'REDMINE_HTTP_PROTOCOL' variable values to required one.
Example: 
REDMINE_HOST='origin1'
REDMINE_HTTP_PROTOCOL='http'
will generate url like 'http://origin1/projects/manpyo-op/wiki/CPU使用率閾値超過'

**Note:**
If on running the server if you get like port 7015 (or other) is already in use the you can use following command to kill the process first and then run the server again.
```bash
sudo kill -9 `sudo lsof -t -i:7015` (just replace the port number)
```

