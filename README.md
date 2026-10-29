
<h1 align="center">🏀 Basketball Shot Prediction</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/CVZone-Image%20Processing-orange?style=for-the-badge" alt="CVZone">
</p>

<p align="center">
  A computer vision project that predicts whether a basketball shot will enter the basket by tracking the ball and estimating its trajectory.
</p>

<hr>

<h2>📌 About The Project</h2>

<p>
  Basketball Shot Prediction is a computer vision project developed using Python, OpenCV, NumPy, and CVZone.
</p>

<p>
  The system detects the basketball using HSV color thresholding, tracks its position across video frames, and applies polynomial regression to estimate the ball's trajectory.
</p>

<p>
  By calculating the intersection between the predicted trajectory and the basket's horizontal level, the program estimates whether the shot is likely to enter the basket.
</p>

<h2>⚙️ Features</h2>

<ul>
  <li>🎯 Basketball detection using HSV color thresholding</li>
  <li>📍 Ball position tracking across video frames</li>
  <li>🟢 Visualization of detected ball positions</li>
  <li>📈 Polynomial regression for trajectory estimation</li>
  <li>🔮 Prediction of the ball's path toward the basket</li>
  <li>🏀 Shot prediction: Basket or No Basket</li>
  <li>🎥 Video processing and visualization using OpenCV</li>
</ul>

<h2>🛠️ Technologies Used</h2>

<table>
  <thead>
    <tr>
      <th>Technology</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python</td>
      <td>Main programming language</td>
    </tr>
    <tr>
      <td>OpenCV</td>
      <td>Image processing and video handling</td>
    </tr>
    <tr>
      <td>NumPy</td>
      <td>Numerical calculations and polynomial regression</td>
    </tr>
    <tr>
      <td>CVZone</td>
      <td>Text overlays and visualization utilities</td>
    </tr>
    <tr>
      <td>Math</td>
      <td>Trajectory intersection calculations</td>
    </tr>
  </tbody>
</table>

<h2>🧠 How It Works</h2>

<h3>1. Video Input</h3>
<p>
  The program reads a basketball video using OpenCV and processes it frame by frame.
</p>

<h3>2. Color-Based Detection</h3>
<p>
  Each frame is converted from BGR to HSV color space. A color mask is generated using predefined HSV thresholds to isolate the basketball.
</p>

<h3>3. Ball Tracking</h3>
<p>
  The program detects contours in the mask and filters them based on their area. The center coordinates of detected regions are stored to track the ball's movement.
</p>

<h3>4. Trajectory Estimation</h3>
<p>
  NumPy fits a second-degree polynomial to the detected ball positions:
</p>

<p align="center">
  <code>y = Ax² + Bx + C</code>
</p>

<p>
  The resulting curve estimates the ball's trajectory based on previously detected positions.
</p>

<h3>5. Basket Prediction</h3>
<p>
  The predicted trajectory is evaluated at the configured basket height, y = 590. The resulting horizontal coordinate is compared with the basket range, x = 330 to x = 430.
</p>

<ul>
  <li><strong>Basket:</strong> The predicted intersection falls inside the configured basket range.</li>
  <li><strong>No Basket:</strong> The predicted intersection falls outside the range or no valid intersection is found.</li>
</ul>

<p>
  <em>Note: This is a trajectory-based prediction and does not guarantee that the ball physically enters the basket.</em>
</p>

<h2>📦 Installation</h2>

<p>Install the required libraries:</p>

<pre><code>pip install opencv-python numpy cvzone</code></pre>

<h2>🚀 Usage</h2>

<ol>
  <li>Clone or download the repository.</li>
  <li>Install the required dependencies.</li>
  <li>Place your basketball video inside the <code>data</code> directory.</li>
  <li>Update the video path if necessary.</li>
  <li>Run the Python script.</li>
</ol>

<pre><code>python main.py</code></pre>

<p>
  Press <code>ESC</code> to exit the video window.
</p>

<h2>📁 Project Structure</h2>

<pre>
Basketball-Shot-Prediction/
├── data/
│   └── vid (3).mp4
├── main.py
├── requirements.txt
└── README.md
</pre>

<h2>🔧 Configuration</h2>

<ul>
  <li><strong>HSV Thresholds:</strong> Define the color range used to detect the ball.</li>
  <li><strong>Contour Area:</strong> Filters out small detected regions.</li>
  <li><strong>Basket Height:</strong> Defines the horizontal level used for trajectory intersection.</li>
  <li><strong>Basket X Range:</strong> Defines the horizontal boundaries of the basket.</li>
  <li><strong>Resize Percentage:</strong> Controls the displayed video size.</li>
</ul>

<h2>⚠️ Limitations</h2>

<ul>
  <li>Detection accuracy depends on lighting and color conditions.</li>
  <li>The basket coordinates are manually configured for the input video.</li>
  <li>Incorrect ball detections may affect the estimated trajectory.</li>
  <li>The current implementation predicts the shot outcome rather than verifying an actual basket.</li>
</ul>

<h2>🔮 Future Improvements</h2>

<ul>
  <li>Automatic basket detection</li>
  <li>Improved ball tracking and trajectory estimation</li>
  <li>Actual shot-result verification</li>
  <li>Live camera support</li>
  <li>Shot counting and accuracy statistics</li>
</ul>

<hr>

<p align="center">
  <strong>Built with Python, OpenCV, NumPy, and CVZone 🏀</strong>
</p>
