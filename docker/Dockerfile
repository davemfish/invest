# syntax=docker/dockerfile:1

# Build the InVEST wheel in a separate container stage
FROM debian:12.2 as build
ARG INVEST_VERSION="main"
ARG INVEST_REPO="natcap/invest"

# Create the container for distribution that has runtime dependencies.
FROM mambaorg/micromamba:1.5.0-bookworm-slim
RUN apt update && apt install -y git
RUN cd / && \
        git clone https://github.com/${INVEST_REPO}.git && \
        cd $(basename ${INVEST_REPO}) && \
        git checkout ${INVEST_VERSION}

# The environment.yml file will be built during github actions.
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -c conda-forge -f /tmp/environment.yml && \
        micromamba install build && \
        micromamba clean --all --yes && \
        /opt/conda/bin/python -m build && \
        /opt/conda/bin/python -m pip install /tmp/*.whl && \
        /opt/conda/bin/python -m pip cache purge && \
        micromamba remove -y -n base cxx-compiler git

ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]
