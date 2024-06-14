var canvas = new fabric.Canvas('canvas', { isDrawingMode:true, backgroundColor:'black' });

canvas.freeDrawingBrush.color = 'white';
canvas.freeDrawingBrush.width = 30;

function clearCanvas() {
    location.reload();
}

function sendImageData(imageData) {
    console.log(imageData)
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image_data: imageData })
    }).then(
        response => response.json()
    ).then(
        data => {
            var confi = parseInt(data.confidence)
            var textColor = confi >= 75? "success": confi >= 50? "warning": "danger"
            document.getElementById('prediction').innerHTML = `Predicted digit: <span class="fs-1 fw-bold text-${textColor}">${data.prediction}</span><br>Confidence: <span class="fs-1 fw-bold text-${textColor}">${data.confidence}</span>`;
        }
    ).catch(
        error => {
            console.error('Error:', error)
        }
    );
}

function predictDigit() {
    var imageData = canvas.toDataURL('image/png');
    sendImageData(imageData);
}
