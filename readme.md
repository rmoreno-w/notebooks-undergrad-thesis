# Transfer Learning with Audio Data - Final Project

This project was elaborated as my final project for my undergraduate degree and aimed to investigate the application of **transfer learning** for emotion classification in audio, using pre-trained neural networks such as **YAMNet** and **VGGish**. The goal is to compare the performance of different classifiers, such as **SVM**, **Random Forest**, **Naive Bayes**, and **MLP**, for emotion classification based on audio data.

The dataset used is the **RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)**, widely used for emotion analysis in audio. You can access the RAVDESS dataset on this [link](https://zenodo.org/records/1188976).

> **Nota**: Se preferir, você pode ler a descrição do projeto em português 🇧🇷. Consulte o [README em português](readme-pt.md) para mais detalhes.

## 🗂️ Table of Contents

-   [Description](#description)
-   [Technologies](#technologies)
-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [How to Use](#how-to-use)
-   [License](#license)

## 📜 Description

This project applies **transfer learning** using pre-trained neural networks (**YAMNet** and **VGGish**) to extract features from audio. Then, we train traditional classifiers (**SVM**, **Random Forest**, **Naive Bayes**, and **MLP**) on these extracted features, as well as features derived from **Mel spectrograms**, in order to classify emotions in the audio data.

The project workflow is as follows:

1. **Feature Extraction**:

    - **VGGish**: Uses a pre-trained model to extract audio features.
    - **YAMNet**: A neural network model used for extracting audio features.
    - **Mel Spectrograms**: Extracts Mel spectrograms directly from the audio files.

2. **Classifier Training**:
    - Trains **SVM**, **Random Forest**, **Naive Bayes**, and **MLP** classifiers to predict emotions from the extracted features.

> **Important**: The script `generate_csv_metadata.py` expects the audio files to be placed in a folder called `data`. It only processes the audio files and **excludes the audio files from singing actors** and any video files. Make sure to only include speech audio files in the `data` folder for the script to work properly. Or modify the script, if you prefer to do it in a different way.

## 💻 Technologies

This project was developed using the following libraries and tools:

-   **Python 3.11**
-   **Jupyter Notebooks** (for interactive analysis)
-   **Pandas (v 2.2.1)**: For data analysis and manipulation
-   **Librosa (v 0.10.1)**: For audio file processing
-   **TensorFlow (v 2.13.0)**: For creating and adapting neural networks
-   **TensorFlow Hub (v 0.16.1)**: For access to pre-trained machine learning models
-   **Scikit-learn (v 1.4.1.post1)**: For training traditional machine learning models
-   **Matplotlib (v 3.8.3)**: For visualizing results and graphs

## 📌 Prerequisites

This project was developed using **Python 3.11** and requires the following libraries:

-   **Pandas** for data manipulation
-   **Librosa** for reading and processing audio files
-   **TensorFlow** and **TensorFlow Hub** for neural networks and transfer learning
-   **Scikit-learn** for training traditional machine learning models
-   **Matplotlib** for visualizing results

A `requirements.txt` file with all dependencies can be found in the repository.

## 🛠️ Installation

To run this project, follow the instructions below:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create and activate a virtual environment (optional, but recommended)

```bash
python -m venv venv
```

Activate the environment:

-   On Windows:

    ```bash
    venv\Scripts\activate
    ```

-   On Mac/Linux:
    ```bash
    source venv/bin/activate
    ```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## 🧑🏽‍💻 How to Use

### Step 1: Generate the CSV file with the file paths and corresponding emotions

Run the script `generate_csv_metadata.py` to generate a CSV file containing the file paths and the emotions represented in each audio file. This file will be used for feature extraction in the Jupyter notebooks.

> **Important**: The `generate_csv_metadata.py` script expects the audio files to be located in a folder called `data`. Only audio files (not singing or video files) should be placed in this folder for the script to work correctly.

```bash
python generate_csv_metadata.py
```

### Step 2: Feature Extraction

After generating the CSV, you can use the Jupyter notebooks to extract the audio features. The notebooks are organized as follows:

1. **YAMNet**:

    - Open the notebook `yamnet_feature_extraction.ipynb` to extract features using the YAMNet model.

2. **VGGish**:

    - Open the notebook `vggish_feature_extraction.ipynb` to extract features using the VGGish model.

3. **Mel Spectrograms**:
    - Open the notebook `mel_spectrogram_extraction.ipynb` to extract Mel spectrograms from the audio files.

### Step 3: Train the Classifiers

Once you have extracted the features, you can train the classifiers using the extracted features. The code for this is available in the notebooks, where you can train **SVM**, **Random Forest**, **Naive Bayes**, and **MLP** classifiers to predict emotions from the audio data.

## 🔓 License

This project is licensed under the **GNU General Public License (GPL v3)**. This means that you are free to use, modify, and distribute this code, as long as you share it under the same license. In other words, any derivative work must also be open and licensed under the **GPL v3**.

See the [LICENSE](LICENSE) file for more details.
