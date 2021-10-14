FROM python:3.9
LABEL "repository"="https://github.com/xxDonkey/Mr-Meeseeks"
LABEL "maintainers"="WarpWing and xxDonkey"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt update && apt upgrade && apt install ffmpeg -y
RUN SODIUM_INSTALL=system pip3 install pynacl
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "main.py"]