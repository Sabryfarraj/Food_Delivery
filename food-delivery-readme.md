# Food Delivery Time Prediction App 🍕

A machine learning application that predicts food delivery time using XGBoost Regressor. The application is containerized using Docker and provides an interactive web interface built with Streamlit.

## 🚀 Quick Start

You have two options to access the application:

### Option 1: Web Browser (No Installation Required)
Visit the live application at:
```
https://fooddelivery-bysabryfarraj.streamlit.app/
```
This option requires no setup - just click and use!

### Option 2: Run using Docker

If you prefer to run the application locally:

```bash
# Pull the image from Docker Hub
docker pull sabryfarraj/food-delivery-predictor:latest

# Run the container
docker run -p 8501:8501 sabryfarraj/food-delivery-predictor:latest
```

After running these commands, open your browser and visit:
```
http://localhost:8501
```

## 🛠️ Project Structure
```
Food_Delivery/
├── Food_Delivery.py              # Main Streamlit application
├── final_pipeline.pkl           # Trained XGBoost model pipeline
├── min_max_values.pkl          # Feature scaling values
├── unique_values.pkl           # Categorical features mapping
└── requirements.txt            # Python dependencies
```

## 📋 Prerequisites
For Docker option only:
- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))

## 🔧 Local Development

If you want to build the Docker image locally:

```bash
# Clone the repository
git clone https://github.com/Sabryfarraj/Food_Delivery.git

# Navigate to project directory
cd Food_Delivery

# Build Docker image
docker build -t food-delivery-predictor .

# Run container
docker run -p 8501:8501 food-delivery-predictor
```

## 📊 Features
- Predicts food delivery time based on various factors
- Interactive web interface
- Real-time predictions
- Available as web application and containerized application
- Pre-trained XGBoost model
- Handles various input features like:
  - Delivery person details
  - Restaurant information
  - Order type
  - Vehicle condition
  - Weather conditions
  - Traffic density
  - Distance metrics

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Authors
- Sabry Farraj

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments
- Built with Streamlit and XGBoost
- Uses scikit-learn for preprocessing
- Hosted on Streamlit Cloud
