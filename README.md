# Soccer Stats App
This is a Streamlit app that displays soccer team statistics of the 5 top Premier League clubs and allows users to predict match outcomes and compare team performances. The app is containerized using Docker.

# Features
- Team Statistics: View team goals scored, goals conceded, and points in a table format.
- Goals Scored Visualization: A bar chart displaying goals scored by each team.
- Match Predictor: Predict the outcome of a match between two selected teams based on their points.
- Team Comparison: Compare two teams' performance using a radar chart based on goals scored, goals conceded, and points.

# How to Run the App

For Local Setup without Docker:

- Clone the repository:

Copy the code:

git clone https://github.com/your-username/Streamlite-Soccer-App.git

cd app

- Install Python dependencies: 

Copy the code:

pip install -r requirements.txt

- Run the app:

Copy the code:

streamlit run soccer_stats_app.py

Access the app: Open your browser and go to http://localhost:8501.

# Running the App with Docker

- Build the Docker image: 

Copy the code:

docker build -t soccer-stats-app .

- Run the Docker container:

Copy the code:

docker run -p 8501:8501 soccer-stats-app

Access the app: Open your browser and go to http://localhost:8501.
