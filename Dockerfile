FROM greycilik/cilikuserbot:buster

RUN git clone -b main https://github.com/PayXr/cilik-ubot /home/cilik-ubot/ \
    && chmod 777 /home/cilik-ubot \
    && mkdir /home/cilik-ubot/bin/

COPY ./sample_config.env ./config.env* /home/cilik-ubot/

WORKDIR /home/cilik-ubot/

CMD ["python3", "-m", "CilikUbot"]
