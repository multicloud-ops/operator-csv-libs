FROM python:3.8-alpine as base
FROM base as builder

# Run multistage build to save some space on the resulting image
RUN apk add git
RUN apk add --update build-base libffi-dev
RUN mkdir /install
WORKDIR /install
COPY /docker/requirements.txt /requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install --no-warn-script-location --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local

WORKDIR /app

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["-c", "print('Please specify python script to run')"]
