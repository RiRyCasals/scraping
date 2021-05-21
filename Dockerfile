FROM python:latest
USER root
RUN pip install selenium requests
WORKDIR /home
CMD ["bash"]
