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
 unzip \
 nano \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
  
RUN conda install -y  Markdown PyYAML SQLAlchemy appdirs \
	beautifulsoup4 boto3  chardet \
	filelock  ipykernel ipython jmespath jupyter numpy \
	pandas petl requests s3transfer scikit-learn scipy statsmodels 
	  
  
RUN mkdir -p /opt/metapack
 
ADD cmd.sh /opt/metapack
ADD entrypoint.sh /opt/metapack
ADD build /opt/metapack
 
WORKDIR /opt/metapack

ENTRYPOINT ["/opt/metapack/entrypoint.sh"]

#CMD ["/opt/metapack/cmd.sh"]
