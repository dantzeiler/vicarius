FROM python:3.11-slim
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY application/ /app

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the application
CMD ["python", "main.py"]