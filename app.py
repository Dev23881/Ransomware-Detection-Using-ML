
import gradio as gr
import pandas as pd
import joblib

# Load trained model and preprocessing files
rf_model = joblib.load("random_forest.pkl")
imputer = joblib.load("imputer.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

def detect_ransomware(file):
    if file is None:
        return "Please upload a CSV file.", None

    try:
        data = pd.read_csv(file)

        missing = [col for col in feature_names if col not in data.columns]

        if missing:
            return "Missing required features: " + ", ".join(missing[:10]), None

        X_input = data[feature_names]
        X_input = X_input.replace([float("inf"), float("-inf")], float("nan"))

        X_imputed = imputer.transform(X_input)
        X_scaled = scaler.transform(X_imputed)
        predictions = rf_model.predict(X_scaled)

        results = data.copy()
        results["Prediction"] = [
            "Ransomware" if value == 1 else "Benign"
            for value in predictions
        ]

        ransomware_count = int(sum(predictions == 1))
        benign_count = int(sum(predictions == 0))

        summary = (
            f"Analysis Completed!\n"
            f"Total Records: {len(predictions)}\n"
            f"Benign Records: {benign_count}\n"
            f"Ransomware Records: {ransomware_count}"
        )

        return summary, results

    except Exception as e:
        return f"Error: {str(e)}", None


with gr.Blocks(title="Ransomware Detection System") as demo:

    gr.Markdown("# Ransomware Detection System")
    gr.Markdown("### Deep Learning-Based Ransomware Detection Using Behavioral Features")

    file_input = gr.File(
        label="Upload CSV Dataset",
        file_types=[".csv"],
        type="filepath"
    )

    analyze_btn = gr.Button("Analyze Dataset", variant="primary")

    output_summary = gr.Textbox(label="Detection Summary", lines=5)
    output_table = gr.Dataframe(label="Prediction Results")

    analyze_btn.click(
        fn=detect_ransomware,
        inputs=file_input,
        outputs=[output_summary, output_table]
    )

demo.launch()
