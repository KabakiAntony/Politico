# Politico
 This is a web app that helps the electorate vote and monitor elections.

 Follow the below steps and you will be able to run the app without any challenges the assumption
 is you already have python installed any version from 3.* and above should run without any challenges

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

   But note if you choose to use "flask run" you don't need to have a run.py module but then you have
   to set the environment variables.
   If you have the run.py and you choose to use it as the entry point of the app 
   then follow this steps 

   NOTE "flask run" defaults to production where the debug mode is off 
        and that denies one the chance of seeing the errors that arise
        but the below settings will help override that 
   ```
      use set on windows and export on linux/mac
      set FLASK_APP=run.py
      set FLASK_DEBUG=1
      SET FLASK_ENV=development
       
   ```
   If you choose to use "python run.py" or whatever other name you may choose to call the apps entry 
   point or main then make sure the module is there and there on in you can configure the app how you
   want, it's worth nothing that app.run() is not advisable to be on the production app.

   

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