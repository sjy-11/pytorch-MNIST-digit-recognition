# Handwritten Digit Classification

![Default Homepage][index-screenshot]

## About The Project

This project demonstrates a simple web interface using Flask as the backend and Bootstrap as the frontend.

The main goal is to classify handwritten digits using a CNN model built with PyTorch. This multi-class classifier predicts digits from 0 to 9. 

The web interface allows users to draw digits on an interactive HTML canvas, and the model provides corresponding predictions along with confidence scores.

### Built With

Major libraries, frameworks, and languages used in this project:
* [![Python][Python.com]][Python-url]
* [![Pytorch][Pytorch.com]][Pytorch-url]
* [![Flask][Flask.com]][Flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JavaScript][JavaScript.com]][JavaScript-url]

## Table of Contents

1. [Getting Started](#getting-started)
2. [Usage](#usage)
3. [Model Overview](#model-overview)
5. [Acknowledgments](#acknowledgments)
6. [License](#license)

## Getting Started

_To get a local copy up and running, follow these steps._

### Prerequisites

Ensure you have the following dependencies installed:
* Flask
* Pillow
* torch
* torchmetrics
* torchvision

You can install these dependencies using pip:
  ```sh
  pip install Flask Pillow torch torchmetrics torchvision
  ```

### Initialize Environment

1. Clone the repository:
   ```sh
   git clone https://github.com/sjy-11/pytorch-MNIST-digit-recognition.git
   ```
2. Navigate to the project directory:
   ```sh
   cd pytorch-MNIST-digit-recognition
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. Access the web interface:  
   The local development server will be hosted on port 5000. After running python app.py, you can click on the URL shown in the terminal, or open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
### Usage

Once you have the application running, you can draw digits (0-9) on the interactive canvas through the web interface.   
The application will show:
* The predicted digit.
* The confidence score of the prediction.
* Example:
![Example of drawn digits on canvas][example-screenshot]



## Model Overview

The Convolutional Neural Network (CNN) model used in this project is designed for multi-class classification. Users can alter the model's architecture in the model.py file and train their models in the train_test.py file.

## Acknowledgments

* [MNIST Dataset Wikipedia](https://en.wikipedia.org/wiki/MNIST_database)
* [MNIST Dataset PyTorch](https://pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html)
* [Canvas Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)



## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[index-screenshot]: images/index_screenshot.png
[example-screenshot]: images/example_screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Pytorch.com]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white 
[Pytorch-url]: https://pytorch.org
[Flask.com]: https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff&style=for-the-badge
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x
[Python.com]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge
[Python-url]: https://www.python.org
[Javascript.com]: https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000&style=for-the-badge
[Javascript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript