[![Build Status](https://travis-ci.org/KabakiAntony/Politico.svg?branch=develop)](https://travis-ci.org/KabakiAntony/Politico) [![Maintainability](https://api.codeclimate.com/v1/badges/2520ce3bfae6e8e38329/maintainability)](https://codeclimate.com/github/KabakiAntony/Politico/test_coverage) [![Coverage Status](https://coveralls.io/repos/github/KabakiAntony/Politico/badge.svg)](https://coveralls.io/github/KabakiAntony/Politico)  [![codecov](https://codecov.io/gh/KabakiAntony/Politico/branch/develop/graph/badge.svg)](https://codecov.io/gh/KabakiAntony/Politico) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/88cda9fd1e4241758ce98192d6bd297d)](https://www.codacy.com/manual/KabakiAntony/Politico?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=KabakiAntony/Politico&amp;utm_campaign=Badge_Grade)


# Politico
 This is a web app that helps the electorate vote and monitor elections.

 Follow the below steps and you will be able to run the app without any challenges 
 the assumption is you already have python installed, any version from 3.* above.

 This application has two versions of the backend v1 and v2. Where v1 is not persistent
 it uses a list data structure to store data and hence the data is overwritten everytime the app
 is reloaded and v2 uses the postgres database to store information hence what we will connect with 
 the UI.

 [Find the UI here](https://kabakiantony.github.io/Politico/UI/)

 [Find the app on heroku](https://kapolitico.herokuapp.com/)

 [Find the API Documentation here](https://kapolitico.docs.apiary.io)

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

      For those that may have a challenge running pytest as I noticed there is a bug getting pytest to 
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
        but the below settings will help override that.
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
| `DELETE` | `/api/v1/offices/<int:office_id>`     | Delete a office by Id                 |

</details>

<details open>

Incase of a bug or anything else use any on the below channels to reach me

[Find me on twitter](https://twitter.com/kabakikiarie) OR  drop me an email at kabaki.antony@gmail.com


