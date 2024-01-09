# Dental Health Management System

Welcome to the Dental Health Management System! This system comprises several microservices written in Python to manage authentication, dentist information, patient records, and notifications. The UI Service, built with Vue 3, provides an intuitive interface for users.

## Table of Contents

- [Services](#services)
  - [Auth Service](#1-auth-service)
  - [Dentist Service](#2-dentist-service)
  - [Patient Service](#3-patient-service)
  - [Notification Service](#4-notification-service)
  - [UI Service (Vue 3)](#5-ui-service-vue-3)
- [Setup](#setup)
- [Usage](#usage)
## Services

### 1. Auth Service

The Auth Service is responsible for user authentication and authorization.

#### Features

- User Registration
- User Login
- Password Recovery
- Token-based Authentication

### 2. Dentist Service

The Dentist Service manages information related to dentists.

#### Features

- Add New Dentists
- Update Dentist Profiles
- Retrieve Dentist Details

### 3. Patient Service

The Patient Service handles patient-related information.

#### Features

- Add New Patients
- Update Patient Records
- Retrieve Patient Details

### 4. Notification Service

The Notification Service is designed for handling various types of notifications.

#### Features

- Send Appointment Reminders
- Provide Updates to Users

### 5. UI Service (Vue 3)

The UI Service serves as the frontend built with Vue 3.

#### Features

- User Authentication
- Appointment Scheduling
- Wishlist Management
- Responsive User Interface

## Setup

Follow the steps below to set up and run the services:

1. **Clone the Repository:**

   ```bash
   git clone https://git.chalmers.se/courses/dit355/2023/student-teams/dit356-2023-07/User.git
## **Install Dependencies**

Navigate to each service folder and install dependencies:
    
```bash
cd auth-service
    pip install -r requirements.txt
```
```bash
cd ../dentist-service  
    pip install -r requirements.txt
```
```bash
cd ../patient-service
    pip install -r requirements.txt
```
```bash
cd ../notification-service
    pip install -r requirements.txt
```
```bash
cd ../ui-service
    npm install
```
## Run Services
 Start each service individually:

 ```bash
    cd auth-service
        python run.py
```
```bash
    cd ../dentist-service
     python app.py
```
```bash
    cd ../patient-service
     python app.py
```
```bash
    cd ../notification-service
     python app.py
```
```bash
    cd ../ui-service
     npm run serve
```

## Usage
- Visit the UI service at http://localhost:8080 and explore the functionalities.
- Make requests to individual service endpoints for backend functionalities.