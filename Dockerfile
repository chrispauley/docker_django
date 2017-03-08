FROM python:3.4

# Set PYTHONUNBUFFERED so output is displayed in the Docker log
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application's code
COPY . /usr/src/app

# Run the app
RUN chmod +x ./run_app.sh
CMD ["./run_app.sh"]
