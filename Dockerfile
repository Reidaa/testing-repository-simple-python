FROM python:3.11-slim

# Install uv package manager from ghcr.io/astral-sh/uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# copy all the files to the container
COPY --link src/ src/
COPY --link app.py uv.lock pyproject.toml ./

RUN uv sync --frozen --no-dev --no-cache

ENTRYPOINT [ "uv", "run",  "app.py" ]