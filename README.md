# CI/CD Server for Automatic Deployment

This repository contains the FastAPI application that serves as a CI/CD server, specifically set up for Continuous Deployment (CD) using GitHub webhooks.

## Overview

The server listens for webhook notifications from GitHub indicating that a new commit has been pushed to the `cornerstone3d` branch. Upon receiving a valid webhook request, it automatically executes a series of deployment commands.

## Setup

### Requirements

- Python 3.8+
- FastAPI
- Docker
- Git installed on the deployment server

### Installation

1. Clone the repository to your local machine/server:

   ```shell
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. Navigate to the cloned directory:

   ```shell
   cd yourrepository
   ```

3. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up environment variables as needed for your deployment environment.

5. Ensure Docker is running and that you have Docker Compose installed.

## Running the Server

To run the CI/CD server, use the following command:

```shell
uvicorn main:app --host 0.0.0.0 --port 8000
```

Replace `main:app` with the appropriate module and FastAPI app instance name if different.

## Webhook Configuration

Configure your GitHub repository to send webhook notifications to your server:

1. Go to your repository on GitHub.
2. Click on 'Settings' > 'Webhooks'.
3. Click 'Add webhook'.
4. Set the 'Payload URL' to your server's address (e.g., `http://yourserver.com/webhook`).
5. Choose 'application/json' for the 'Content type'.
6. Set a secret and store it securely.
7. Choose 'Just the push event'.
8. Ensure 'Active' is checked.
9. Click 'Add webhook'.

## Security Note

Before going into production, ensure that you secure your webhook endpoint by verifying the incoming webhook secret.

## Contributing

Contributions to this CI/CD server are welcome. Please ensure that you write tests for new features and that all tests pass before opening a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
