FROM python:3.11-slim

WORKDIR /app

# Copy code + tests
COPY src/ ./src/
COPY test/ ./test/

# Make src importable
ENV PYTHONPATH=/app

# Run all unit tests under ./tests
CMD ["python", "-m", "unittest", "discover", "-s", "test", "-p", "test*.py", "-v"]