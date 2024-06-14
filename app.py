from model.model import Net
import base64
from io import BytesIO
import torch
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def render_html():
    return render_template("html/index.html")


@app.route("/predict", methods=['POST'])
def prediction():
    img_data = request.json['image_data']
    img_bytes = base64.b64decode(img_data.split(',')[1])
    
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor()
    ])

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    img = transform(Image.open(BytesIO(img_bytes)).convert("L"))
    img = img.unsqueeze(0).to(device)

    model = Net().to(device)
    model.load_state_dict(torch.load("./model/model_state_dict.pth"))

    with torch.no_grad():
        model.eval()
        output = model(img)
        probs = torch.nn.functional.softmax(output, 1)
        confidence, prediction = torch.max(probs, 1)
        
        prediction = prediction.item()
        confidence = f'{confidence.item():.1%}'

        return jsonify({
            "prediction": prediction,
            "confidence": confidence
        })
        

if __name__ == '__main__':
    app.run(port=5000, debug=True)
