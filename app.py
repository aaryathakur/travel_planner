from flask import Flask, render_template, request
from utils.distance import get_distance
from utils.weather import get_weather

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    source = request.form.get("source")
    destination = request.form.get("destination")

    # Get distance
    distance = get_distance(source, destination)

    # Get weather and icon
    weather, icon = get_weather(destination)

    # If data is invalid
    if not distance or not weather or not icon:
        return "Invalid source or destination, or unable to fetch weather data."

    # Print for debugging
    print(f"Source: {source}")
    print(f"Destination: {destination}")
    print(f"Distance: {distance}")
    print(f"Weather: {weather}")
    print(f"Icon: {icon}")

    return render_template(
        "result.html",
        source=source,
        destination=destination,
        distance=f"{distance} km",
        weather=weather,
        icon=icon,
        api_key="AIzaSyBiCYAcbOLnvEu9udIh5cT9dB0o_vldc9I"
    )

if __name__ == "__main__":
    app.run(debug=True)
