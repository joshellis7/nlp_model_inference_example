from permutable_nlp_model_inference.inference import inference

model_dir = "models/general_sentiment/"
text = ["oil price is up 10%", "gas output has decreased"]

predictions = inference(model_dir, text)
print(predictions)