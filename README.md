# Using Chainlit for any Bot creation...
## documentation link: https://docs.chainlit.io/get-started/overview


```bash
conda create -n chainlit python=3.10 -y
```

```bash
conda activate chainlit
```

# If setup.py needs to be installed seprately, normall it will be executed as "-e ." in requirements.txt file
```bash
python setup.py install
```
```bash
pip install -r requirements.txt
```
# Command to check Chainlit is working
chainlit hello

# Command to run the application
chainlit run app.py