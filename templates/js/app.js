var canvas = new fabric.canvas('canvas', { isDrawingMode:true });

canvas.backgroundColor = 'black';
canvas.freeDrawingBrush.color = 'white';
canvas.freeDrawingBrush.width = 10;

function clearCanvas() {
    canvas.clear();
}

function sendImageData(imageData) {
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
            document.getElementById('prediction').innerText = `Predicted digit: ${data.prediction}`;
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
