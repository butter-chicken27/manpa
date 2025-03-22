#!/bin/bash

# Log startup script output
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1

# Update system packages
sudo yum update -y


sudo su
curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
exit
sudo ACCEPT_EULA=Y yum install -y msodbcsql17
sudo yum install -y unixODBC-devel

# Install Python and required tools
sudo yum install -y python3-pip git

# Set up application directory
APP_DIR=/home/ec2-user/app
sudo mkdir -p $APP_DIR
sudo chown ec2-user:ec2-user $APP_DIR
cd $APP_DIR

# Clone the repository and move files to correct location
git clone https://github.com/butter-chicken27/manpa.git .
cd app

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn gunicorn python-dotenv

# Create systemd service with sudo
sudo bash -c 'cat << EOF > /etc/systemd/system/fastapi.service
[Unit]
Description=FastAPI application
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/home/ec2-user/app/app
Environment="PATH=/home/ec2-user/app/app/venv/bin"
Environment="PYTHONPATH=/home/ec2-user/app/app"
StandardOutput=append:/var/log/fastapi.log
StandardError=append:/var/log/fastapi.error.log
ExecStart=/home/ec2-user/app/app/venv/bin/gunicorn \
    -w 4 \
    -k uvicorn.workers.UvicornWorker \
    main:app \
    --bind 0.0.0.0:8000 \
    --log-level debug

[Install]
WantedBy=multi-user.target
EOF'

# Create log files and set permissions
sudo touch /var/log/fastapi.log /var/log/fastapi.error.log
sudo chown ec2-user:ec2-user /var/log/fastapi.log /var/log/fastapi.error.log

# Set proper permissions
sudo chown -R ec2-user:ec2-user $APP_DIR
sudo chmod 644 /etc/systemd/system/fastapi.service

# Start and enable the service
sudo systemctl daemon-reload
sudo systemctl start fastapi
sudo systemctl enable fastapi

# Output the status
echo "Installation complete. Check status with: sudo systemctl status fastapi s"