# Use the code-server base image
FROM codercom/code-server:4.96.4-debian

# Set the DEBIAN_FRONTEND environment variable to avoid interactive prompts during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and git
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    git

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv

# Change ownership of the virtual environment to the coder user
RUN chown -R coder:coder /opt/venv

USER coder
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip in the virtual environment
RUN pip install --upgrade pip

# Install the required Python packages in the virtual environment
RUN pip install \
    "python-dateutil>=2.8.2" \
    "setuptools>=21.0.0" \
    "urllib3>=2.1.0,<3.0.0" \
    "pydantic>=2" \
    "typing-extensions>=4.7.1" \
    "aiohttp>=3.9.3" \
    "jupyter>=1.0.0" \
    "ipykernel>=6.0.0"

USER root
# Copy entrypoint for pulling example from GitHub on start up
COPY ./jopt-docker-entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/jopt-docker-entrypoint.sh

# Set password for IDE
ENV PASSWORD=jopt

USER coder

# Install Python and Jupyter extensions
RUN code-server --install-extension ms-python.python && \
    code-server --install-extension ms-toolsai.jupyter

# Register the venv as a Jupyter kernel
RUN /opt/venv/bin/python -m ipykernel install --user --name=jopt-venv --display-name="Python (JOpt)"

# Set working directory
WORKDIR /home/coder/project

# Start code-server and bind address
ENTRYPOINT ["/usr/bin/jopt-docker-entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "."]
