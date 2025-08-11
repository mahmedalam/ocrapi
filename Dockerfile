# ---- Base Image ----
FROM python:3.13-slim

# Install uv (ultra-fast Python package installer)
RUN pip install --no-cache-dir uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Compile dependencies to requirements.txt and install them
RUN uv pip compile pyproject.toml --no-header > requirements.txt \
    && uv pip install --system --no-cache --upgrade -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Start FastAPI using uvicorn (production mode)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
