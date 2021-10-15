FROM python:3.7-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
RUN pip install . --use-feature=in-tree-build
EXPOSE 8050
CMD ["python", "src/navara_dash/app.py"]