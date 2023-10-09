# ExoWeb.AI

ExoWeb.AI is a distributed framework for exoplanets detection using self-supervised machine learning. It enables collaboration between sky observatories, which act as clients, and a central server hosted on Earth.

## Installation

To get started with ExoWeb, follow these steps:

1. Clone the repository from GitHub:

   ```shell
   git clone https://github.com/exowebai/stable.git
   ```

2. Install the required packages:

   ```shell
    pip install -r requirements.txt
    ```

3. Run the system:

   ```shell
   python system.py
   ```

## Usage

Once you have ExoWeb.AI up and running, you can access the Flask web app by opening your web browser and navigating to:
    
    http://localhost:5000

## Architecture

The overall architecture if the application looks like this :

![image](https://github.com/HamzaBamohammed/exoplanet-network/assets/114748477/7b6795e2-a0c7-4092-aef0-1afa69ff0ad3)

Clients (observatories) send their collected data, which will be preprocessed, then classified using a machine learning model. This model will continuously learn and retrain itself to improve it's accuracy in predicting potential exoplanets from the collected data.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

ExoWeb.AI is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

## Acknowledgements

ExoWeb.AI is a project developed by [Hamza Bamohammed](https://github.com/HamzaBamohammed), [Rihab Boudkour](http://github.com/RihabBoudkour), [Meryem El Karati](http://github.com/Cristal32)

## Contact

For any questions or suggestions, please contact us at []
