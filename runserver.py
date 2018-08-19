import subprocess

if __name__ == "__main__":
    run_command = 'export FLASK_APP=urls.py && python3 -m flask run --host 0.0.0.0 --port 5001'
    subprocess.call(run_command, shell=True)