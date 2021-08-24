FROM python:3.8-slim
#suppress warining https://stackoverflow.com/questions/67244301/warning-messages-when-i-update-pip-or-install-packages
RUN apt update -y;
RUN apt install curl jq -y
RUN pip3 install requests pyyaml|| true
RUN mkdir -p /dd_prepare
#ENV PYTHONPATH "${PYTHONPATH}:/dd_prepare"
COPY ./defectdojo_apiv2.py /dd_prepare/defectdojo_apiv2.py
COPY ./dd_prepare.py /dd_prepare/dd_prepare.py
COPY ./make_variables.sh /dd_prepare/make_variables.sh
