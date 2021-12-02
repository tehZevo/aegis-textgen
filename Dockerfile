FROM pytorch/pytorch

WORKDIR /app

COPY requirements.txt .
RUN apt update -y
RUN apt install git -y
RUN pip install -r requirements.txt

# download model in separate layer
COPY download.py .
RUN python download.py

COPY . .

EXPOSE 80

CMD [ "python", "-u", "main.py" ]
