# NLP Model Inference Example

- Setup a virtual environment with **Python 3.8** and install the requirements.

    **Using Pip:**
    ```
    virtualenv -p python3.8 <env_name>
    source <env_name>/bin/activate
    pip install -r requirements.txt
    ```
    **Using Anaconda:**
    ```
    conda create python=3.8 --name <env_name> --file requirements.txt
    ```

- Place model folders in **model** folder
- In **inference.py** set `model_dir`and `text` before running the script to get inference results
