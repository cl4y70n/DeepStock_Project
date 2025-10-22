
from prophet import Prophet

def train_prophet(df):
    m = Prophet(yearly_seasonality=True)
    m.fit(df.rename(columns={'Date':'ds','Close':'y'}))
    return m

def forecast_prophet(model, periods=5):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
