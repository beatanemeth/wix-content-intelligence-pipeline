# Wix Velo Backend Code

The custom JavaScript code designed to run on the **Wix website backend** using Velo is already published in one of my earlier projects with a detailed overview, as well as the code itself.
[Find the code here](https://github.com/beatanemeth/ai-engineering-custom-wix-data-chat/tree/main/getData/wixVeloCode)

## Purpose

This code runs on the Wix platform and implements the necessary HTTP functions to securely expose Wix data to the external FastAPI microservice described in the main README.

- **`http-functions.js`**: Defines the public REST endpoints (`/yourEventsEndpoint`, `/yourPostsEndpoint`, etc.) that the FastAPI service calls.
- **`utils.web.js`**: Contains core logic, specifically the function to **validate and decode the incoming JWT token** and check the associated subject (`sub`) claim against a stored secret.
- **`services.web.js`**: Contains the business logic for querying the actual Wix database collections (Events, Blog, etc.) using Wix APIs.

**Configuration Note:** The JWT signing secret used for authentication must be configured in the Wix Secrets Manager.

## Documentation

[Wix Velo API](https://dev.wix.com/docs/velo)
