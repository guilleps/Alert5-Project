FROM tensorflow/serving:latest

COPY models /models/1

ENV MODEL_NAME=1


ENTRYPOINT ["/usr/bin/tensorflow_model_server", "--rest_api_port=10000", "--model_name=1", "--model_base_path=/models/1"]