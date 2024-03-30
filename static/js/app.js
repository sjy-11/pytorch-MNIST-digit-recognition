var canvas = new fabric.Canvas('canvas', { isDrawingMode:true, backgroundColor:'black' });

canvas.freeDrawingBrush.color = 'white';
canvas.freeDrawingBrush.width = 50;




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
            document.getElementById('prediction').innerText = `Predicted digit: ${data.prediction}, Confidence: ${data.confidence}`;
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
