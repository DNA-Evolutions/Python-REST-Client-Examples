# Use the code-server base image
FROM codercom/code-server:4.91.0-debian

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
    "python-dateutil>=2.5.3" \
    "setuptools>=21.0.0" \
    "urllib3>=1.25.3,<2.1.0" \
    "pydantic>=2" \
    "typing-extensions>=4.7.1" \
    "aiohttp>=3.9.3"

USER root
# Copy entrypoint for pulling example from GitHub on start up
COPY ./jopt-docker-entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/jopt-docker-entrypoint.sh

# Set password for IDE
ENV PASSWORD=jopt

USER coder

# Install Python extension
RUN code-server --install-extension ms-python.python

# Set working directory
WORKDIR /home/coder/project

# Start code-server and bind address
ENTRYPOINT ["/usr/bin/jopt-docker-entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "."]
