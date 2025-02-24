FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install numpy pandas scikit-learn wandb opencv-python
RUN apt-get update && apt-get install -y libgl1-mesa-glx

CMD ["python", "distance_classification.py"]