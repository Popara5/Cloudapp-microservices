# Data Processor Service

The Data Processor is a Python microservice designed to handle backend data processing tasks within the CloudSync application. It receives incoming data, processes it, and performs analytics, making the results available to other components in the application.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running the Service](#running-the-service)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Docker](#docker)
- [CI/CD Integration](#cicd-integration)

## Overview
The Data Processor service operates as a REST API and performs backend data operations. It integrates with other services (Node.js real-time service and Laravel authentication) to provide a complete end-to-end solution for data handling in the CloudSync application.

## Technologies Used
- **Python**: Core programming language
- **Flask**: Lightweight framework to serve as a REST API
- **Docker**: Containerizes the service for consistency across environments
- **SonarCloud**: Integrated for code quality and coverage checks
- **GitHub Actions**: CI/CD pipeline for automated testing and deployment

## Setup and Installation

### Prerequisites
- **Python**: Version 3.8 or higher
- **Docker** (optional, for containerized deployment)

### Installation
1. **Clone the repository** and navigate to the `data-processor` directory:
   ```bash
   git clone https://github.com/your-username/CloudSync.git
   cd CloudSync/data-processor
