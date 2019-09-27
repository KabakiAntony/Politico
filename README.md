[![Build Status](https://travis-ci.org/KabakiAntony/Politico.svg?branch=develop)](https://travis-ci.org/KabakiAntony/Politico)

[![Maintainability](https://api.codeclimate.com/v1/badges/2520ce3bfae6e8e38329/maintainability)](https://codeclimate.com/github/KabakiAntony/Politico/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/2520ce3bfae6e8e38329/test_coverage)](https://codeclimate.com/github/KabakiAntony/Politico/test_coverage)

[![Coverage Status](https://coveralls.io/repos/github/KabakiAntony/Politico/badge.svg?branch=develop)](https://coveralls.io/github/KabakiAntony/Politico?branch=develop)


# Politico
 This is a web app that helps the electorate vote and monitor elections.

 Follow the below steps and you will be able to run the app without any challenges the assumption
 is you already have python installed any version from 3.* and above should run without any challenges
 
 Find the frontend for this app hosted on gh-pages on the following link https://kabakiantony.github.io/Politico/UI/

## Setup and installation

1. Set up virtualenv

   ```bash
        virtualenv venv
   ```

2. Activate virtualenv on linux and windows  as below

   ```bash
      LINUX/MAC

       source venv\bin\activate

      WINDOWS

       venv\Scripts\activate
      
   ```

3. Install dependencies

   ```bash
        pip install -r requirements.txt
   ```


4. Running tests

   ```
      python -m pytest --cov=app/api 

      For the machines that may have a challenge running pytest as I noticed there is a bug getting pytest to 
      run on some windows machines then run the tests with  the below command. 

      python -m nose2 -v 

      The difference is that nose2 will not run coverage you will have to invoke coverage on your own

   ```

5. Start the server

   ```
      flask run or python run.py 
   ```
 NOTE "flask run" defaults to production where the debug mode is off 
        and that denies one the chance of seeing the errors that arise
        but the below settings will help override that 
   ```
      use set on windows and export on linux/mac
      set FLASK_APP=run.py
      set FLASK_DEBUG=1
      SET FLASK_ENV=development
       
   ``` 

<details>
<summary>V1 Politico Endpoints</summary>

| Method   | Endpoint                              | Description                           |
| -------- | ------------------------------------- | ------------------------------------- |
| `GET`    | `/api/v1/offices`                     | view all offices created by admin     |
| `POST`   | `/api/v1/offices`                     | create a new office                   |
| `GET`    | `/api/v1/offices/<int:office_id>`     | Get a specific office by id           |
| `GET`    | `/api/v1/parties`                     | View all parties created by admin     |
| `POST`   | `/api/v1/parties`                     | create a new party                    |
| `GET`    | `/api/v1/parties/<int:party_id>`      | Get specific party Id                 |
| `PATCH`  | `/api/v1/parties/<int:party_id>/name` | modify a party by name                |
| `PATCH`  | `/api/v1/offices/<int:office_id>/name`| modify an office by name              |
| `DELETE` | `/api/v1/parties/<int:party_id>`      | Delete a party by Id                  |

</details>

<details open>


Done by Kabaki Antony find me on twitter https://twitter.com/kabakikiarie
