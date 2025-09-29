from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)

stations=pd.read_csv("weather_data/stations.txt", skiprows=17)
stations=stations[['STAID', 'STANAME                                 ']]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def home_data(station, date):
    filename=f"weather_data\TG_STAID{str(station).zfill(6)}.txt"
    df=pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'], na_values=-9999)
    temperature = df.loc[df['    DATE'] == date, '   TG'].squeeze() / 10.0
    return {"station": station, "date": date, "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename=f"weather_data\TG_STAID{str(station).zfill(6)}.txt"
    df=pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'], na_values=-9999)
    return df.to_dict(orient="records")

@app.route("/api/v1/yearly/<station>/<year>")
def yearly_data(station,year):
    filename=f"weather_data\TG_STAID{str(station).zfill(6)}.txt"
    df=pd.read_csv(filename, skiprows=20, na_values=-9999)
    df['    DATE'] = df['    DATE'].astype(str)
    return df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")

if __name__ == "__main__":
    app.run(debug=True)