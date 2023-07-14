# Django Wildfire Tracker App

The Django Wildfire Tracker App is a web application designed to track and monitor wildfires in real-time. It provides users with a comprehensive platform to stay updated on the latest wildfire incidents, view their locations on an interactive map, and access relevant information such as fire size, containment status, and affected areas.

## Features

- **Real-time Data:** The app fetches data from reliable sources and updates the wildfire information in real-time, ensuring users have the latest information at their fingertips.

- **Interactive Map:** The app displays wildfire incidents on an interactive map, allowing users to visualize the affected areas, fire perimeters, and other relevant details.

- **Detailed Information:** The app provides comprehensive information about each wildfire, including its current location, factors that affect the fire spread and a calculated fire danger index to caution stake holders on how to contain the fire.

## Installation

To install and run the Django Wildfire Tracker App on your local machine, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/meet-tim/wildfire-tracker.git
   ```

2. Navigate to the project directory:

   ```
   cd wildfire-tracker
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

   - On Windows:

     ```
     venv\Scripts\activate
     ```

5. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Open your web browser and navigate to `http://localhost:8000` to access the Django Wildfire Tracker App.

## Configuration

The Django Wildfire Tracker App can be configured by modifying the `config/settings.py` file. You can update the following settings:

- **Database:** Configure the database connection settings according to your requirements. By default, the app uses SQLite for local development.

- **API Integration:** Update the API credentials or endpoints if you wish to use a different wildfire data source.

## Contributing

Contributions to the Django Wildfire Tracker App are welcome! If you encounter any bugs, have feature suggestions, or would like to contribute code improvements, please follow these steps:

1. Fork the repository.

2. Create a new branch:

   ```
   git checkout -b my-feature
   ```

3. Make the necessary changes and commit them:

   ```
   git commit -am 'Add my feature'
   ```

4. Push the changes to your forked repository:

   ```
   git push origin my-feature
   ```

5. Open a pull request on the main repository.

Please ensure your code follows the project's coding conventions and includes appropriate tests and documentation.

## License

The Django Wildfire Tracker is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for both commercial and non-commercial purposes.
