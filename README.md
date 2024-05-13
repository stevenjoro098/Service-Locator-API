# Car Services Locator API

## Overview
This project aims to provide a RESTful API for locating various car services, catering to a wide range of car brands. Developed using Django and Django REST Framework, the API facilitates easy access to information about car service centers including their locations, services offered, and supported car brands.

## Features
- **Location Search**: Users can search for car service centers based on their geographical location.
- **Car Brand Filtering**: Users can filter service centers based on the car brand they own or prefer.
- **Service Offerings**: Information about the services offered by each service center is provided.
- **API Integration**: The API can be easily integrated into web and mobile applications for seamless user experience.

## Installation
1. Clone the repository:
2. Navigate to the project directory:
3. Install dependencies:
4. Apply migrations:
5. Run the development server:

## Usage
### Endpoints
- `/api/services/`: Retrieve a list of all car service centers.
- `/api/services/<pk>/`: Retrieve details of a specific car service center.
- `/api/services/search/`: Search for car service centers based on location and/or car brand.

### Query Parameters
- `latitude` (optional): Latitude of the user's location.
- `longitude` (optional): Longitude of the user's location.
- `brand` (optional): Car brand for filtering the service centers.

### Sample Requests
- Retrieve all service centers:
- Retrieve details of a specific service center:
- Search for service centers near a location:
- Filter service centers by car brand:

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or features you'd like to see.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
