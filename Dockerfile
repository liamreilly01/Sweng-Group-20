FROM python:3.9


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "bot.py"]
