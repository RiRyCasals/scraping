FROM python:latest
USER root
RUN pip install selenium
WORKDIR /home
CMD ["bash"]
