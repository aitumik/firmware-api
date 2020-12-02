# Firmware API and UI
This is a firmware and Web test

## Description
A web app(ui + api) for showing the humidity and temperature posted by esp8266

## Screenshots
<table>
    <tr>
        <td>
            <img alt="open opps 1" src="docs/screenshots/open-opps-01.png">
        </td>
        <td>
            <img alt="open opps 2" src="docs/screenshots/open-opps-02.png">
        </td>
        <td>
            <img alt="open opps 3" src="docs/screenshots/open-opps-03.png">
        </td>
    </tr>
</table>

## Installation
First clone the project into your local machine and navigate to the folder
```bash
git clone https://github.com/aitumik/firmware-api.git
cd firmware-api
```

Create a virtual environment:
```bash
python3 -m venv nameofvirtualenv
```

Activate the virtual environment
```bash
source nameofvirtualenv/bin/activate
```

Install the requirments files
```bash
pip install -r requirements.txt
```

## Usage
Serve the application and make sure that the firmware runs on the same wifi as this server
```bash
python3 manage.py runserver --host 0.0.0.0
```
As soon as the server starts you should start seeing incoming request from the esp8266 server

## Technologies used
* Python
* Flask
* jQuery
* Semantic UI

## Contributing
Pull requests are welcome. For major changes please open an issue first

## License
[MIT](https://choosealicense.com/licenses/mit/)
