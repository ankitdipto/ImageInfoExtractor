# ImageInfoExtractor

An AI-powered tool that processes images to distinguish scanned documents from regular pictures, and then classifies those documents into their respective domains. This project automates the management of large collections of images and documents by intelligently sorting them.

The pipeline consists of three main components: an **OCR Engine**, a **Spell Checker**, and a **Document Classifier**.

Status: Core components are complete; integration pipeline is pending.

## Features

-   **OCR Text Extraction:** Extracts text from various image formats using the Tesseract OCR engine.
-   **Text Correction:** Improves the accuracy of the extracted text with an integrated spell checker.
-   **Document Classification:** A deep neural network classifies documents into "Computer Science" or "Science" categories with high accuracy (98-99%).
-   **Advanced NLP Pipeline:** Utilizes custom-trained Word2Vec and pre-trained GloVe embeddings for semantic understanding of the text.

## How It Works

The project operates in a three-stage pipeline:

1.  **OCR Engine:** An image is first processed by the OCR engine, which performs several preprocessing steps (resizing, grayscaling, adaptive thresholding) to enhance image quality before using `pytesseract` to extract the raw text.

2.  **Spell Checker:** The extracted text is then passed to a spell-checking module. This script uses `symspellpy` to correct common OCR errors, significantly improving the quality of the text for the next stage.

3.  **Document Classifier:** The corrected text is fed into a sophisticated Natural Language Processing (NLP) model. This model, detailed in the `documentclassification.ipynb` notebook, tokenizes the text, removes stopwords, and performs lemmatization. It then uses a neural network with embedding layers (trained on both custom Word2Vec and pre-trained GloVe vectors) to classify the document.

## Codebase Structure

-   `documentclassification.ipynb`: Contains the complete pipeline for training and evaluating the document classification model.
-   `OCR/python files/OCRengine.py`: The core script for the OCR functionality.
-   `OCR/python files/spellcheckpy.py`: The script for spell-checking the extracted text.
-   `Extracted_txts/`: The output directory where extracted and corrected text files are stored.
-   `OCR/python files/test.py` and `example.py`: Example scripts showing how to use the OCR and spell-checking modules.

## Setup and Installation

1.  **Install Tesseract OCR Engine:**
    This project requires the Tesseract OCR engine to be installed on your system. You can find installation instructions for your OS at the official [Tesseract repository](https://github.com/tesseract-ocr/tesseract).

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ImageInfoExtractor.git
    cd ImageInfoExtractor
    ```

3.  **Install Python dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

    **requirements.txt:**
    ```
    tensorflow
    pandas
    numpy
    scikit-learn
    nltk
    gensim
    opencv-python
    symspellpy
    Pillow
    pytesseract
    ```

## How to Use

Since there is no main entrypoint script, the components can be run individually.

1.  **Extract Text from an Image:**
    -   Place your image in the `OCR/` directory.
    -   Modify `OCR/python files/test.py` to point to your image file.
    -   Run the script:
        ```bash
        python OCR/python files/test.py
        ```
    -   The extracted text will be saved as a `.txt` file in the same directory.

2.  **Correct Spelling in a Text File:**
    -   Place your text file in the `OCR/python files/` directory.
    -   Modify `OCR/python files/example.py` to point to your text file.
    -   Run the script:
        ```bash
        python OCR/python files/example.py
        ```
    -   A new file with the `_corrected.txt` suffix will be created.

3.  **Train the Document Classifier:**
    -   Open and run the `documentclassification.ipynb` notebook in a Jupyter environment.
    -   The notebook loads the preprocessed data, trains the models, and saves the final trained models (`model_C1` and `model_C2`) to disk.

## Future Work

-   **Image Detector:** Implement the "Image Detector-cum-Processor" to filter scanned documents from regular pictures automatically.
-   **Pipeline Integration:** Create a main entrypoint script (`main.py`) to connect all the components into a seamless, end-to-end pipeline.
-   **API and User Interface:** Develop an API and a simple user interface to make the tool more accessible.

## Contributors

-   Ankit Sinha (ankitdipto)
-   Chetanya Kumar Bansal (chetanyaba)
-   Anand Prakash (UnstoppableBRO)
-   Anwoy Chatterjee (C-anwoy)