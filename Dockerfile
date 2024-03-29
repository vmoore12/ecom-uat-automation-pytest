FROM python:3.10
WORKDIR /automation/ecom_uat_automation_pytest


# WORKDIR /automation


# Do not know where the folowing is from

RUN ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime 
RUN echo "America/Chicago" > /etc/timezone

# RUN mkdir /automation

# Option 1
#COPY requirements.txt /automation
#RUN python3 -m pip install -r /automation/requirements.txt

# Option 2
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "-m", "pytest", "tests"]

#CMD []