import os
import re
from dotenv import load_dotenv

load_dotenv()

from pollo.agents.draft.writer import generate_drafts_from_topics

# Define the base directory where topic folders are located
base_dir = "."  # Change this to your actual base directory path

# Define directories to exclude from processing
EXCLUDE_DIRS = [
    "01. Vector Spaces",
    "02. Matrices",
    "03. Determinants"
]

# Get all directories in the base directory
all_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Filter directories matching the pattern "[0-9+]. [Topic Name]"
topic_dirs = [d for d in all_dirs if re.match(r"^\d+\.\s+.+$", d)]

# Exclude directories that are in the EXCLUDE_DIRS list
topic_dirs = [d for d in topic_dirs if d not in EXCLUDE_DIRS]

# Define the perspectives for all topics
basic_perspective = "Focus on the foundational concepts of linear algebra, including vector spaces, matrices, determinants, and norms. Explore the theoretical foundations, properties, and applications of these concepts in mathematical analysis and computational problems."
advanced_perspective = "Focus on advanced linear algebra topics, including eigendecomposition, singular value decomposition, spectral theorems, and special matrices like Hermitian and Hadamard matrices. Address computational methods for solving linear systems and applications in rotation representations using quaternions."

# Process each topic directory
for directory in topic_dirs:
    print(f"Processing directory: {directory}")
    generate_drafts_from_topics(
        directory=directory,
        perspectives=[
            basic_perspective,
            advanced_perspective,
        ],
        json_per_perspective=1,
        branching_factor=5
    )
    
print(f"Processed {len(topic_dirs)} topic directories")