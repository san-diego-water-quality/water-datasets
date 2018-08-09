FROM conda/miniconda3

  
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
 git ffmpeg \
 build-essential \
 vim \
 jed \
 libsm6 \
 libxext-dev \
 libxrender1 \
 lmodern \
 netcat \
 pandoc \
 python-dev \
 texlive-fonts-extra \
 texlive-fonts-recommended \
 texlive-generic-recommended \
 texlive-latex-base \
 texlive-latex-extra \
 texlive-xetex \
 unzip \
 nano \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
  
RUN conda install -y numpy pandas scipy scikit-learn \
    statsmodels ipython ipykernel jupyter 
  
RUN mkdir -p /opt/metapack
 
ADD cmd.sh /opt/metapack
ADD entrypoint.sh /opt/metapack
 
WORKDIR /opt/metapack


