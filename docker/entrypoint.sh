#!/bin/bash

# Exit immediately if a command fails
set -e

# Log container start
echo "Starting Isaac Sim (4.5.0) inside Docker ..."

# Run Isaac Sim (4.5.0)
python3 /home/workspaces/docker/sim.py

# Keep the container running
exec /bin/bash
