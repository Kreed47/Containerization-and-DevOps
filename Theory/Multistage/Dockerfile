# =========================
# Stage 1: Build
# =========================
FROM ubuntu:22.04 AS builder

# Install compiler
RUN apt-get update && apt-get install -y gcc

# Set working directory
WORKDIR /app

# Copy C source code
COPY app.c .

# Compile statically
RUN gcc -static -o sapid_checker app.c


# =========================
# Stage 2: Runtime (minimal)
# =========================
FROM scratch

# Copy compiled binary from builder stage
COPY --from=builder /app/sapid_checker /sapid_checker

# Run the application
CMD ["/sapid_checker"]

