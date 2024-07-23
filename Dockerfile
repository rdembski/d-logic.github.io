# Dockerfile

FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    git-lfs \
    ffmpeg \
    libsm6 \
    libxext6 \
    cmake \
    rsync \
    libgl1-mesa-glx \
    tesseract-ocr \
    python3-pip \
    && rm -rf /var/lib/apt/lists/* \
    && git lfs install

# Set environment variables for CUDA
ENV CUDA_HOME=/usr/local/cuda
ENV PATH=$CUDA_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install streamlit

# Copy the application files
COPY . .

# Expose the ports the apps run on
EXPOSE 7860 8501

# Command to run both the Gradio app and Streamlit app
CMD streamlit run image_analyzer.py --server.port 8501 & python3 app.py
