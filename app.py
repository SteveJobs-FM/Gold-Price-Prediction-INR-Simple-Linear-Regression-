# Importing the required libraries
import gradio as gr
import pickle 
import numpy as np

# Opening the pickled data for prediction
with open('scaled_data.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('GoldPrice_pred.pkl', 'rb') as f:
    model = pickle.load(f)

# Function for prediction
def goldrate_calc(usd_inr):
    scaled_input = scaler.transform(np.array([[usd_inr]]))
    prediction = model.predict(scaled_input)[0]
    return float(np.round(prediction, 2))

# Interface
interface = gr.Interface(
    fn=goldrate_calc,
    inputs=gr.Number(label="USD to INR Rate (e.g. 88.50)", value=88.50),
    outputs=gr.Number(label="Predicted 22K Gold Price (₹/gram)"),
    title="22K Gold Price Predictor in India (per gram)"
)

if __name__ == '__main__':
    interface.launch()