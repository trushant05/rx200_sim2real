#====================================================================
# Stage 1: Base Image Setup (Isaac Sim 4.5.0)
#====================================================================
ARG ISAAC_SIM_TAG=4.5.0
FROM nvcr.io/nvidia/isaac-sim:$ISAAC_SIM_TAG

ENV DEBIAN_FRONTEND=noninteractive

# Install essential system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg2 \
    lsb-release \
    software-properties-common \
    locales \
    tmux \
    htop \
    vim \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set up locales
ENV LANG=en_US.UTF-8
RUN locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8


# ===================================================================
# Stage 2: Setup Isaac Sim Paths
# ===================================================================
# Setup Isaac Sim environment variables
ENV ISAAC_SIM_PATH=/isaac-sim
ENV CARB_APP_PATH=${ISAAC_SIM_PATH}
ENV ISAAC_PATH=${ISAAC_SIM_PATH}
ENV EXP_PATH=${ISAAC_PATH}/_build/linux-x86_64/release/exts
ENV OMNIVERSE_KIT_PATH=/opt/nvidia/omniverse/kit
ENV OMNI_KIT_ALLOW_ROOT=1

# Source Isaac Sim 4.5 environment in .bashrc
RUN echo "source ${ISAAC_SIM_PATH}/setup_python_env.sh" >> /root/.bashrc


# ===================================================================
# Stage 3: Use Internal ROS2 Humble
# ===================================================================

RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ISAAC_SIM_PATH/exts/isaacsim.ros2.bridge/humble/lib" >> /root/.bashrc


#====================================================================
# Stage 4: Install Python Packages from requirements.txt
#====================================================================
# Copy the requirements.txt file to the container
COPY ./requirements.txt /tmp/requirements.txt

# Install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt

# Default command
CMD ["/bin/bash"]
