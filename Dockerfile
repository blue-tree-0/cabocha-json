FROM python:3.7.7

RUN apt-get update && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    swig \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN echo "Install CRF++"
RUN wget -O /tmp/CRF++-0.58.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ" \
    && cd /tmp \
    && tar zxf CRF++-0.58.tar.gz \
    && cd CRF++-0.58 \
    && ./configure \
    && make \
    && make install \
    && cd / \
    && rm /tmp/CRF++-0.58.tar.gz \
    && rm -rf /tmp/CRF++-0.58 \
    && ldconfig

RUN echo "Install CaboCha"
RUN cd /tmp\
    && curl -c cabocha-0.69.tar.bz2 -s -L "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU" \
    | grep confirm | sed -e "s/^.*confirm=\(.*\)&amp;id=.*$/\1/" \
    | xargs -I{} curl -b  cabocha-0.69.tar.bz2 -L -o cabocha-0.69.tar.bz2 \
    "https://drive.google.com/uc?confirm={}&export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU" \
    && tar jxf cabocha-0.69.tar.bz2 \
    && cd cabocha-0.69 \
    && export CPPFLAGS=-I/usr/local/include \
    && ./configure --with-mecab-config=`which mecab-config` --with-charset=utf8 \
    && make \
    && make install \
    && cd / \
    && rm /tmp/cabocha-0.69.tar.bz2 \
    && rm -rf /tmp/cabocha-0.69 \
    && ldconfig

WORKDIR /cabocha-json
COPY . /cabocha-json
RUN  pip install .
CMD [ "/bin/bash" ]
