# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# ระบุ Python version ก่อนติดตั้ง requirements
RUN pip install  -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask application when the container starts
# CMD ["python", "app.py"]
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
